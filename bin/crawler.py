#! /usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import urllib

import chardet

from bs4 import BeautifulSoup

def webEncode(web):
	return chardet.detect(web)["encoding"]

def crawlWeb(url):
	web = ""
	web_fd = urllib.urlopen(url)
	if web_fd:
		web = web_fd.read()
	web_fd.close()

	return web

def getFeed(web):
	page = hp()
	hp.feed(web)

	hp.close()

def main(file_path):
	#print main.__name__
	fd=open(file_path, "r")
	while 1:
		url = fd.readline()
		if len(url) > 0:
			# 判断是否是url
			# todo...
			web = crawlWeb(url)
			#encoding = webEncode(web)
			#soup =  BeautifulSoup(web.decode(encoding, 'ignore'), "html.parser")
			soup =  BeautifulSoup(web, "html.parser")
			print(soup.find_all('a'))
		else:
			break 

if __name__ == '__main__':
	local_pwd = os.getcwd()
	file_path = local_pwd + "/../conf/webdir.conf"
	main(file_path)
