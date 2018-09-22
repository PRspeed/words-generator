

file1 = open('fgen.txt', 'r')
file2 = open('slovar.txt', 'r')
same = set(file1).intersection(file2)

same.discard('/n')

with open('output.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)