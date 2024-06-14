from os import listdir
from os.path import isfile, join

from handler import FileHandlerDispatcher

file_handler = FileHandlerDispatcher()

for f in listdir('..'):
    if isfile(join('..', f)):
        file_handler.handle(f)