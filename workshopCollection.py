#NMACERI - Workshop Collection parser 
# Converts a workshop colleciton ID to lua format for GMOD server

import requests
from bs4 import BeautifulSoup

#Compile URL from given ID
collection_id = input("Please enter Steam Workshop collection ID (Must be unlisted or public!)\n")
url = 'https://steamcommunity.com/sharedfiles/filedetails/?id='
url = url + collection_id
print('Given URL: ' + url)

#Grab raw HTML
html_text = requests.get(url)
soup = BeautifulSoup(html_text.content, "html.parser")

#Pull all workshop IDs with coresponding names
workshop_ids = soup.find_all("div", class_="collectionItem")
workshop_names = soup.find_all("div", class_="workshopItemTitle")

if not workshop_ids or not workshop_names:
	print("ID is not valid! (Not public or bad ID)")
	exit(0)

#Write LUA file
luaFile = open("workshop.lua", "w")
luaFile.write("-- LUA FILE AUTOMATICALLY GENERATED USING CLONES SCRIPT\n")
for unique_idstr,unique_name in zip(workshop_ids,workshop_names):
	unique_id = unique_idstr.get('id')[11:]
	print('Found workshop item: '+ unique_name.get_text() + ' with ID: ' + unique_id)
	luaFile.write("resource.AddWorkshop(" + unique_id + ")\n")
luaFile.close()
print("Finished writing LUA file, thanks for using this script!")