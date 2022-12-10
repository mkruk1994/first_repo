import os
import time

# print(os.getcwd()) #wyswietlenie obecnej lokalizacji #
# os.chdir('C:\\Users\\vdi-student\\Desktop')
# print(os.getcwd())
# os.mkdir('new_folder') # tworzenie nowego foldera
# time.sleep(5)
# os.rename('new_folder', 'new_folder2') # zmiana nazwy
# time.sleep(5)
# os.rmdir('new_folder2')
#os.system('cmd /c "cd C:\\Users\\vdi-student\\Desktop && dir /s new.txt >> result.txt"')
#os.system('cmd c "dir /s new.txt >> result.txt"')

my_string1 = 'mom'
my_string2 = 'dad'
sum1 = my_string1 + my_string2
print(sum1)
sum2 = 'my ' + my_string1 + ' and my ' + my_string2
print(sum2)
print(sum2[3:6])
print(sum2[-4:-1])