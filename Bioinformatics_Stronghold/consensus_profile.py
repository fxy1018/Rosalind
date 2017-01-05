#!/use/bin/python

f_in = open('rosalind_cons.txt','r')
input_list = f_in.read().split(">")[1:]
bp_max = []
line_matrix = []
count_a,count_b,count_c,count_d = 0,0,0,0



for block in input_list:
    print block
    line_arr = block.split('\n')
    line = ''
    for i in range(1,len(line_arr)):
        line = line+line_arr[i]
    line_matrix.append(line)
    
for i in range(len(line_matrix[1])):
    string = ''
    count = []
    for j in range(len(line_matrix)):
        string = string + line_matrix[j][i]
    count.append(string.count('A'))
    count.append(string.count('C'))
    count.append(string.count('G'))
    count.append(string.count('T'))
    bp_max.append(count)



def print_result(ba_max):
    concerive_str = ''
    for i in ba_max:
        index = i.index(max(i))
        if index == 0:
            concerive_str = concerive_str + 'A'
        elif index == 1:
            concerive_str = concerive_str + 'C'
        elif index == 2:
            concerive_str = concerive_str + 'G'
        elif index == 3:
            concerive_str = concerive_str + 'T'
    print concerive_str
    
    for j in range(len(ba_max[1])):
        if j==0:
            string = 'A:'
        elif j==1:
            string = 'C:'
        elif j==2:
            string = 'G:'
        elif j==3:
            string = 'T:'
        for z in range(len(ba_max)):
            string = string + ' ' + str(ba_max[z][j])
        print string 



print_result(bp_max)
