#!/usr/bin/env python

import urllib2
import re


#line = "DR   GO; GO:0045177; C:apical part of cell; IDA:RGD."
#is_go = re.search(r"GO:[0-9]*?;\s[A-Z]\:(.*?;)", line).group(1)
#print(is_go)

for line in urllib2.urlopen("http://www.uniprot.org/uniprot/Q9UH73.txt"):
	if re.search(r"GO\:[0-9]*?\;\s[A-Z]\:(.*?)\;", line)==None:
		continue
	else:
		print(re.search(r"GO\:[0-9]*?\;\s[A-Z]\:(.*?)\;", line).group(1))

 