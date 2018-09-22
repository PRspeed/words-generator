#-*- coding: utf-8 -*-
###################################### import ##########################################
import itertools

##################################### function #########################################

def words_generator(mystr:str, b=7):
    """ Составляет любые комбинации слов из букв, переданных как строка без пробелов.
    Вторым параметром передается  количество букв в генерируемых словах.

    """

    with open("generate.txt", mode="a") as my_generate:
        tuple_generate = (''.join(i) for i in itertools.permutations(mystr, b))
        for line in tuple_generate:
            my_generate.write(line + '\n')


def words_compare(gen='generate.txt', slovar='slovar.txt'):
    """ Принимает два файла - сгенерированные слова и базовый словарь.
    При совпадении слов из одного файла с другим записывает список данных слов
     в текстовый документ 'output.txt'

    """
    file1 = open(gen, mode='r')
    file2 = open(slovar, mode='r')
    same = set(file1).intersection(file2)
    same.discard('/n')
    with open('myoutput.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)

    file1.close()
    file2.close()

###################################### main ##########################################


if __name__ == "__main__":

    mystr = 'рпоёлтщвовапь'

    words_generator(mystr, 5)
    words_compare()

