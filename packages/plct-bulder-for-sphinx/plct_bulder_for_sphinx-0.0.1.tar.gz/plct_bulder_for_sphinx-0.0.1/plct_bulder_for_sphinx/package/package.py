from copy import deepcopy
import os
import shutil
import tempfile
import mimetypes
import zipfile

from pkg_resources import resource_filename

from .util import apply_template_dir, make_zip_delete_src, ensure_dir
from .moodleclasses import *


class ScormProxyPackager:
    def __init__(self, course_config, json_file_path, export_path) -> None:
        self.course_id :str = os.path.basename(os.getcwd())
        self.json_file_path : str= json_file_path
        self.export_path : str = export_path
        self.export_path = os.path.join(self.export_path, 'scorm')
        self.moodle_path = export_path+'/moodle'
        ensure_dir(self.export_path)
        ensure_dir(self.moodle_path)
        self.course_scorm_export_path : str = os.path.join(
            self.export_path, self.course_id + '_scorm')
        self.course_parts_scorm_export_path : str = os.path.join(
            self.export_path,   self.course_id + '_scorm_activity')
        self.course_config   =course_config
        self.course_config.id =  self.course_id
        self.package_conf : dict[str,str] = {}
        self.package_conf['data_content_url'] = self.course_config.content_uri
        self.package_conf['title'] = self.course_config.title
        self.package_conf['identifier'] = self.course_id

    def create_package_for_course(self):
        apply_template_dir(resource_filename(
            'plct_bulder_for_sphinx', 'scorm-proxy-templates'), self.course_scorm_export_path, self.package_conf)
        shutil.copyfile(self.json_file_path, os.path.join(
            self.course_scorm_export_path, 'course.json'))
        make_zip_delete_src(self.course_scorm_export_path)

    def create_packages_for_activities(self):
        self.course_config.add_index_pages(self.course_config.toc_tree)
        for course_node in self.course_config.toc_tree.children:
            for node in course_node.children:
                course_node_zip_path = os.path.join(
                    self.course_parts_scorm_export_path, node.docname)
                apply_template_dir(resource_filename(
                    'plct_bulder_for_sphinx', 'scorm-proxy-templates'), course_node_zip_path, self.package_conf)
                course_copy = deepcopy(self.course_config)
                course_copy.toc_tree = node
                course_copy.create_JSON_file(os.path.join(course_node_zip_path, 'course.json'))
                make_zip_delete_src(course_node_zip_path)
        make_zip_delete_src(self.course_parts_scorm_export_path)

    def create_moodle_backup(self):
        archive_index_lines = []
        course_scorm_zip_path = self.course_id + '_scorm_activity.zip'
        course_scorm_zip_path = os.path.join(
            self.export_path, course_scorm_zip_path)
        temp_dir = tempfile.TemporaryDirectory()
        moodle_backup_file = zipfile.ZipFile(self.moodle_path + '/' + self.course_id + '.mbz', 'w')
        activity_aggregationcoef2 = round(1/(self.course_config.number_of_active_nodes), 5)
        sort_order = 0
        section_sort_order = 0
        with zipfile.ZipFile(course_scorm_zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir.name)
            moodle_course = MoodleCourse(self.course_config)
            moodle_backup_file.write(temp_dir.name, 'course')
            copied_files = []
            for node in self.course_config.toc_tree.children:
                section_sort_order += 1
                moodle_section = MoodleSection(node, section_sort_order)
                moodle_course.sections.append(moodle_section)
                moodle_backup_file.write(
                    temp_dir.name, moodle_section.section_dir_path)
                for subnode in node.children:
                    sort_order += 1
                    moodle_activity = MoodleActivity(
                        subnode, activity_aggregationcoef2, sort_order, self.course_id)
                    moodle_section.add_activity(moodle_activity)
                    moodle_backup_file.write(
                        temp_dir.name, moodle_activity.activity_dir_path)
                    file_path = os.path.join(
                        temp_dir.name, subnode.docname + '.zip')
                    moodle_activity.sah1 = Sha1Hasher(file_path)
                    moodle_activity.file_size = str(os.path.getsize(file_path))
                    with zipfile.ZipFile(file_path, 'r') as zip_scorm_file_ref:
                        temp_dir_scorm = tempfile.TemporaryDirectory()
                        zip_scorm_file_ref.extractall(temp_dir_scorm.name)
                        moodle_activity.add_file(MoodleFile(
                            '.', 'da39a3ee5e6b4b0d3255bfef95601890afd80709', '$@NULL@$', '', '0', 'content'))
                        moodle_activity.add_file(MoodleFile(
                            '.', 'da39a3ee5e6b4b0d3255bfef95601890afd80709', '$@NULL@$', '', '0', 'package'))
                        for file in os.listdir(temp_dir_scorm.name):
                            path = os.path.join(temp_dir_scorm.name, file)
                            hash_file_name = Sha1Hasher(path)
                            mime_type, _ = mimetypes.guess_type(path)
                            rel_path = os.path.relpath(
                                path, temp_dir_scorm.name)
                            file_size = os.path.getsize(path)
                            moodle_file = MoodleFile(
                                file, hash_file_name, mime_type, rel_path, file_size, 'content')
                            moodle_activity.add_file(moodle_file)
                            if hash_file_name not in copied_files:
                                copied_files.append(hash_file_name)
                                moodle_backup_file.write(
                                    path, 'files/' + hash_file_name[0:2] + '/' + hash_file_name)
                    moodle_activity.add_file(MoodleFile(
                        file_path, moodle_activity.sah1, '$@NULL@$', '', '0', 'content'))
                    moodle_backup_file.write(
                        file_path, 'files/' + moodle_activity.sah1[0:2] + '/' + moodle_activity.sah1)
                    moodle_activity.extract_activity_data()
                    apply_moodle_template_dir(resource_filename('plct_bulder_for_sphinx', 'moodle-templates/activities'),
                                              moodle_backup_file, root_copy_path=moodle_activity.activity_dir_path, xml_data=moodle_activity.xml_data)

                moodle_section.extract_section_data()
                apply_moodle_template_dir(resource_filename('plct_bulder_for_sphinx', 'moodle-templates/sections'),
                                          moodle_backup_file, root_copy_path=moodle_section.section_dir_path, xml_data=moodle_section.xml_data)
            moodle_course.extract_corse_data()
            apply_moodle_template_dir(resource_filename('plct_bulder_for_sphinx', 'moodle-templates'),
                                      moodle_backup_file, filter_name=['activities', 'sections'], xml_data=moodle_course.xml_data)
        moodle_backup_file.close()
        temp_dir.cleanup()

        temp_dir = tempfile.TemporaryDirectory()
        with zipfile.ZipFile(self.moodle_path + '/' + self.course_id + '.mbz', 'a') as zip_ref:
            zip_ref.extractall(temp_dir.name)
            total_entries = 0
            for root, dirs, files in os.walk(temp_dir.name):
                total_entries += len(files) + len(dirs)
            for root, dirs, files in os.walk(temp_dir.name):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(
                        file_path, temp_dir.name).replace('\\', '/')
                    file_size = os.path.getsize(file_path)
                    creation_time = round(os.path.getctime(file_path))
                    archive_index_lines.append(
                        rel_path + '\tf\t' + str(file_size) + '\t' + str(creation_time))
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    rel_path = os.path.relpath(
                        dir_path, temp_dir.name).replace('\\', '/')
                    archive_index_lines.append(
                        rel_path + '/' + '\td\t' + '0\t?')
            archive_index_lines.sort()
            archive_index_lines.insert(
                0, ('Moodle archive file index. Count: ' + str(total_entries)))

            zip_ref.writestr('.ARCHIVE_INDEX', '\n'.join(archive_index_lines))

            zip_ref.close()


