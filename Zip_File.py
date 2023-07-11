

f = open('File1.txt', 'w+')
f.write('Hello all, it is time to start new phase')
f.close()

q = open('File2.txt', 'w+')
q.write('Hello all, i completed my old version. I want to update new version')
q.close()

import zipfile
print('Zip File')

zip_files = zipfile.ZipFile('Filezip.zip', 'w')
zip_files.write('File1.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_files.write('File2.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_files.close()

print('Zip file completed')
unzip_files = zipfile.ZipFile('Filezip.zip', 'r')
unzip_files.extractall('Files')
print('Unzip_files')