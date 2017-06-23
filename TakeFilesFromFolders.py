import os
import string
import shutil

class TakeFilesFromFolders:
    # Класс выполняющий копирование файлов
    def __init__(self, path):
        self.pathToFolder = path
        self.treeOfFolders = os.walk(self.pathToFolder) # Определение путей до директорий, вложенных директорий и файлов в них
    def loadFilesToFolder(self, isExistTargetFolder, pathToTargetFolder):
        if (not isExistTargetFolder):
            os.mkdir(pathToTargetFolder) # Создание директории loaded
            print('Создана директория loaded')
        for element in self.treeOfFolders:
            fullNameOfDir = os.path.split(element[0]) # Парсинг пути на путь до директории с файлами и на имя директории
            directoryNameArr = fullNameOfDir[-1].split('_') # Парсинг имени директории на directoryname и date
            if directoryNameArr[0] != 'raw': # Выполнить загрузку для всех директорий кроме raw
                yearOfFile = directoryNameArr[2] # Определение date
                if all(map(lambda x: x in string.ascii_letters, str(directoryNameArr[0]))): # Определение кириллицы
                    for files in element[2]:
                        targetFileName = '{0}_{1}_{2}'.format(directoryNameArr[0],yearOfFile,files) # Имя нового файла
                        sourcePathToFile = os.path.join(element[0],files) # Путь откуда копировать
                        targetPathToFile = os.path.join(pathToTargetFolder,targetFileName) # Путь куда копировать
                        if os.path.exists(targetPathToFile): # Если файл уже существует
                            print('Файл {} уже существует, операция копирования не будет выполнена!'.format(targetFileName))
                        else: # Копирование файла
                            shutil.copyfile(sourcePathToFile,targetPathToFile)
                            print('Скопирован файл {0} из директории {1}'.format(files, fullNameOfDir[0]))
        print('Операция выполнена!')


