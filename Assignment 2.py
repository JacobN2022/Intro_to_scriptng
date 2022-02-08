"""
Author: Jacob Nino
Date: 2/08/2022

"""



# Problem 1
# This programs is to print out 2 different patterns


# 1st pattern
x=5

for i in range(1,x+1):
    for k in range(1, i+1):
        print("*", end=" ")
    print()

print(" ")


# 2nd pattern
y=5

for a in range(y):
    for b in range(1, y-a):
        print(" ", end=" ")
    for c in range(0, a+1):
        print("*", end=" ")
    print()

# Problem 2
# This program is to find the factorial number for two equations

n = int(input('Enter a number'))
r = int(input('Enter another number'))
n_counter =1
n_result =1

r_counter=1
r_result=1

s = n-r
s_counter=1
s_result=1

# To get 1st factorial number
while n_counter <= n:
    n_result = n_result*n_counter
    n_counter+=1
print('n factorial number is:',n_result)


# To get 2nd factorial number
while r_counter <= r:
    r_result = r_result*r_counter
    r_counter+=1
print('r factorial number is:',r_result)


# To get factorial number  for n-r
while s_counter <= s:
    s_result = s_result*s_counter
    s_counter+=1
print('n-r=',s_result)


total = n_result/(r_result*s_result)

print('The 1st total is:',total)


total_1=n_result/(s_result)
print('The final total is:',total_1)


# Problem 3
# This program is to sort a given list and display it


list = [20,68,41,88,16,40,65,97,85]

new_list =[]


for d in range(0,len(list)):
    for e in range(1+d,len(list)):
        if list[d] > list[e]:
            temp = list[d]
            list[d] = list[e]
            list[e] =temp

loop_counter =0
    
while loop_counter < len(list):
    if(list[loop_counter] != ""):
        new_list.append(list[loop_counter])
    loop_counter +=1
    
print('Here is the sorted new list')
print(new_list)

# Problem 4
# This program is to find the sum for a list, even list and odd list

sum =0
odd_sum =0
even_sum=0

odd_numbers = []
even_numbers = []

my_list1 = [1,2,3,4,5,6,7,8,9,10]

for num in range(0,len(my_list1)):
    sum = sum+my_list1[num]
    if my_list1[num] % 2==1:
        odd_numbers.append(my_list1[num])
    elif my_list1[num] %2==0:
        even_numbers.append(my_list1[num])

# To find Odd list sum
for odd in range(0,len(odd_numbers)):
    odd_sum = odd_sum+odd_numbers[odd]

# To find Even list sum
for even in range(0,len(even_numbers)):
    even_sum = even_sum+even_numbers[even]
       

print('The sum is:',sum)
print('Odd numbers list',odd_numbers)
print('Odd list sum:', odd_sum)
print('Even numbers list',even_numbers)
print('Even list sum:', even_sum)


# Problem 5

# This program is to display prime numbers between 2-50

prime_numbers_list =[]

min = 2
max = 50
temp = min

while temp in range(min,max+1):
    m=2

    is_prime = False
    if temp >1:
        is_prime = True

    while m <= int(temp/2):
        if temp% m ==0:
            is_prime=False
            break
        m +=1
    else:
        if is_prime:
            prime_numbers_list.append(temp)

            if not is_prime: print(temp)
    temp+=1
print('Here are your prime numbers')
print(prime_numbers_list)


# Problem 6


# 1st pattern

def print_patterns():
    
    x=5

for i in range(1,x+1):
    for k in range(1, i+1):
        print("*", end=" ")
    print()

print(" ")


# 2nd pattern
y=5

for a in range(y):
    for b in range(1, y-a):
        print(" ", end=" ")
    for c in range(0, a+1):
        print("*", end=" ")
    print()

# function call
print_patterns()    



# part 1
# Program to pass n and r as agruments

def n_factorial(n,r):
    
    n = int(input('Enter a number'))
    r = int(input('Enter another number'))


    n_counter =1
    n_result =1

    r_counter=1
    r_result=1

    s = n-r
    s_counter=1
    s_result=1
   
    while n_counter <= n:
        n_result = n_result*n_counter
        n_counter+=1
    print('First factorial number:',n_result)

    while r_counter <= r:
        r_result = r_result*r_counter
        r_counter+=1
    print('Second factorial number:',r_result)

    # To get factorial number  for n-r
    while s_counter <= s:
        s_result = s_result*s_counter
        s_counter+=1
    print('n-r=',s_result)


    total = n_result/(r_result*s_result)

    print('The 1st total is:',total)


    total_1=n_result/(s_result)
    print('The final total is:',total_1)

# function call
n_factorial("n","r")


#Part 2
# Program to pass list as agrument

list = [20,68,41,88,16,40,65,97,85]

def fun_list(list):

    new_list =[]

    for d in range(0,len(list)):
        for e in range(1+d,len(list)):
            if list[d] > list[e]:
                temp = list[d]
                list[d] = list[e]
                list[e] =temp

    loop_counter =0
    
    while loop_counter < len(list):
        if(list[loop_counter] != ""):
            new_list.append(list[loop_counter])
        loop_counter +=1
    
    print('Here is the sorted new list')
    print(new_list)

# function call
fun_list(list)

# Problem 7
# This program is to find if users number is an Armstrong number or not

num = input('Enter a number to check if its an Armstrong number')
total =0

temp = int(num)

while(temp>0):
    remainder = int(temp%10)
    temp=temp/10

    total = total+(remainder*remainder*remainder)

if(int(total) == int(num)):
    print('Your number ' + num + 'is an Armstrong number')
else:
    print('Your number ' + num + 'is not an Armstrong number')


# Problem 9
# This program is to print even numbers in range 1-10

loop_counter=1

while loop_counter <=10:

    if loop_counter%2==0:
        print(loop_counter)

    loop_counter+=1



    



    









