#List:

marks = [90,80,70,60,50]
print(marks)
print(type(marks[0]))
print(type(marks))
print("length of list is",len(marks))
print(marks[0])
print(marks[1])
print(marks[2])         
print(marks[3])
print(marks[4])
print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[-4])
print(marks[-5])

#Strings are the immutable (cannot be changed) in the python
#Lists are the mutable (can be changed) in the python

student = ["Ahamd",20,"A"]
print(student)
print(type(student[0]))
print(type(student))
print("length of list is",len(student))
print(student[0])
print(student[1])
print(student[2])
print(student[-1])
print(student[-2])
print(student[-3])

#or

student = ["Ahmad", 20, "A"]
print(student)
student[0] = "Ali"
print(student)
student[1] = 21
print(student) #That is allow is the python.
student[2] = "B"
print(student)


#List Slicing:

marks = [90,80,70,60,50]
print("Marks of first 3 students:",marks[0:3])
print("Marks of last 2 students:",marks[-2:])
print("Marks of first 4 student",marks[0:4])


#List Methods:

#append(): Adds an element to the end of the list.
#insert(): Inserts an element at a specific position in the list.
#remove(): Removes the first occurrence of a specific element from the list.
#pop(): Removes and returns the element at a specific position (default is the last element).
#sort(): Sorts the list in ascending order.
#reverse(): Reverses the order of the elements in the list.
#count(): Returns the number of occurrences of a specific element in the list.
#index(): Returns the index of the first occurrence of a specific element in the list.
#copy(): Returns a shallow copy of the list.
#clear(): Removes all elements from the list.

#Append method:

list1 = [90,80,70,60,50]
print(list1)
list1.append(100) 
#If we are print the append function then the return in the result  will be none.
print(list1.append(100))
print(list1)

#Sort method:
#Two types of sort method:
#1. sort(): Sorts the list in ascending order.
#2. sort(reverse=True): Sorts the list in descending order.

list1 = [90,80,70,60,50]
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#Reverse method:

list1 = [90,80,70,60,50]
print(list1)
list1.reverse()
print(list1)

#or

lis2=['a','b','c','d','e']
print(lis2)
lis2.reverse()
print(lis2)

#Count method:

list1 = [90,80,70,60,50]
print(list1)
print(list1.count(90))

#Index method:

list1 = [90,80,70,60,50]
print(list1)
print(list1.index(90))

#Insert method:

list1 = [90,80,70,60,50]
print(list1)
list1.insert(1,100)
print(list1)

#Remove method:

list1 = [90,80,70,60,50]
print(list1)
list1.remove(90)
print(list1)

#Pop method:

list1 = [90,80,70,60,50]
print(list1)
list1.pop()
print(list1)

#or

list1 = [90,80,70,60,50]
print(list1)
list1.pop(1)
print(list1)

#Copy method:

list1 = [90,80,70,60,50]
print(list1)
list1.copy()
print(list1)

#Clear method:

list1 = [90,80,70,60,50]
print(list1)
list1.clear()
print(list1)


#Tuples:

# Tuples are immutable, which means they cannot be changed after creation.
# Tuples are ordered collections of elements.
# Tuples are defined using parentheses ().
# Tuples can contain elements of different data types.
# Tuples are more memory-efficient than lists.
# Tuples are faster than lists.
# Tuples are immutable, which means they cannot be changed after creation.
# Tuples are ordered collections of elements.
# Tuples are defined using parentheses ().
# Tuples can contain elements of different data types.
# Tuples are more memory-efficient than lists.
# Tuples are faster than lists.


#Tuple Methods:

tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-1])
print(tup[-2])
print(tup[-3])
print(tup[-4])
print(tup[-5])

#or

tup = ("Hello")
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-1])
print(tup[-2])
print(tup[-3])
print(tup[-4])
print(tup[-5])


#Note: If we are print the tuple without parentheses then the return in the result  will be string.
#Note: If we are print the tuple with parentheses then the return in the result  will be tuple.

#or

tup = ("Hello",)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])

#Slicing:

tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0:3])
print(tup[-2:])
print(tup[0:4])



#count(): Returns the number of occurrences of a specific element in the tuple.
#index(): Returns the index of the first occurrence of a specific element in the tuple.

#Index method:

tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))
print(tup.index(3))

#Count method:

tup = (1,2,3,4,5,1,4)
print(tup)
print(type(tup))
print(len(tup))
print(tup.count(1))