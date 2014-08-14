#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import urllib, re, HTMLParser
 
def abc(a, b, c):
	per = 100.0 * a * b / c
	if per > 100:
		per = 100
	print "%.2f%%" % per

# d = pq(url="http://book.douban.com/tag/小说?icn=index-sorttags-hot")
d = pq(filename="./douban.html")
booklist = d('span').filter('.rating_nums').filter(lambda i: float(pq(this).text()) >= 9.0).parents('li')('span') \
    .filter('.pl').filter(lambda i: int(pq(this).text()[1:-4]) >= 10000).parents('li')('h2')
# print booklist
match_url = re.compile(r'(?<=href=["]).*?(?=["])')
match_title = re.compile(r'(?<=title=["]).*?(?=["])')
raw_url = re.findall(match_url, str(booklist))
raw_title = re.findall(match_title, str(booklist))
print raw_title

html_parser = HTMLParser.HTMLParser()
book_dict = {}
print range(len(raw_title))
for i in range(len(raw_title)):
    title = html_parser.unescape(raw_title[i])
    print raw_url[i], title
    book_dict[raw_url[i]] = title
print book_dict

for key in book_dict:
    print "Downloading %s.html:" % book_dict[key]
    (filename, headers) = urllib.urlretrieve(key, "./douban/" + book_dict[key] + ".html", abc)
