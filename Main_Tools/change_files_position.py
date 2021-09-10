import datetime
import shutil
import os
from constants import DOWNLOAD_SRC, BACKUP_SRC, COMPLETED_SRC, TODO_SRC


class ChangePosition:
    def __init__(self):
        self.all_files_completed = os.listdir(DOWNLOAD_SRC)
        self.all_files_todo = os.listdir(TODO_SRC)

    def backup_work_files(self):
        if not self.all_files_completed:
            return 0

        files_backup = []
        for file in self.all_files_completed:
            if "~$" not in file and ".docx" in file:
                files_backup.append(file)

        direct_name = datetime.datetime.now().strftime("%Y%m%d")
        all_backup_files = os.listdir(BACKUP_SRC)

        if direct_name not in all_backup_files:
            os.mkdir(BACKUP_SRC + direct_name)

        for file in files_backup:
            src = COMPLETED_SRC + file
            dst = BACKUP_SRC + direct_name
            shutil.move(src, dst)

    def remove_todo_files(self):
        if not self.all_files_todo:
            return 0

        files_remove = []
        for file in self.all_files_todo:
            if "~$" not in file and ".docx" in file:
                files_remove.append(file)

        for file in files_remove:
            remove_path = TODO_SRC + file
            os.remove(remove_path)
