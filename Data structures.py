#data structures(advanced data types)
#data structure are used to store,organize and manipulate data effeciently . python provide several built in data structures.
#And for storing multiple values we will again use variable 
#now in python we have 4 types of built in data structure
#1-list , 2-tuple , 3-dictionary , 4-set

#custom data structures 
#stack , queue , linked list , graphs etc 
#searching algorithms ,sorting algorithm

#lists basics - the syntax of list is [] square brackets and if you wnt to create a list you can use []
#now list having indexing and silicing and it is same as string 
#1-heterogenous data structure-multiple types ke data ko store karwa sakta hai. 
#2-duplicacy is allowed.
#3-list is ordered.
#4- mutable - we can change the value of the item in the lists 


#l = [] empty lists
#1 =[10,20,30,40,40]
# print(l)
# print(type(l))

# a = [10,20,30,40,50]
# print(a[0:3])


# a = [10,20,30,40,50]
# print(a[0:4:1])


#list traveling and methods 

#1.append()->adding element at  the last of lists

# a = [10,20,30,40,50]
# a.append(100)
# print(a)


#2-> .extend()-
# l1 = [10,20,30,40,50]
# l2 = [60,70,80]
# l1.extend(l2)
# print(l1)

# #3- .insert(index,value)
# l1 = [10,20,30,40,50]
# l1.insert(1,100)
# print(l1)



# #4 -.pop()
# l1 = [10,20,30,40,50]
# l1.pop(1)
# print(l1)


#5- .remove(element)
# l1 = [1,5,5,5,5,2,3,4,5]
# l1.remove(5)#agar duplicate value hai toh first occurance remove.
# print(l1)


#6- len()-> list ki length print karta hai
# l1 = [1,5,5,5,5,2,3,4,5]
# print(len(l1))



# a = [10,20,30,40,50]
# #1st way(index wise loop)
# for i in range(len(a)):
#     print(a[i])


# #2nd way(item wise loop)
# for i in a:
#     print(i)
#i -> index of lists 
#a[i] -> item at index



#1. accept lists element  and reprint it.
#part1 accept element 
# n = int(input('enter the size of the list:'))
# l = []
# for i in range(n):
#     element = input(f'enter element {i} for your list: ')
#     l.append(element)
# print(l)


a = [10,20,30,40,50]
rev = 0
for i in range(-1):
    rev = rev*10
    a = a //10   
print(rev(a))    








# a = [1,67,10,25,14,77]
# for i in range(len(a)):
#             if a[i] > 15:
#                     print(i)



# a = [10,20,30,40,50]
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum/len(a))


# a =[-45,67,12,-68,-69,-48484,47474]
# print("positive element are")
# for i in a:
#     if i >= 0:
#         print(i)
# print("negative element are")
# for i in a:
#     if i < 0:
#         print(i)



# a =[12,15,27,18,38,48,59,40,87]
# largest = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i
# print(f"your largest number is {largest} at index {index}")        



# l =[12,15,27,18,38]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(sec_largest, largest)            


# a = [12,13,14,15,16]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")


#Tuple 

# syntax ()
#1 -immutable - you cannot change the value of tuple 
#2- duplicates - you have duplicate value in tuple there is no restriction
#3 - ordered -set are ordered and you can access them through index values.
#4- heterogenous - set also have heterogenous nature and can have different type of datat type of dat structure in tuple

#tuple traveling
#1-Tuples can be traversed using loops, just like lists.
#2-Elements can be accessed using indexing and slicing.
#3-Once created, tuple elements cannot be modified.


#Tuple Methods

#1.index() – Returns the index of the first occurrence of an element.
#2.count() – Returns the number of times an element appears.

# t = (5, 2, 9, 1, 5, 6)

# print(t.index(9))   # Output: 2
# print(t.count(5))   # Output: 2


#key point
#Tuple = Immutable + Ordered + Duplicates Allowed + Supports Different Data Types




#set- syntax -{}
#special features
# Mutable – A set can be modified after creation (add or remove elements).
# No Duplicates – Duplicate values are not allowed; every element is unique.
# Unordered – Elements are not stored in a fixed order, and indexing is not supported.
# Heterogeneous – A set can store different data types such as integers, strings, and tuples.

# How Sets Store Values
# Each element in a set is stored using hashing.
# A hash value is generated for every element.
# The hash value helps Python store and find elements efficiently in memory.
# Since hashing does not maintain order, sets are unordered.
# Only immutable (hashable) objects can be stored in a set.


# my_set = {10, 20, 30, "Jayesh", (1, 2)}

# my_set.add(40)      # Add element
# my_set.remove(20)   # Remove element

# print(my_set)

# Remember:
# Set = Mutable + Unique Values + Unordered + No Indexing.



#Set Traversing

#1-A *set is unordered*, so it does not have index values.
#2-You *cannot access elements using indexing* like s[0].
#3-The order of elements may appear different each time.

# Set Methods

#1-Sets are *mutable*, meaning elements can be added or removed.
#2-Common methods:

# s = {1, 2, 3}

# s.add(4)       # Adds 4
# s.remove(2)    # Removes 2 (error if not found)
# s.discard(5)   # Removes 5 (no error if not found)
# s.pop()        # Removes a random element
# s.clear()      # Removes all elements


### Set Operations

# Let:

# python
# A = {1, 2, 3}
# B = {3, 4, 5}


# * *Union (A | B)* → Combines all elements
#   Result: {1, 2, 3, 4, 5}

# * *Intersection (A & B)* → Common elements
#   Result: {3}

# * *Difference (A - B)* → Elements in A but not in B
#   Result: {1, 2}

# * *Symmetric Difference (A ^ B)* → Elements in either set, but not both
#   Result: {1, 2, 4, 5}

### Shortcuts

# python
# A | B   # Union
# A & B   # Intersection
# A - B   # Difference
# A ^ B   # Symmetric Difference


# *Summary:* Sets are unordered collections of unique elements. They support adding/removing elements and powerful operations like union, intersection, difference, and symmetric difference.



#Dictionary-
# synatx - empyt {}
# d = {}            #output - <class 'dict'>
# print(type(d))

# Dictionary Powers

# 1-Mutable* – You can add, update, or delete items after creation.
# 2-Unique Keys* – Every key must be unique.
# 3-Duplicate Values Allowed* – Values can be repeated.
# 4-Ordered* – Items are stored in the order they are inserted.
# 5-Heterogeneous* – Can store different data types (string, integer, list, etc.).


# Dictionary Syntax and Working

# 1-Dictionary stores data in *key-value pairs*.
# 2-A *key* is used to identify a value.
# 3-Keys work similarly to indexes in a list.
# 4-Values are accessed using their keys.
# 5-Supports CRUD operations:

# 1-*Create* – Add new data.
# 2-*Read* – Access data.
# 3-*Update* – Modify data.
# 4-*Delete* – Remove data.


## Dictionary Traversing

# * Traversing means visiting all elements of a dictionary.
# * We can traverse both *keys and values*.
# * By default, a loop traverses keys.
# * Values can be accessed through their corresponding keys.
# * Keys and values can be processed together.

# ---

# ## Dictionary Methods

# * *keys()* – Returns all keys.
# * *values()* – Returns all values.
# * *items()* – Returns both keys and values.
# * *get()* – Safely accesses a value using a key.
# * *pop()* – Removes a specific key-value pair.
# * *clear()* – Removes all items from the dictionary.

# ### Short Summary

# A *Dictionary* is a mutable collection of *key-value pairs* where keys are unique, values can repeat, and data can be accessed using keys.


















