import os

f = open('normal_text.txt', 'w')
f.write('practice test for prepare the code')
f.close()

print(os.listdir('D:\\B.TECH NOTES'))


print("Current directory: ",os.getcwd())

import shutil
#print(shutil.move('normal_text.txt','D:\\pythonProject\\PythonUdemy'))

os.rm