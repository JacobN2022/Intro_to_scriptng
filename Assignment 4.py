# Problem1
# This program is to add,chagne, and delete items in a dictionary


employees = {'name1': 'Susan','number1':'47899','dept1': 'Accounting','Job1':'Vice President',
             'name2': 'Mark','number2':'39119','dept2': 'IT','Job2':'Programmer',
             'name3': 'Joy','number3':'81774','dept3': 'Manufacturing','Job3':'Engineer'}
              


menu_choices = {
    1: 'Option 1 to look up employee',
    2: 'Option 2 to add new employee',
    3: 'Option 3 to change existing employee',
    4: 'Option 4 to delete employee',
    5: 'Quit',
    }


def print_menu():
    for key in menu_choices.keys():
        print(key, '--', menu_choices[key])

# To look up employee
def choice1():
    if employees['number1'] == '47899':
        print(employees['name1'])

# To add new exmployee
def choice2():
    
    new_employee = input('Enter employees name')
    number = input('Enter employees number')
    dept = input('Enter depatment')
    job = input("Enter employees job title")

    employees[new_employee] = number
    employees[dept] = job

    print(employees)



# To change an existing employee's info
def choice3():
    employees['name1'] = 'Jake'
    print('Change an employee',employees)



# To delete an employee
def choice4():
        employees.pop('name3')
        print('Deleting employee',employees)



# Menu
while(True):
    print_menu()
    choice = int(input('Enter your choice:'))

    if choice ==1:
        choice1()
    elif choice==2:
        choice2()
    elif choice==3:
        choice3()
    elif choice==4:
        choice4()
    elif choice==5:
        print('Program will quit now')
        exit()





# Problem 2
# This program is to find lowest,highest,total and average of a list

list=[]

counter=0
print('Please enter 20 numbers:')
for i in range(0,5):
    e = int(input("Enter a number:"))
    counter+=1

    list.append(e)

print(list)

# To find the smallest number
small = list[0] if list else None

for i in list:
    if i<small:
        small=i

print("The smallest number is: ", small)


# To find the highest number
high = list[0] if list else None

for i in list:
    if i>high:
        high=i

print('The highest number is: ', high)

# To find the total number

total=0
for i in list:
    total += i

print ('The total is:',total)

# To find the average

average=total/counter


print('The average is:',int(average))



# Problem 3

n=int(input('Enter a number:'))
dit={x:x*x for x in range(1,n+1)}

print(dit)




# Problem 4
# This program is to find second largest number and remove repeating elements in random list

import random
r_list =[]
new_list=[]

for i in range(0,100):
    num = random.randint(1,20)
    r_list.append(num)
print(r_list)


# Function to find the second largest number in list
def second_largest_num(r_list):
    second_largest=r_list[0]
    largest=r_list[0]

    for i in range(len(r_list)):
        if r_list[i] > largest:
            largest = r_list[i]
            
    for i in range(len(r_list)):
        if r_list[i] > second_largest and r_list[i] != largest:
            second_largest = r_list[i]

    return second_largest

print('The second largest number in list is:',second_largest_num(r_list))

# loop to get rid of duplicates
for i in r_list:
    if i not in new_list:
        new_list.append(i)

print('The list without duplicates:', (new_list))
