#!/usr/local/bin/python3

import requests
from bs4 import BeautifulSoup

url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
content = requests.get(url, headers={
	'authority': 'seekingalpha.com',
	'method': 'GET',
	'path': '/earnings/earnings-call-transcripts',
	'scheme': 'https',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
})

soup = BeautifulSoup(content.text, 'html5lib')
anchors = soup.select('#analysis-list-container ul li a')
for anchor in anchors:
	print(anchor['href'])
