#Loops in Python
#Loops have the two types in the Python programming language.
#1. For loop
#2. While loop
#For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
#While loop is used to execute a block of code repeatedly until a condition is met.
#For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

#While loop
#While loop is used to execute a block of code repeatedly until a condition is met.

#while condition
  #body

#0Practice 1: While loop
a = 10
while a >= 0:
    a -= 1
    print("a")

#Practice 2: While loop with condition
count = 4
while count <= 5:
   print(count)
   count += 1    
 
#Variable is called iterators. 
#And run the loop is called the iteration.


#Some are the examples of loops in Python
#Example 1: Basic for loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

#Example 2: While loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

#Example 3: For loop with range
for i in range(10):
    if i % 2 == 0:
        print(i)

#Break Function:
# It is used to terminate the loop when encountered.

#Program1:
i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1


#Program2:

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36

i =0 
while i < len(nums):
    if(nums[i] == x):
        print("Found At idx", i)
        break
    else:
        print("Finding..")
    i += 1

print("End of Loop")        

#Continue Function:
# It terminates execution in the current iteration & conitinues
# execution of the loop with the next iteration.  

i = 0
while i <= 5:
    if(i == 3):
        i +=1
        continue #skip
    print(i)
    i+= 1

print("All is done")    