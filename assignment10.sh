#!/bin/bash

#Author: Jacob Nino
#Date: 4/26/22

filename="output.txt"

#Problem 1
 
 sum(){
x=$1
	if (( $x==0 ))
	then
		echo 0
	else
		last=$(sum $(( $x-1)))
		echo $(( $x + last ))
	fi
}

#Function call
sum 4


#Problem 2 

echo "Enter a number"
read n

x=0
y=1

echo "Series"
for (( i=0; i<n; i++ ))
do
	echo -n "$x"
	fn=$((x+y))

	x=$y
	y=$fn

done >>$filename



#Problem 3 

sum(){
x=$1
y=0

	if (( $x==0 ))
	then
		echo 0
	else
		last=$(sum $(( $x-1)))
		echo $(( $x +last )) 
	fi
}
sum 4>>$filename

while read line
do
	echo $line
done <$filename


#Problem 4 
j=0

for i in seq {1..10}
do
	r=$(( $RANDOM % 10 ))
	arr[j]=$r
let j++
done

echo ${arr[@]}

sorted(){
sort=0
len=${#arr[@]}

for (( i=0; i<$len; i++))
do
	for((j=i+1; j<$len; j++))
	do
		if [ ${arr[i]} -ge ${arr[j]} ]
		then
			continue
		else
			sort=${arr[i]}
			arr[i]=${arr[j]}
			arr[j]=$sort
		fi
	done
done
}
#Function call
sorted

echo ${arr[@]} >>$filename

while read line
do
	echo $line
done <$filename
