#author: dns43
#this script walks threw a specified directory 
#and makes all filenames unique
#by adding a number to the end of the filename
#each number is added to 1 .ast, 1 .js, and 1 .txt file before it is increased
#this circumvents multiply defined instace names,
#when applying the codestylometry project to the dataset
import zipfile
import os
 
folderlist = []
filelist = []
path = "C:\\Users\\dns43\\Desktop\\Drexel\\webscraper\\testset" 

#dns43: recursively walks through folders and creates a list of .zip files

def collectFiles(pfad):
	for entry in os.scandir(pfad):
		#print(entry.path)
		if entry.is_dir():
			folderlist.append(entry.path)
			collectFiles(entry.path)
		elif entry.is_file():
			filelist.append(entry.path)

collectFiles(path)

#dns43: some verbose debug information
print('Folders:')
print(len(folderlist))

print('Files:')
print(len(filelist))

#dns43: i is used as an index
i=0

#dns43: c is the counter, eventually attached to the filename
c=0
for file in filelist:
#dns43: kind of a switch case construct
#dns43: to make sure filenames stay in relation to each other
#dsn43: otherwise you would have "main1.js, main2.ast, main3.txt"
	if ".js" in file:
		t=file[:-3]+str(i)+file[-3:]
		os.rename(file, t.replace(" ", ""))
		print(t.replace(" ", ""))
		c=c+1
		if c%3 == 0:
			i=i+1
	if ".ast" in file:
		t=file[:-4]+str(i)+file[-4:]
		os.rename(file, t.replace(" ", ""))
		print(t.replace(" ", ""))
		c=c+1
		if c%3 == 0:
			i=i+1

	if ".txt" in file:
		t=file[:-4]+str(i)+file[-4:]
		os.rename(file, t.replace(" ", ""))
		print(t.replace(" ", ""))
		c=c+1
		if c%3 == 0:
			i=i+1