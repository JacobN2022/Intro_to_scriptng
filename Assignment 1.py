# Problem 1
# This program is display my information

print("Jacob Nino")
print("220 W Chris LN")
print("Orange Grove TX 78372")
print("361-660-9116")
print("Computer Science")


# Problem 2
# This program is to calculate to find the number of acres

squareFeet = int(input('Enter total square feet'))
setSquareFeet = 43560

total = setSquareFeet/squareFeet

print('Your number of acres is:',total)


# Problem 3
# This program is calclate a cars distance

# Car distance when driving for 6 hours
miles = 70
hours = 6

distance = miles * hours

print('The distance the car trvel is',distance)

# Car distance when driving for 10 hours
hours = 10

distance = miles * hours

print('The distance the car trvel is',distance)

# Car distance when driving for 15 hours

hours = 15

distance = miles * hours

print('The distance the car trvel is',distance)


# Problem 4
# This program is to indicate if the user is an infant, child, teen, or adult

age = int(input('What is your age'))

if age <= 1:
    print('You are an infant')
else:
    if age >= 2 and age <13:
        print('You are a child')
    else:

        if age >= 13 and age <20:
            print('You are a teen')
        else:
            if age >= 20:
                print('You are an adult')
# Problem 5
# This program is to play a counting game with the user

pennies = 0.01
nickels = 0.05
dimes = 0.10
quarters = 0.25

user_pennies = int(input('How many pennies do you have'))
user_nickels = int(input('How many nickels do you have'))
user_dimes = int(input('How many dimes do you have'))
user_quarters = int(input('How many quarters do you have'))

penn_total = pennies*user_pennies
nick_total = nickels*user_nickels
dime_total = dimes*user_dimes
quart_total = quarters*user_quarters

final_total = penn_total+nick_total+dime_total+quart_total

if final_total ==1.00 or final_total ==100:
    print('Congratulations your total value is equal to one dollar')
else:
    if final_total >1.00 or final_total >100:
        print('Sorry, your amount was more than one dollar')
    else:
        if final_total <1.00 or final_total <100:
            print('Sorry, your amount was less than one dollar')



# Problem 6
#This program is to indicate if the year is a leap year or not

year = int(input('Enter a year'))

if(year % 400==0) and (year % 100==0):
    print('The year you entered is a leap year')

elif(year%4==0) and (year%100!=0):
    print('The year you entered is a leap year')

else:
    print('The year you entered is not a leap year')

    









