"""
Author: Jacob Nino
Date: 3/1/22


"""

# Problem 1
# This program is to turn a string into morse code


morse_code ={ 'A': '.-',
              'B': ' -...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '....',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.--.',
              'Q': '--.-',
              'R': '.-.',
              'S': '...',
              'T': '-',
              'U': '..-',
              'V': '...-',
              'W': '.--',
              'X': '-..-',
              'Y': '-.-',
              'Z': '--..',

              '0': '-----',
              '1': '.----',
              '2': '..---',
              '3': '...--',
              '4': '....-',
              '5': '.....',
              '6': '-....',
              '7': '--...',
              '8': '---..',
              '9': '----.',

              ', ': '--..--',
              '. ': '.-.-.-',
              '? ': '..--..',}
              
              
def converter(user_message):
    cipher = ' '
    for ch in user_message:
            if ch != ' ':
                cipher += morse_code[ch] + ''
            else:
                cipher += ''
    return cipher


def decrypter(user_message):
    user_message += ' '

    decipher = ' '
    morse_text = ' '
    for ch in user_message:
        if ch != ' ':
            i =0
            morse_text += ch
        else:
            i+=1

            if i==2:
                decipher += ' '
            else:
                morse_text = ' '
    return decipher

def main():
    user_message = input('Enter a message')

    result=converter(user_message.upper())
    print(result)

    user_message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ..."
    result = decrypter(user_message)
    print(result)

if __name__ == '__main__':
    main()



# Problem 2
# This program is to search for vowels and consonats in string


def vowel_search(sentence,vowels):

    vowels = [each for each in sentence if each in "aeiouAEIOU"]

    print('There are', len(vowels))
    #print(vowels)
    return vowels



def consonant_search(sentence):

    consonant = [each for each in sentence if each not in "aeiouAEIOU"]
    print('Number of consonants in string', len(consonant))
    return consonant


sentence = input('Enter a string')
vowels='aeiou AEIOU'

# vowel funtion call
print(vowel_search(sentence,vowels))


# consonant function call
print(consonant_search(sentence))




# Problem 3 
# This program is to count all letters, digits and symbols
str1 = "P@#yn26at^&i5ve"

letters =0
num =0
symbols =0

for i in range(len(str1)):
    if(str1[i].isalpha()):
        letters = letters +1

    elif(str1[i].isdigit()):
        num = num+1

    else:
        symbols = symbols +1

print('The string has',letters ,'letters')
print('The string has',num,'numbers')
print('The string has',symbols,'special symbols')


# To remove specia symbols
str1 = "/*Jon is @developer & musician"
new_string = ""

for ch in str1:
    if(ch.isalnum()):
        new_string = new_string+ch
print('String without special characters',new_string)



# To remove - and replace with a space

str1 = "Emma-is-a-data-scientist"
new_string = str1.replace('-', ' ')

print('The string without -',new_string)



# To remove all consonants
str1 = "Hello ,have a good day"

vowel= 'aeiouAEIOOU'

list=[]

for i in range(len(str1)):
    k=0
    for j in range(len(vowel)):
        if(str1[i] == vowel[j]):
            k+=1
    if(k!=1):
       list.append(str1[i])

str1="".join(i for i in list)

print(str1)
        


# Problem 4
# This program is to make a list then find average and median
list = []
new_list=[]

n = int(input('How mny inputs do you want'))
while n > 100 or n <0:
     n=int (input('Enter a number from 0-100'))
        

for i in range(n):
    user_element= int(input('Enter a number'))
    list.append(user_element)

if list[i] >10:
    sum =0
    average=0

    for i in list:
        sum = sum+i

    average = sum/ len(list)
    print('The average is',average)


list.sort()

mid = len(list)//2
res = (list[mid] + list[~mid]) /2

print('The median is',str(res))


# Problem 5
# This program is to modify strings


str1 = "this is the string for the class"

string_list = list(str1.split())


# Capitaze every word
for i in range(len(string_list)):

    string_list[i] = string_list[i].capitalize()
fin = ' '.join(string_list)

print(fin)


# Removing spaces
for i in range(len(fin)):
    fin=fin.replace(' ', "")

print('Removing spaces',fin)


# To replace the letter s with a $
for i in range(len(fin)):

    fin=fin.replace('s', "$")
print('Replaceing the s' , fin)


# Convertion 4 
for i in range(len(fin)):
    fin = fin.replace('$', "s")
    fin = fin.replace('I' , "i")
print('Final covertion' ,fin)
        









            
    

