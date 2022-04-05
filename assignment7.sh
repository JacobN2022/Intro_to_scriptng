#!/bin/sh

#Author: Jacob Nino
#Date: 4/5/22

#Problem 1

echo "This is assignemnt 7"

#Changeing /sh to /bach
echo "This is assignment 7"

#Problem 2

name="Jacob"
course1="History"
course2="Scrippting"
course3="Bio"
course4="College Alegbra"

echo "My namme is" $name
echo "I am enrolled in" $course1 "," $course2 "," $course3 "," $course4

#Problem 3 
#Using special Variables to display name and courses
echo "Command to execute : $0"
echo "My name is : $1"
echo "Course 1 : $2"
echo "Course 2 : $3"
echo "Course 3 : $4"
echo "Course 4 : $5"

#Problem 4

echo "Shell ID = $$"
echo "Arguments passed = $#"

#Problem 5

#To create random number
RANDOM=$$

echo $(($RANDOM%100+1))

if[ RANDOM-ge90 ]
then
	echo"A"
elif [ RANDOM-ge80 ]
then
	echo"B"
elif [ RANDOOM-ge70 ]
then
	echo"C"
elif [ RANDOM-ge60 ]
then
	echo"D"
else
	echo"Failed"
fi

#Problem 6

num1=20
num2=50

#Basic math operations

echo "Addition" $((num1+num2))
echo "Subtraction" $((num1-num2))
echo "Multiply" $((num1*num2))
echo "Division" $((num1/num2))

echo "Increment" $((num1))
echo "Decrement" $((num2))

#Problem 7

echo "What is your salary"
read salary

echo "Gross salary is $(($salary/12))

if [ $salary-le10000 ]
then
	echo"HRA is 20% DA is 80%"
elif [[ $salary-gt10001 && $salary-lt20000]]
then
	echo "HRA is 25% DA is 90%"
else
	echo "HRA is 30% DA is 95%"
fi
