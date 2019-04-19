# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result
lower = 0
upper = int(input("Enter range of number= "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
