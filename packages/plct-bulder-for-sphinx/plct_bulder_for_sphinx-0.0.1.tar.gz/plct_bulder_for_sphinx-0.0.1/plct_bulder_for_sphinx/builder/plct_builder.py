import json
import re
import os
import urllib.parse

from os import path
from pkg_resources import resource_filename
from typing import Iterable, Sequence
from docutils import nodes

from sphinx.application import Sphinx, BuildEnvironment
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.util.fileutil import copy_asset
from sphinx.util.matching import DOTFILES
from sphinx.util.osutil import os_path
from sphinx.environment.adapters.toctree import TocTree

from ..package.package import ScormProxyPackager


SHPINX_TO_ISO_LANGUAGE_CODES = {
    'sr_RS': 'sr-Cyrl',
    'sr': 'sr-Cyrl',
    'sr@latn': 'sr-Latn'
}

SKIP_CLASS_ATTRIBUTES = ['course_config_json_file_path',
                         ]


class PLCTBuilder(StandaloneHTMLBuilder):
    name = 'plct_builder'
    bc_outdir = 'bc_html'

    def __init__(self, app, env=None):
        super().__init__(app, env)
        if self.outdir.endswith("static_website"):
            self.rootdir = self.outdir
        else:
            self.rootdir = os.path.join(self.outdir, "static_website")

        self.outdir =  os.path.join(self.rootdir,"bc_html")
        self.app.outdir = self.outdir
        player_files = resource_filename('plct_bulder_for_sphinx', 'player/player')
        copy_asset(player_files, path.join(self.rootdir, 'assets'), excluded=DOTFILES)
        static_files = resource_filename('plct_bulder_for_sphinx', 'player/content')
        copy_asset(static_files, path.join(self.outdir, '_platform'), excluded=DOTFILES)

        app.add_js_file('../_platform/petljaRTBundle.js')
        app.add_js_file('../_platform/content.js')

        self.search = False
        
    def dump_search_index(self) -> None:
        pass

    def write_buildinfo(self) -> None:
        pass

    def dump_inventory(self) -> None:
        pass

    def write_genindex(self) -> None:
        pass

    def get_outfilename(self, pagename: str) -> str:
        return path.join(self.outdir, os_path(pagename) + self.out_suffix)
    
    def write(self, build_docnames: Iterable[str], updated_docnames: Sequence[str], method: str = 'update') -> None:
        super().write(build_docnames, updated_docnames, method)
        self.app.add_message_catalog('sphinx', resource_filename('plct_bulder_for_sphinx', 'player/locale'))
        self.handle_page('player', addctx={}, templatename=resource_filename(
            'plct_bulder_for_sphinx', 'player/player.html'),
                            outfilename=path.join(self.rootdir, 'index.html'))
        

def get_toc_dict(app: Sphinx, env: BuildEnvironment) -> None:
    if not isinstance(app.builder, PLCTBuilder):
        return
    course_config = CourseConfig(app, env)

    if 'scorm' in app.config.additional_build_targets:
        if course_config.content_uri == '':
            raise Exception('Content uri must be set for scorm export')
        export_path = path.join(app.builder.rootdir, '..')
        scorm_package = ScormProxyPackager(
            course_config,
            course_config.course_config_json_file_path,
            export_path)
        scorm_package.create_package_for_course()
        scorm_package.create_packages_for_activities()
        scorm_package.create_moodle_backup()

class TocTreeNode:
    def __init__(self, title: str, doc_path: str):
        self.title: str = title
        self.doc_path: str = doc_path
        self.docname: str = os.path.splitext(self.doc_path)[0]
        self.children: list[TocTreeNode] = []
        self.meta_data: dict[str, str] = {}

        self.meta_data['anchor_link'] = bool(
            re.search(r"#.*$", self.doc_path))
        if self.meta_data['anchor_link']:
            self.meta_data['anchor'] = re.search(r"#.*$", self.doc_path).group()
            self.doc_path = re.sub(r'#.*$', '', self.doc_path)

    def toJSON(self) -> dict:
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
                                     sort_keys=True))
    
    def is_active(self) -> bool:
        if 'status' in self.meta_data and self.meta_data['status'] == 'exclude':
            return False
        return True


