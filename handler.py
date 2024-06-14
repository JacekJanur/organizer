import shutil
import os

type_to_directory_name = {
    'text': 'Texts',
    'document': 'Documents',
    'spreadsheet': 'Spreadsheets',
    'other': 'Others',
    'runnable': 'Runnables',
    'video': 'Videos',
    'archive': 'Archives',
    'flashcard': 'Flashcards',
    'image': 'Images'
}

class FileHandlerDispatcher:
    def __init__(self):
        self.extension_to_handler = {
            'txt': 'text',
            'pdf': 'document',
            'doc': 'document',
            'docx': 'document',
            'xls': 'spreadsheet',
            'xlsx': 'spreadsheet',
            'xlsm': 'spreadsheet',
            'htm': 'document',
            'html': 'document',
            'dat': 'other',
            'tmp': 'other',
            'ini': 'other',
            'class': 'other',
            'lua': 'other',
            'gpx': 'other',
            'iso': 'other',
            'exe': 'runnable',
            'msi': 'runnable',
            'dmg': 'runnable',
            'apkg': 'other',
            'png': 'image',
            'jpg': 'image',
            'jpeg': 'image',
            'gif': 'image',
            'bmp': 'image',
            'mp4': 'video',
            'mov': 'video',
            'zip': 'archive',
            'rar': 'archive',
            '.apkg': 'flashcard'
        }

    def handle(self, file):
        src_path = f"../{file}"
        dest_path = self.get_dest_path(file)
        shutil.move(src_path, dest_path)

    def get_dest_path(self, file):
        file_extension = file.split('.')[-1]
        directory_name = type_to_directory_name.get(self.extension_to_handler.get(file_extension, 'other'), "Others")
        dest_path = f"../{directory_name}/{file}"
        
        self.create_dir_if_not_exist(directory_name)
        dest_path = self.rename_file_if_duplicated(file, directory_name, dest_path)
            
        return dest_path

    def create_dir_if_not_exist(self, directory_name):
        if not os.path.exists(f'../{directory_name}/'):
            os.mkdir(f'../{directory_name}')

    def rename_file_if_duplicated(self, file, directory_name, dest_path):
        while os.path.isfile(dest_path):
            new_file_name = file.split('.')[0] + '_.' + file.split('.')[1]
            dest_path = f"../{directory_name}/{new_file_name}"
        return dest_path