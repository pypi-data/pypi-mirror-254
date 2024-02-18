
from .util import *
import xml.etree.cElementTree as ET

class MoodleSection:
    def __init__(self, lesson_node , sort_order : int):
        self.id = get_unused_id()
        self.sort_order = sort_order
        self.title = lesson_node.title
        self.activities = []
        self.section_dir_path = '/sections/section_' + str(self.id)
        self.xml_data = {}

    def extract_section_data(self):
        time_stamp = get_time_stamp()
        self.xml_data = {
            'section': {
                "attributes": {"id": self.id},
                './number': str(self.sort_order),
                './name':  self.title,
                './sequence':  ','.join([activity.module_id for activity in self.activities]),
                './timemodified': time_stamp,
            }
        }

    def add_activity(self, activity):
        self.activities.append(activity)
        activity.section_id = self.id
        activity.section_order = self.sort_order


class MoodleCourse:
    def __init__(self, course_data):
        self.course_data = course_data
        self.sections = []
        self.activity_et_elements = []
        self.section_et_elements = []
        self.setting_et_elements = []
        self.file_et_elements = []
        self.xml_data = {}

    def extract_corse_data(self):
        self._make_file_et_elements()
        time_stamp = get_time_stamp()
        self.xml_data = {
            'moodle_backup': {
                "./information/name": "-".join([self.course_data.id, 'nu.mbz']),
                "./information/backup_date": time_stamp,
                "./information/original_course_fullname": self.course_data.title,
                "./information/original_course_shortname": self.course_data.id,
                "./information/original_course_startdate": time_stamp,
                "./information/contents/course/title": self.course_data.id,
                "./information/settings/setting[1]/value":  "-".join([self.course_data.id, 'nu.mbz']),
                "./information/contents/activities": self.activity_et_elements,
                "./information/contents/sections": self.section_et_elements,
                "./information/settings": self.setting_et_elements,
            },
            'files': {
                "root_elements": self.file_et_elements
            },
            'course': {
                "./shortname": self.course_data.id,
                "./fullname": self.course_data.title,
                "./summary": self.course_data.description,
                "./startdate": time_stamp,
                "./timecreated": time_stamp,
                "./timemodified": time_stamp,
            },
        }

    def _make_file_et_elements(self):
        for section in self.sections:
            self.section_et_elements.append(
                self._make_et_section_element(section))
            for activity in section.activities:
                self.activity_et_elements.append(
                    self._make_activity_et_element(section, activity))
                for file in activity.activity_files:
                    el = self._make_file_et_element(file, activity)
                    self.file_et_elements.append(el)

        for section in self.sections:
            self.setting_et_elements.append(
                self._make_setting_et_element_section_included(section))
            self.setting_et_elements.append(
                self._make_setting_et_element_section_userinfo(section))
            for activity in section.activities:
                self.setting_et_elements.append(
                    self._make_setting_et_element_activity_included(activity))
                self.setting_et_elements.append(
                    self._make_setting_et_element_activity_userinfo(activity))
                self.file_et_elements.append(
                    self._make_activity_file_et_elements(activity))

    def _make_activity_file_et_elements(self, activity):
        el = ET.Element("file", {"id": get_unused_id()})
        ET.SubElement(el, "contenthash").text = activity.sah1
        ET.SubElement(el, "contextid").text = activity.context_id
        ET.SubElement(el, "component").text = 'mod_scorm'
        ET.SubElement(el, "filearea").text = 'content'
        ET.SubElement(el, "itemid").text = '0'
        ET.SubElement(el, "filepath").text = '/'
        ET.SubElement(el, "filename").text = activity.activity_node.title + ".zip"
        ET.SubElement(el, "userid").text = '$@NULL@$'
        ET.SubElement(el, "filesize").text = activity.file_size
        ET.SubElement(el, "mimetype").text = "application/zip"
        ET.SubElement(el, "status").text = '0'
        ET.SubElement(el, "timecreated").text = get_time_stamp()
        ET.SubElement(el, "timemodified").text = get_time_stamp()
        ET.SubElement(el, "source").text = activity.activity_node.title + ".zip"
        ET.SubElement(el, "author").text = 'Petlja'
        ET.SubElement(el, "license").text = 'allrightsreserved'
        ET.SubElement(el, "sortorder").text = '0'
        ET.SubElement(el, "repositorytype").text = '$@NULL@$'
        ET.SubElement(el, "repositoryid").text = '$@NULL@$'
        ET.SubElement(el, "reference").text = '$@NULL@$'

        return el

    def _make_dummy_et_elements(self, activity):
        el = ET.Element("file", {"id": get_unused_id()})
        ET.SubElement(el, "contenthash").text = activity.sah1
        ET.SubElement(el, "contextid").text = activity.context_id
        ET.SubElement(el, "component").text = 'mod_scorm'
        ET.SubElement(el, "filearea").text = 'content'
        ET.SubElement(el, "itemid").text = '0'
        ET.SubElement(el, "filepath").text = '/'
        ET.SubElement(el, "filename").text = '.'
        ET.SubElement(el, "userid").text = '1'
        ET.SubElement(el, "filesize").text = '0'
        ET.SubElement(el, "mimetype").text = "$@NULL@$"
        ET.SubElement(el, "status").text = '0'
        ET.SubElement(el, "timecreated").text = get_time_stamp()
        ET.SubElement(el, "timemodified").text = get_time_stamp()
        ET.SubElement(el, "source").text = '$@NULL@$'
        ET.SubElement(el, "author").text = '$@NULL@$'
        ET.SubElement(el, "license").text = '$@NULL@$'
        ET.SubElement(el, "sortorder").text = '0'
        ET.SubElement(el, "repositorytype").text = '$@NULL@$'
        ET.SubElement(el, "repositoryid").text = '$@NULL@$'
        ET.SubElement(el, "reference").text = '$@NULL@$'

        return el

    def _make_file_et_element(self, file, activity):
        el = ET.Element("file", {"id": file.id})
        ET.SubElement(el, "contenthash").text = file.hash_file_name
        ET.SubElement(el, "contextid").text = activity.context_id
        ET.SubElement(el, "component").text = 'mod_scorm'
        ET.SubElement(el, "filearea").text = file.filearea
        ET.SubElement(el, "itemid").text = '0'
        ET.SubElement(el, "filepath").text = '/'
        ET.SubElement(el, "filename").text = os.path.basename(file.path)
        ET.SubElement(el, "userid").text = '$@NULL@$'
        ET.SubElement(el, "filesize").text = str(file.size)
        ET.SubElement(el, "mimetype").text = file.mime_type
        ET.SubElement(el, "status").text = '0'
        ET.SubElement(el, "timecreated").text = get_time_stamp()
        ET.SubElement(el, "timemodified").text = get_time_stamp()
        ET.SubElement(el, "source").text = '$@NULL@$'
        ET.SubElement(el, "author").text = '$@NULL@$'
        ET.SubElement(el, "license").text = '$@NULL@$'
        ET.SubElement(el, "sortorder").text = '0'
        ET.SubElement(el, "repositorytype").text = '$@NULL@$'
        ET.SubElement(el, "repositoryid").text = '$@NULL@$'
        ET.SubElement(el, "reference").text = '$@NULL@$'

        return el

    def _make_et_section_element(self, section):
        el = ET.Element("section")
        ET.SubElement(el, "sectionid").text = section.id
        ET.SubElement(el, "title").text = section.title
        ET.SubElement(
            el, "directory").text = section.section_dir_path.lstrip('/')

        return el

    def _make_activity_et_element(self, section, activity):
        el = ET.Element("activity")
        ET.SubElement(el, "moduleid").text = activity.module_id
        ET.SubElement(el, "sectionid").text = section.id
        ET.SubElement(el, "modulename").text = 'scorm'
        ET.SubElement(el, "title").text = activity.activity_node.title
        ET.SubElement(
            el, "directory").text = activity.activity_dir_path.lstrip('/')

        return el

    def _make_setting_et_element_section_included(self, section):
        el = ET.Element("setting")
        ET.SubElement(el, "level").text = 'section'
        ET.SubElement(el, "section").text = 'section_' + section.id
        ET.SubElement(el, "name").text = 'section_' + section.id + '_included'
        ET.SubElement(el, "value").text = '1'

        return el

    def _make_setting_et_element_section_userinfo(self, section):
        el = ET.Element("setting")
        ET.SubElement(el, "level").text = 'section'
        ET.SubElement(el, "section").text = 'section_' + section.id
        ET.SubElement(el, "name").text = 'section_' + section.id + '_userinfo'
        ET.SubElement(el, "value").text = '0'

        return el

    def _make_setting_et_element_activity_included(self, activity):
        el = ET.Element("setting")
        ET.SubElement(el, "level").text = 'activity'
        ET.SubElement(el, "activity").text = 'scorm_' + activity.module_id
        ET.SubElement(el, "name").text = 'scorm_' + \
            activity.module_id + '_included'
        ET.SubElement(el, "value").text = '1'

        return el

    def _make_setting_et_element_activity_userinfo(self, activity):
        el = ET.Element("setting")
        ET.SubElement(el, "level").text = 'activity'
        ET.SubElement(el, "activity").text = 'scorm_' + activity.module_id
        ET.SubElement(el, "name").text = 'scorm_' + \
            activity.module_id + '_userinfo'
        ET.SubElement(el, "value").text = '0'

        return el


