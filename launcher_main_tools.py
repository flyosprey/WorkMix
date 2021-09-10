from Main_Tools.get_eng_files import GetEngFiles
from Main_Tools.edit_file import EditFile
from Main_Tools.change_files_position import ChangePosition


def main_edit_file():
    get_eng = GetEngFiles()
    eng_files = get_eng.select_files()

    if eng_files == 0:
        print("There are no TODO files")

    else:
        for file in eng_files:
            manage = EditFile(file)
            manage.get_content_en_file()
            manage.translate_en_ru()
            manage.put_translated_file()


def main_change_position():
    ed = ChangePosition()
    ed.backup_work_files()
    ed.remove_todo_files()
