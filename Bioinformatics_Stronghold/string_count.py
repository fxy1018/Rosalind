#!/usr/bin/perl


string = "AGAGCAGTGGTGAGGCACCTTTTAATGTACACGTAGGGTGGCTTCTTCTTAACTCGGAGGAATTGAGGACATCGCTCCATCATTGTGAAACCTCGAAAATCTGTCCACTTACTTATACAGGGCGAAGGACGATGGTATATCATGTGCCCAGGTTATGGTCGACCACGCGCGTAGGGTTTTACCAGGTTTAGGTGGATCGGACTAGGGAGACCTTAAATACAAACATCTTTGGTTATGTGACTTGCATGTGTGTCTCGTATGCTCGAAAAAGGCCTACTGTTAACTGTGATGGCTGATTCTTATACTAACCGCGGACTGCGGAGGCGTGTAAGGGTTGGGACCTTTAGTGTCAGTGTACTGATGTAGACGTTGGGCGTATCCGTCTTACGTTCGCGACGAAATCAGTCAGTTCTCCTCGAATGGGTTTCGCATTGCGCGAGACCCGGGAGCCAGGTGTATTGCGATAGGCCAGAGCTTTAAGGCCAACACGAGTCCAGGTTGCGCAAGGCTAATCTCCACAGCTGACAGTAGAGAAAGCGTCACGCGTACATCCATGCGTTAAGCCCAGCAATTTGAACAAGGCCCTACCAAAATGTCACTACTTCAAGAAATTACGTTTGGATTCCTCGCACGAACAATAGACTTCCTTAAGCAATACGTGCGAAGTACACCGACGGTAATGCCTCCGGTCACGTTCATACATAGGCCTAAGAGTCTGGCCGAACCACCCTTTTCCAGGGGTTTTTAGAGCCGAATGTCCGCGATACGCTCCTATTCGTACGCCTTTGGGCCTAGATGTCGGGAATGTGTCTGTAAAGCAATGGGCTGTAAGTACCAGCGATCGCTCGTTTGTCCCGGTGAGGCGGTGGGAAACCCAATCGGAGTCATCTCTTGAGTCTTGA"
dic = {'A':0,'T':0,'C':0,'G':0}
for letter in string:
   # print letter
   dic[letter]+= 1;
print dic['A'],dic['C'],dic['G'],dic['T']

        