class MoodleActivity:
    def __init__(self, activity_node, aggregationcoef2, sort_order, course_id):
        self.course_id = course_id
        self.context_id = get_unused_id()
        self.module_id = get_unused_id()
        self.id = get_unused_id()
        self.sort_order = sort_order
        self.activity_node = activity_node
        self.activity_dir_path = 'activities/scorm_' + str(self.module_id)
        self.time_stamp = get_time_stamp()
        self.aggregationcoef2 = aggregationcoef2
        self.grade_item_id = str(get_unused_id())
        self.file_ref_et_elem = []
        self.activity_files = []
        self.xml_data = {}

    def add_file(self, file):
        self.activity_files.append(file)

    def _make_file_inforef_element(self, id):
        el = ET.Element('file')
        ET.SubElement(el, 'id').text = id
        return el

    def extract_activity_data(self):
        self.xml_data = {
            'activity_gradebook': {
                "./grade_items/grade_item": {"id":  self.grade_item_id},
                "./grade_items/grade_item/categoryid": get_unused_id(),
                "./grade_items/grade_item/itemname": self.activity_node.title,
                "./grade_items/grade_item/iteminstance": str(self.sort_order - 1),
                "./grade_items/grade_item/aggregationcoef2": str(self.aggregationcoef2),
                "./grade_items/grade_item/sortorder": str(self.sort_order),
                "./grade_items/grade_item/timecreated": self.time_stamp,
                "./grade_items/grade_item/timemodified": self.time_stamp,
            },
            'module': {
                "attributes": {"id": self.module_id},
                "./sectionid":  str(self.section_id),
                "./sectionnumber": str(self.section_order),
                "./added": self.time_stamp,
            },
            "inforef": {
                "./fileref": [self._make_file_inforef_element(file.id) for file in self.activity_files],
                ".grade_itemref/grade_item/id": self.grade_item_id,
            },
            "activity": {
                "attributes": {"id": self.id, "moduleid": self.module_id, "contextid": self.context_id},
                "./scorm": {"id": self.id},
                "./scorm/name": self.activity_node.title,
                "./scorm/reference":  self.activity_node.title+".zip",
                "./scorm/sha1hash": self.sah1,
                "./scorm/revision": '1',
                "./scorm/launch": '1',
                "./scorm/timemodified": self.time_stamp,
                "./scorm/scoes/sco[1]": {"id": get_unused_id()},
                "./scorm/scoes/sco[1]/manifest": self.course_id,
                "./scorm/scoes/sco[2]": {"id": get_unused_id()},
                "./scorm/scoes/sco[2]/manifest": self.course_id,
                "./scorm/scoes/sco[2]/sco_datas/sco_data[1]": {"id": get_unused_id()},
                "./scorm/scoes/sco[2]/sco_datas/sco_data[2]": {"id": get_unused_id()},
                "./scorm/scoes/sco[3]": {"id": get_unused_id()},
                "./scorm/scoes/sco[3]/manifest": self.course_id,
                "./scorm/scoes/sco[3]/sco_datas/sco_data[1]": {"id": get_unused_id()},
                "./scorm/scoes/sco[3]/sco_datas/sco_data[2]": {"id": get_unused_id()},

            }
        }


class MoodleFile:
    def __init__(self, path, hash_file_name, mime_type, rel_path, file_size, filearea):
        self.path = path
        self.id = get_unused_id()
        self.hash_file_name = hash_file_name
        self.mime_type = mime_type
        self.rel_path = rel_path
        self.size = file_size
        self.filearea = filearea

