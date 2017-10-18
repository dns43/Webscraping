 
#author: dns43
#this script walks threw a specified directory 
#and extracts all .zip files to their parent directory

import zipfile
import os
 
folderlist = []
filelist = []

path = "C:\\Users\\dns43\\Desktop\\Drexel\\webscraper\\data" 

#dns43: recursively walks through folders and creates a list of .zip files
#dns43: expects all files to be zipfiles! does not handle exceptions!
def collectZipFiles(pfad):
	for entry in os.scandir(pfad):
		print(entry.path)
		if entry.is_dir():
			folderlist.append(entry.path)
			collectZipFiles(entry.path)
		elif entry.is_file():
			filelist.append(entry.path)

collectZipFiles(path)

#dns43: some verbose debug information
print('Folders:')
print(len(folderlist))

print('Files:')
print(len(filelist))

#dns43: extracts all files in the list to their current directory
#dns43: expects all files to be zipfiles! does not handle exceptions!
i=0
for file in filelist:
	print(file)
	print(file[:-3])
	zip_ref = zipfile.ZipFile(file, 'r')
	zip_ref.extractall(file[:-3])
	zip_ref.close()
	i=i+1
