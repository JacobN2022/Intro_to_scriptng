
#!/bin/bash

#Author: Jacob Nino
#Date: 4/12/22

#Problem 1 

i=1

while [ $i -le 15 ]
do
	echo $i
	let i++
done

i=1

until [ ! $i -le 15 ]
do
	echo $i
	let i++
done

for i in $(seq 15)
do
	echo $i
done



#Problem 2
i=20
sum=0

while [ $i -le 40 ]
do
	((sum += $i))
	let i++
done
echo "While Loop:" $sum


until [ ! $i -le 40 ]
do
	((sum += $i))
	let i++
done
echo "Until Loop:" $sum

i=0
sum=0

for i in {20..40}
do
	((sum+= $i))
done
echo "For Loop:" $sum

#Problem 3 

i=0
echo "While loop:"
while [ $i -le 50 ]
do
	if [ $((i%2)) -eq 0 ]
	then
		echo $i "not prime"
	else
		echo $i "is prime"
	fi
let i++
done


i=0

echo "Until Loop:"
until [ ! $i -le 50 ]
do
	if [ $((i%2)) -eq 0 ]
	then
		echo $i "not prime"
	else
		echo $i "is prime"
	fi
let i++
done

echo "For Loop:"
for i in $(seq 50)
do
	if [ $((i%2)) -eq 0 ]
	then
		echo $i "not prime"
	else
		echo $i "is prime"
	fi
done


#Problem 4 

echo "Enter a word"
read word

select WORD in corpus Kingsville commeerce stop
do
	case $word in corpus)
		echo "Texas A&M University Corpus Christi"
		;;
	Kingsville)

		echo "Texas A&M University Kingsville"
		;;
	commeerce)
		echo "Texas A&M University Commerce"
		;;
	stop)
		break
	;;
	*) echo "Texas A&M University"
	;;
	esac
done

#Bonus

num=20

if [ $num -ge 1 ] && [ $num -le 10 ]
then
	echo "Between 1 and 10"
elif [ $num -ge 11 ] && [ $num -le 20 ]
then
	echo "Between 11 and 20"
elif [ $num -gt 20 ]
then
	echo "Greater than 20"
else
	echo "Less than 1"
fi
