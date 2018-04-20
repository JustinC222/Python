# Written by: Justin Clark 
# Program Description: This program will calculate a variable amount of Monisen Numbers.

from math import sqrt

#This function will find all the prime numbers between 2 and 100: 
def find_primes():
	for i in range(2,101):
		flag = True
		x = int(sqrt(i))
		for j in range(2,x+1):
			if(i % j == 0):
				flag = False
				break
		if(flag):
			print(i,end=" ")
	
		if(i == 100):
			print("\n")



#This function allows you to pass a number and inquire if it is prime or not. Returns True or False.
def is_prime(x): 

	a = int(sqrt(x))
	
	for j in range(2,a+1):
		if(x % j == 0):
			return False
			
	return True	



# This function will output the first 6 Monisen Numbers.
# If you would like to calculate more than 6 Monisen numbers, change the 19, two lines below, "for P in range(2,19)", to a higher value and as long as there is another Monisen number in that range, it will output it.
# A Monisen Number is any number that is a prime result of Some_Monisen_Number = 2^(another_prime_#) - 1.
def get_Monisen_Numbers():
	for P in range(2,19): 
		if(is_prime(P)): 
			M = 2**P - 1
			if(is_prime(M)):
				print(M, end = " ")



#This outputs the results from the get_Monisen_Numbers function:
print("\nMonisen Numbers: ")

get_Monisen_Numbers()

print("\n")
