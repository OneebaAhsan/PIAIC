# Write a program to find the factorial of a number

def fact(n1):
    if n1==0:
        return 1
    else:
        return (n1*fact(n1-1))

num = int(input("Enter a number: "))

if num < 0:
   print("factorial does not exist")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("Factorial of num: ",num," is ",fact(num))