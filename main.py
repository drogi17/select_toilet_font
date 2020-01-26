import os
directory = 'figlet-fonts-master/'
files = os.listdir(directory)
# flf_files = filter(lambda x: x.endswith('.flf'), files)
string = input('Введите строку: ')
os.system('echo > text.txt')
for f in files:
    os.system('echo ' + f + " >> text.txt;toilet -f '"+ directory + f + "' " + string + " >> text.txt; echo >> text.txt")