import os

class FolderOpener:
    # Класс определяющий все нужные пути
    def __init__(self):
        self.currentPath = os.getcwd() # Путь до директории выполнения программы
        self.pathToSourceFolder = os.path.join(self.currentPath,'raw') # Путь до папки raw
        self.pathToTargetFolder = os.path.join(self.currentPath,'loaded') # Путь до папки loaded
        self.isExistSourceFolder = os.path.exists(self.pathToSourceFolder) # Проверка на существование папки raw
        self.isExistTargetFolder = os.path.exists(self.pathToTargetFolder) # Проверка на существование папки loaded
        if not self.isExistSourceFolder: print("Директории 'raw' не существует!")

