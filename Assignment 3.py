# Problem 1
# This program is to display cars speed 5 times for accelerating and braking

class Car:
    def __init__(self,year,make):
        self.year=year
        self.make=make
        self.speed=0

    def accelerate(self):
        self.speed +=5


    def brake(self):
        self.speed -=5
        

    def get_speed(self):
        return self.speed

def main():

    # Object created
    car=Car(1997, "ford")


    # Car accelerate 5 times
    for c in range(0,5):
        car.accelerate()
        current_speed=car.get_speed()
        print('Car after accelerating speed is:',current_speed)

    # Car braking 5 times
    for c in range (0,5):
        car.brake()
        current_speed=car.get_speed()
        print('Car speed after braking:',current_speed)
    print(' ')


# Main function call   
main()


# Problem 2
# This program is to create 3 employees objects and display there data

class Employee:
    def __init__(self,name,iD_number,department,job_title):
        self.name=name
        self.iD_number=iD_number
        self.department=department
        self.job_title=job_title

    def printing_info(self):
        print(self.name,self.iD_number,self.department,self.job_title)


def main():
    employee1 = Employee("Susan Meyers",47899,"Accounting","Vice President")
    employee1.printing_info()

    employee2=Employee("Mark Jones",39119,"IT","Programmer")
    employee2.printing_info()

    employee3= Employee("Joy Rogers",81774,"Manufacturing","Engineer")
    employee3.printing_info()
    print(' ')

main()

# Problem 3
# This program is combine employees first and last name also forming email with them

class Employee:
    def __init__(self,first_name,last_name,iD_number,department,job_title):
        self.first_name=first_name
        self.last_name=last_name
        self.iD_number=iD_number
        self.department=department
        self.job_title=job_title
        self.full_name=first_name+' '+last_name
        self.email=first_name+'.'+last_name+'@company.com'

    def printing_info(self):
        #print(self.first_name,self.last_name,self.iD_number,self.department,self.job_title)
        print('The full name is:',self.full_name)
        print('Email:',self.email.lower())
        print(' ')


def main():
    employee1 = Employee("Susan" ,"Meyers",47899,"Accounting","Vice President")
    employee1.printing_info()

    employee2=Employee("Mark", "Jones",39119,"IT","Programmer")
    employee2.printing_info()

    employee3= Employee("Joy", "Rogers",81774,"Manufacturing","Engineer")
    employee3.printing_info()

# Main fuction call
main()


# Problem 4
# This program is to find students average for 6 courses

class Student:
    def __init__(self,name,mark1,mark2,mark3,mark4,mark5,mark6):
        self.name = name
        self.mark1 =mark1
        self.mark2 =mark2
        self.mark3 =mark3
        self.mark4 =mark4
        self.mark5 =mark5
        self.mark6 =mark6

        
mark_list=[]

mark_list.append(Student("Bob",50,90,85,47,64,88))

mark_list.append(Student("Bill",80,99,86,95,98,80))

mark_list.append(Student("Sal",76,36,91,50,75,78))

mark_list.append(Student("Annie",90,99,100,91,89,90))

mark_list.append(Student("Josh",70,75,68,83,81,65))

mark_list.append(Student("Kelly",33,48,78,63,59,25))

mark_list.append(Student("Andrew",69,70,80,64,79,80))

mark_list.append(Student("Whatt",50,88,78,61,16,66))

mark_list.append(Student("Owen",26,75,66,81,98,100))

mark_list.append(Student("Ashton",20,100,46,75,69,82))

mark_list.append(Student("Ray",100,89,86,95,91,93))

mark_list.append(Student("Bella",84,88,81,91,100,67))

mark_list.append(Student("Cat",72,90,91,76,79,85))

mark_list.append(Student("Ty",54,10,75,89,46,82))

mark_list.append(Student("Victor",65,90,67,83,91,76))

mark_list.append(Student("Liz",61,98,78,64,48,73))

mark_list.append(Student("Zach",96,45,37,82,70,77))

mark_list.append(Student("Jon",66,62,87,79,83,71))

mark_list.append(Student("Matt",32,84,72,86,90,100))

mark_list.append(Student("Pete",90,97,100,75,79,87))

mark_list.append(Student("Cameron",70,78,26,72,82,100))

mark_list.append(Student("Jake",82,90,78,96,76,66))

mark_list.append(Student("Paul",49,75,90,95,85,56))

mark_list.append(Student("Pam",96,97,75,81,86,96))

mark_list.append(Student("Bailey",69,71,86,98,78,100))


per_list = []
percentage =0
average =0
for stu in mark_list:
    print('name :{}, {} {} {} {} {} {}' .format(stu.name, stu.mark1, stu.mark2, stu.mark3, stu.mark4, stu.mark5, stu.mark6))
    percentage = (stu.mark1+stu.mark2+stu.mark3+stu.mark4+stu.mark5+stu.mark6)/600
    average = (stu.mark1+stu.mark2+stu.mark3+stu.mark4+stu.mark5+stu.mark6)/6
    per_list.append(percentage)
    print('Percentage is:',percentage)
    print('Average is:', average)
    print(' ')

  
per_list.sort()




    




    
