#!/usr/local/bin/python3

#import httplib 
import requests
from bs4 import BeautifulSoup
# try:
# 	from urllib.request import Request, urlopen  # Python 3
# 	from urllib.error import HTTPError
# except:
#     from urllib2 import Request, urlopen  # Python 2

#httplib.client.HTTPConnection.debuglevel = 1
#http.client.HTTPConnection.set_debuglevel(1)

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
print(anchors[0]['href'])

# req = Request(
# 	url, 
# 	method='GET',
# 	headers={
# 		'authority': 'seekingalpha.com',
# 		'method': 'GET',
# 		'path': '/earnings/earnings-call-transcripts',
# 		'scheme': 'https',
# 		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
# 	}
# )

#req.method = 'GET'
# req.add_header('authority', 'seekingalpha.com')
# req.add_header('method', 'GET')
# req.add_header('path', '/earnings/earnings-call-transcripts')
# req.add_header('scheme' , 'https')
# req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

# print(req.has_header('Path'))
# print(req.header_items())
# try:
# 	content = urlopen(req).info() #read()
# 	print(content)
# except HTTPError as err:
# 	print(err)

