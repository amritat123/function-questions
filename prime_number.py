#in this question (prime number) we want....

def prime_number(number):
	num=1
	while num<=number:
		count=0
		i=2
		while (i<=num//2):
			if num%i==0:
				count=count+1
			i=i+1
		if (count==0 and num!=1):
			print(num)
		num=num+1
prime_number(100)

