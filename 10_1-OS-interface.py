import os
import shutil
print(os.getcwd())
# os.chdir() # змінити каталог
# os.system('mkdir today') # створення нового каталогу

dir(os) # list available attributes and methods
help(os) # documentation os

shutil.copyfile("work.txt", "workfile.txt") # копіює вміст файлу work.txt в workfile.txt

# shutil.move('old_folder', 'new_lokation') # переміщає файл або папку