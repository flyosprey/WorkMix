import shutil
import os

from constants import TODO_SRC, DOWNLOAD_SRC


class GetEngFiles:
    def __init__(self):
        self.en_files = []
        self.all_download_files = os.listdir(DOWNLOAD_SRC)
        self.all_todo_files = None

    def move_files_todo_folder(self):
        if not self.all_download_files:
            return 0

        for file in self.all_download_files:
            if "~$" not in file and ".docx" in file:
                shutil.move(DOWNLOAD_SRC + file, TODO_SRC)

    def select_files(self):
        self.move_files_todo_folder()

        self.all_todo_files = os.listdir(TODO_SRC)

        if not self.all_todo_files:
            return 0

        for file in self.all_todo_files:
            if "~$" not in file and ".docx" in file:
                self.en_files.append(file)

        return self.en_files
