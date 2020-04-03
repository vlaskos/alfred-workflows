#!/usr/bin/python
from lxml import html
import requests
import json
import sys, os

#query = sys.argv[1]
#query = 'https://songwhip.com/https://open.spotify.com/track/6jKVU3e0gnQLj3iifJBvVN?si=XFo4C4ghRbmOuUIfvWEDvQ'
#page = requests.get(query)
#tree = html.fromstring(page.content)

with open('demo.html', 'r') as myfile:
    query = myfile.read()

tree = html.fromstring(query)

title = tree.xpath('/html/head/title/text()')[0]

data = {}

data = { 
	"items": []
}

mods = {
	"cmd": {
		"subtitle": "Copy link to clipboard"
	},
	"alt": {
		"subtitle": ""	
	}
}

mods["alt"]["subtitle"] = "demo.html"
data["items"].append({"uid": "00songwhip", "title": "SongWhip", "subtitle": title, "arg": "songwhip url", "mods": mods}) #query})


items = tree.xpath('//a[@role="button"]')
i = 0
for item in items:
	i = i + 1
	title = item.text
	url = item.get("href")
	file_icon = "icon.png"
	if os.path.isfile(title + ".png"): 
		file_icon = title + ".png"
	mods["alt"]["subtitle"] = url
	data["items"].append({"uid": str(i).rjust(2,"0") + title, "title": title, "subtitle": title,  "arg": url, "icon": {"path": file_icon}, "mods": mods})
	print url
	print mods

#sys.stdout.write(json.dumps(data))