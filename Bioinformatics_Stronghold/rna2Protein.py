#!/usr/bin/python


#f1 = open ('rosalind_prot.txt','r')
#rna = f1.read()
rna = "AUGUCGGGGUGCACUAAAAAUUAUACACUGUAUCGACAGCGGGGAAAAGCCUUCUACCGUUACGCUACGCUACACUGCGCCGCACAACGGACACACUUAUUGUUUAGGGUGGGCGGUGCCAGGUCAAGGCGAAAUGCGGCACGGCUCGGAGUAUGUCGGGUUUCUAGAUGUUCCAGGUCCCCGCCGCACACUUUGUACAGUGGCGACGUGCUAAGUCAGCACGCAUCUGUCCAAGACGAGCAUCUGCAGAGAGCGAGGGUAGCCGGACCGCUCGGCGGGGCUUCCGGCACCCUACAAUUAUACGCGUCCCAAUUAGGCAGAGGAUCUGUUGGACAGGACAUUUAUUGCACAGGGCUUGCUCCAAGACCCUCAUUUACCGGAAUUCCUGCCAAGUCGAGGGAUGCAUUCACGUCGGAAGGCUUCUUGAUAGCCAGGCCCAAAGUUUGCAUGCGAAGUAUGCAGAUCCCUCAAGUGUUGCCUCUCCUUACACUAUAUAAUUGCACGAAAUCUCAGUUGGUGAAGACUGUUUGGCCCAAAUUGGCUGGGACGGGCUUGGGAUGA"


coden_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
'UUC': 'F', 'CUC':'L', 'AUC': 'I', 'GUC': 'V',
'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA':'V',
'UUG': 'L',      'CUG': 'L',      'AUG': 'M', 'GUG': 'V',
'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
'UGC': 'C',      'CGC':'R',      'AGC': 'S',      'GGC': 'G',
'UGA': 'Stop',  'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G' }

#print coden_table['UGG']

n = int(len(rna)/3)
protein = ''
for i in range(n):
    coden = rna[(3*i):(3*i+3)]
    if coden_table[coden]=="Stop":
        next
    else: 
        protein = protein + coden_table[coden]
print(protein)



