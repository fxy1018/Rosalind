#!/usr/bin/env python
from Bio import Entrez
from Bio import SeqIO
#######open file
with open("rosalind.txt", "r") as file:
	data = file.read()
	ls = data.split(" ")
	Entrez.email = "xueyi.fan27@gmail.com"
	handle = Entrez.efetch(db="nucleotide", id=ls, rettype="fasta")
	records = list (SeqIO.parse(handle, "fasta")) 
	length_list = []
	min_index = 0
	count = 0
	mi = len(records[0].seq)
	for record in records:
		if (len(record.seq)<mi):
			mi = len(record.seq)
			min_index = count
			count +=1
		else:
			count +=1
	print(records[min_index].description)


#sorted_records = sorted(records, key=len)