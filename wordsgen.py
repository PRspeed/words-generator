#-*- coding: utf-8 -*-

import itertools



mystr = 'рпоёлтщвовапь'

listgen = [''.join(i) for i in itertools.permutations(mystr, 5)]

myfile = open('fgen.txt', mode='w')
for i in listgen:
    myfile.write(i + '\n')

myfile.close()




