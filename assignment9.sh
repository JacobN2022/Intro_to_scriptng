#!/bin/bash

#Author: Jacob Nino
#Date: 4/19/22


#Problem 1 

RANDOM=$$


j=0
for i in seq {1..19}
do
	r=$(( $RANDOM % 20 ))
	arr[j]=$r
let j++

done

echo "Unsorted" ${arr[@]}

sort=0
len=${#arr[@]}
for ((i=0; i<$len; i++))
do
	for((j=i+1; j<$len; j++))
	do
		if [ ${arr[i]} -le ${arr[j]} ]
		then
			continue
		else
			sort=${arr[i]}
			arr[i]=${arr[j]}
			arr[j]=$sort
		fi
	done
done
echo "Sorted" ${arr[@]}

#Problem 2

j=0
for i in seq {1..19}
do
	r=$(( $RANDOM % 20 ))
	arr[j]=$r
let j++
done

echo "Unsorted" ${arr[@]}

sort=0
len=${#arr[@]}
for ((i=0; i<$len; i++))
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
echo  "Sorted" ${arr[@]}


#Problem 3

j=0
for i in seq{1..51}
do
	arr[j]=$j
let j++
done

echo ${arr[@]}


#Problem 4 

sum (){

j=0
for i in seq{1..51}
do
	arr1[j]=$j
let j++
done


j=2
prime_sum=0
for i in "${arr[@]}"
do
	if [ $(($i%j)) -eq 0 ]
	then
		echo "not prime"
	else
		echo "prime"
		let prime_sum+=$i
	fi
done

echo "Prime Total: $prime_sum"
}

#Function call
sum



#Problem 5 

j=0
even=0
odd=0
for i in seq{1..51}
do
	arr[j]=$j
	let j++
done

j=0
for i in seq{1..51}
do
	if ((arr[j]%2==0))
	then
		even=$((arr[j]+even))
	else
		odd=$((arr[j]+odd))
	fi
let j++
done

echo "Even sum:" $even
echo "Odd sum:" $odd

