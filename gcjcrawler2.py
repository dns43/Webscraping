#author: dns43
#walks the google codejam data on go-hero.net
#downloads all submited JavaScript files int
#<country>/<author>/<filename>.zip

from bs4 import BeautifulSoup
import lxml
import lxml.html
import requests
import csv
from urllib.request import urlopen
import os
#for in
#if in
#if
#arrays
#string handling
#dictionary
#typecasting



#dns43: Goto JavaScript overview page
url = "https://www.go-hero.net/jam/17/"
subset = "languages/JavaScript"
r = requests.get(url+subset)
site = BeautifulSoup(r.content, "lxml")
#dns43: Get all Hyperlinks
hyperlinks = site.find_all("a")

regionallinks = []
regionaldict = {} #dict Key: REGION, value: NAME <<-- dns43: this will hold all JavaScript coders by country 
#c=0
#dns43: Save  Hyperlinks for Regions that have more than 6 Contestants
for link in hyperlinks:
	if "./regions/" in link["href"]:
		if int(link.nextSibling.split()[0][1:]) > 6:
			regionallinks.append(url+link["href"][2:])
			print("dict:"+link["href"][10:])
			regionaldict[link["href"][10:]] = "";

print("#############")
print("Countries >6 contestants:")
print(regionaldict)
print("#############")

##########

regionalNames = []
for country in regionallinks:
	r = requests.get(country)
	site = BeautifulSoup(r.content, "lxml")
	hyperlinks = site.find_all("a")
	names =[]
	for link in hyperlinks:
		if "./name/" in link["href"]:
			names.append(link.text)

	page = 1	
	while len(names)%100 == 0:
		r = requests.get(country+"/partial/"+str(page))
		site = BeautifulSoup(r.content, "lxml")
		hyperlinks = site.find_all("a")
		for link in hyperlinks:
			if "./name/" in link["href"]:
				names.append(link.text)
		page=page+1
	print("#############")
	print(country+":\n"+ str(len(names))+" contestants")
	regionaldict[country[39:]] = names
	print(country[39:]+ ": "+ str(len(regionaldict[country[39:]])))


#########

languageNames = []
#dns43: Back to JavaScript Overview page
r = requests.get("https://www.go-hero.net/jam/17/languages/JavaScript")
site = BeautifulSoup(r.content, "lxml")
hyperlinks = site.find_all("a")

#####
#dns43: cannot find error - hardcoded instead xD
#dns43: TODO: make this run and comment out lines 100-122
#page = 2	
#while len(languageNames)%100 == 0:
#	print(url+subset+"/partial/"+str(page))
#	r = requests.get(url+subset+"partial/"+str(page))
#	site = BeautifulSoup(r.content, "lxml")
#	hyperlinks = site.find_all("a")
#	print("Hyperlinks:"+str(len(hyperlinks)))
#	print(hyperlinks)
#	for link in hyperlinks:
#		if "./name/" in link["href"]:
#			languageNames.append(link.text)
#	print(len(languageNames))
#	page=page+1
#####

#dns43: get all names
for link in hyperlinks:
	if "./name/" in link["href"]:
		languageNames.append(link.text)
print("nach erster: "+str(len(languageNames)))
#dns43: get all names from 2nd page
print(len(languageNames))
r = requests.get("https://www.go-hero.net/jam/17/languages/JavaScript/partial/1")
site = BeautifulSoup(r.content, "lxml")
hyperlinks = site.find_all("a")
for link in hyperlinks:
	if "./name/" in link["href"]:
		languageNames.append(link.text)
print("nach zweiter: "+str(len(languageNames)))
#dns43: get all names from 3rd page
r = requests.get("https://www.go-hero.net/jam/17/languages/JavaScript/partial/2")
site = BeautifulSoup(r.content, "lxml")
hyperlinks = site.find_all("a")
for link in hyperlinks:
	if "./name/" in link["href"]:
		languageNames.append(link.text)
print("nach dritter: "+str(len(languageNames)))


print("#############")
print("JS Dev names:"+str(len(languageNames)))

##########
#dns43: compare if name occurs in COUNTRY and LANGUAGE 
#dns43: goto contestants page and download all his JS files
print("#############")
print("JS Contestants from Countries > 6 JS Developers")
i=0
for name in languageNames:
	#print("debug name: "+ name)
	for index in regionaldict:
		for entry in regionaldict[index]:
			#print("debug entry: "+ entry)
			if name == entry:
				#print(str(i)+" "+ index +": "+ name)
				#goes like "150 UnitedStates: Thomas"
				r = requests.get("https://www.go-hero.net/jam/17/name/"+name)
				site = BeautifulSoup(r.content, "lxml")
				hyperlinks = site.find_all("a")
				for link in hyperlinks:
					print("link: ")
					print(link)
					print("linktext: "+link.text)
					if "JavaScript" in link.text:
						if "google" in link["href"]:
							res = urlopen(link["href"])
							header = res.info()    
							if 'Content-Disposition' in str( header ):
								# It is a file
								test = res.read()
								print("check!")
								filename = res.info()['Content-Disposition'] . split( '=' )[-1] . strip( '"' )
								#filename = unquote(filename)
								if not os.path.exists("./data/"+index):
									os.makedirs("./data/"+index)
								with open("./data/"+index+"/"+filename, "wb" ) as code :
									code.write(test)
								i=i+1
print("#############")

