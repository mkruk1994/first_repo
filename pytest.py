import os
import time

# print(os.getcwd()) #wyswietlenie obecnej lokalizacji #
#os.chdir('C:\\Users\\vdi-student\\Desktop')
print(os.getcwd())
os.mkdir('new_folder') # tworzenie nowego foldera
time.sleep(5)
os.rename('new_folder', 'new_folder2') # zmiana nazwy
time.sleep(5)
os.rmdir('new_folder2')