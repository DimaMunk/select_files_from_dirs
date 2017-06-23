from FolderOpener import FolderOpener
from TakeFilesFromFolders import TakeFilesFromFolders


folder = FolderOpener() # Создание объекта с путями
takeFiles = TakeFilesFromFolders(folder.pathToSourceFolder) # Создание объекта для копирования
takeFiles.loadFilesToFolder(folder.isExistTargetFolder,folder.pathToTargetFolder) # Копирование файлов