class CourseConfig:
    def __init__(self, app: Sphinx, env : BuildEnvironment) -> None:
        self.title: str = app.config.project
        self.content_uri: str = app.config.content_uri
        self.include_toc : bool = app.config.include_toc
        self.number_of_active_nodes : int = 0
        
        self.toc_tree = TocTreeNode(find_title(env.get_doctree(env.config.root_doc)),app.config.root_doc + app.builder.out_suffix)
        build_toc_tree(TocTree(app.env).get_toctree_for("index", app.builder, collapse=False, maxdepth ="10"), self.toc_tree)
        self.cut_anchor_links(self.toc_tree)
        
        self.count_active_nodes(self.toc_tree)
        self.add_metadata_to_nodes(app.env.metadata)

        self.description: str = self.toc_tree.meta_data['description'] if 'description' in self.toc_tree.meta_data else ''

        self.outdir = app.outdir
        self.course_config_json_file_path: str = path.join(
            app.outdir, '..','course.json')
        
        self.create_json()

    def add_metadata_to_nodes(self, metadata) -> None:
        input_metadata(self.toc_tree, metadata)

    def toJSON(self) -> dict:
        return json.loads(json.dumps(self, default=lambda o: {k: v for k, v in o.__dict__.items() if k not in SKIP_CLASS_ATTRIBUTES},
                                     sort_keys=True))

    def create_JSON_file(self, path) -> None:
        with open(path, 'w+', encoding='utf-8') as file:
            json.dump(self.toJSON(), file)

    def create_json(self):
        with open(self.course_config_json_file_path, 'w+', encoding='utf-8') as file:
            json.dump(self.toJSON(), file)
    
    def count_active_nodes(self, node : TocTreeNode) -> None:
        if node.is_active():
            self.number_of_active_nodes += 1
        for child in node.children:
            self.count_active_nodes(child)
    
    def add_index_pages(self, node : TocTreeNode, depth = 0) -> None:
        if depth == 2:
            return
        if node.is_active() and (len(node.children) == 0 or depth <2):
            node.meta_data['status'] = "exclude"
            node.children.insert(0,TocTreeNode(node.title,node.doc_path))   
        for child in node.children:
            self.add_index_pages(child, depth= depth + 1)

    def cut_anchor_links(self, node):
        if all([child.meta_data['anchor_link'] for child in node.children]):
            new_children = []
            for child in node.children:
                new_children+= child.children
            node.children = new_children

        for child in node.children:
            self.cut_anchor_links(child)

def build_toc_tree(node: TocTree, parent: TocTreeNode = None) -> TocTreeNode:
    if node is None:
        # course with no content
        return None
    
    if node.tagname == 'reference':
        refuri = urllib.parse.unquote(node.get('refuri'), encoding='utf-8')
        title = urllib.parse.unquote(
            node.children[0].astext(), encoding='utf-8')
        return TocTreeNode(title, refuri)

    if node.tagname == 'compact_paragraph':
        if len(node.children) == 1:
            return build_toc_tree(node.children[0], parent)
        else:
            return build_toc_tree(node.children[1], parent)

    if node.tagname == 'list_item':
        if len(node.children) == 1:
            return build_toc_tree(node.children[0], parent)
        else:
            item_parent = build_toc_tree(node.children[0])
            for child in node.children[1:]:
                build_toc_tree(
                    child, item_parent)
            return item_parent

    if node.tagname == 'bullet_list':
        for child in node.children:
            parent.children.append(build_toc_tree(child, parent))  
        return parent


def input_metadata(node: TocTreeNode, metadata: dict[str, str]) -> None:
    node.meta_data.update(metadata[node.docname])
    for child in node.children:
        input_metadata(child, metadata)

def find_title(node : nodes.document) -> str:
    if node.tagname == 'comment':
        return ''
    if node.tagname == 'title':
        return node.astext()
    for child in node:
        result = find_title(child)
        if result:
            return result
    return ''


ensure_dir = lambda file_path: os.makedirs(file_path, exist_ok=True)
 

def setup(app: Sphinx):
    app.add_config_value('additional_build_targets', [], 'env', list['str'])
    app.add_config_value('content_uri', '', 'env')
    app.add_config_value('include_toc', True, 'env', bool)
    app.connect('env-updated', get_toc_dict)
    app.add_builder(PLCTBuilder)