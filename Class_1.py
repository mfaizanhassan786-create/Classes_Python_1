#Simple print function:

print("Hello World")
print("My name is Faizan Hassan")
print("My age is 17 years")
print("My name is Faizan Hassan","My age is 17 years")

#Variables:

name= "Faizan"
age= 17
price= 10.5
print("My name is",name,"My age is",age,"My price is",price)
print(price)
print("My age is:",age)

#Data Types:

Age2=18
print("My age2 is ",Age2)
print(type(Age2))
print(type(name))
print(type(price))
print(type(age))


#Strings:

print("name1",name1)
print("name2",name2)
print("name3",name3)
print(type(name1))
print(type(name2))
print(type(name3))

#Booleans:

age=17
old=False
a=None
print(type(old))
print(type(a))
print(type(age))

# Python is a case sensitive Language.

#Sum Program:

a=10
A=20
sum=a+A
print(sum)
print(a)
print(A)
print("First value is",a)
print("Second value is",A)
print("Sum of first and second value is",sum)

# And in the subtraction same as addition

# Arthimetic operators
a=5
b=2
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a%b) #Modulus
print(a**b) #Exponentiation
print(a//b) #Floor division

# Comparison operators or relational operators
# Comparison operators are used to compare two values.

a=20
b=10
print(a<b) #Less than
print(a>b) #Greater than
print(a<=b) #Less than or equal to
print(a>=b) #Greater than or equal to

# Assignment operators
# Assignment operators are used to assign values to variables.

a=10
b=20
print(a==b) #Equal to
print(a!=b) #not equal to
a=a+10
print(a)
b=b-10
print(b)
a=a*10
print(a)
b=b/10
print(b)
a=a%10
print(a)
b=b**10
print(b)
a=a//10
print(a)
b=b//10
print(b)

# Or

a-=10
print(a)
b-=10
print(b)

# Logical operators
# Logical operators are used to combine conditional statements.

a=True
b=False
print(a and b)
print(a or b)
print(not a)
print(not b)

#Another Example:

val1=True
val2=False
print(val1 and val2)
print(val1 or val2)
print(not val1)
print(not val2)

# Membership operators
# Membership operators are used to test if a sequence is presented in an object.

a="Faizan"
b="Hassan"
print("Faizan" in a)
print("Hassan" in b)
print("Faizan" not in a)
print("Hassan" not in b)

# type conversion
# Type conversion have two types:
# Type conversion.

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# Type Casting.

a=float("2")
b=4.40
print(type(a))
print(type(b))
print(a+b)

# Input in the Python.

name=input("Enter your name:")
age=input("Enter your age:")
print("Name:",name)
print("Age:",age)
print("Thanks for Input")

# Another Example:

val=input("Enter any Value:")
print(type(val))
print(val)

# To convert the aproperiate data type.

a=int(input("Enter any Value:"))
b=float(input("Enter any Value:"))
print(type(a))
print(type(b))

# Anther example is:

name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
marks=float(input("Enter your marks:"))
print("Wellcome",name)
print("Age:",age)
print("Marks:",marks)
print("Thanks for Input")
print(type(name))
print(type(age))
print(type(marks))

#Let's Practice
#Write a program that takes two numbers as input and prints their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum of first and second number is:", num1 + num2)

#Another example is:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum=num1+num2
print("The sum of first and second number is:", sum)

#Let's another example is:
#WAP to input sides of a square and print its area.

side=input("Enter the side of the square: ")
side=int(side)*int(side)
print("The area of the square is:",side)
print(type(side))

#Another example is:

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The sum of first and second number is:",num1+num2)
print("The difference of first and second number is:",num1-num2)
print("The product of first and second number is:",num1*num2)
print("The division of first and second number is:",num1/num2)
print("The modulus of first and second number is:",num1%num2)
print("The exponentiation of first and second number is:",num1**num2)
print("The floor division of first and second number is:",num1//num2)
print(type(num1))
print(type(num2))



