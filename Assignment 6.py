'''
Author: Jacob Nino
Date: 3/08/22
'''


# Problem 2
# This program is to create a file from 3 other files with functions

def file_reader():
    f = open('f1.txt', 'r')
    contents = f.read()
    file_writer(contents)
    f.close()

    f = open('f2.txt', 'r')
    contents = f.read()
    file_writer(contents)
    f.close()


    f = open('f3.txt', 'r')
    contents = f.read()
    f.close()
    

    file_writer(contents)


def file_writer(c):
    f = open('fn.txt','a')
    f.write(c)
    f.close()
    
file_reader()

f = open('fn.txt','r')
contents = f.read()
print(contents)
f.close()

