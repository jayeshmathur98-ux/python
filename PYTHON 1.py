#variable-variable in python are used as storage to store a data or things.
#in python variable are created by assigning the value using the operators.
#variable act like a cantainer that holds information in memory.
#variable can store different types of data type :-
#integers(int)-∞.....-3,-2,-1,0,1,2,3,......∞
#float(float) - all decimal number
#complex(complex) - 45+889j........
#strings(str)-1-for single line #,2- for multiline "",''
#boolen(bool)- always give result in True and False 
name = "jayesh"
print(name)
age = 19
print(age)
height = 5.11
print(height)
is_student = True
print(is_student)








# a = 12
# b = 12
# print(a + b)

# for i in range(7,71,7):
#     print(i)

# n = int(input("which table you want : -"))
# for i in range(1,11):
#     print(f"{n} * {i} = { n*i}")

# n = int(input("please tell your number:-"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum+1
# print(f"your sum is {sum}")    

# n = int(input("please tell your number:-"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * 1
# print(f"your factorial is {fact}")

# a = "sheryians"
# print(a[2:6:1])
# print(a[5:8:1])

# a = 1234567788
# print(type(float(a)))

# a = input("enter your name")
# a = input("enter your age")
# print(a)

#ARITHMETIC OPERATORS
# a = 12
# b = 12 
# print(a + b)
# print(a- b)
# print(33/3)
# print(39//3)
# print(3*6)
# print(5**2)
# print(36%7)

# a = int(input("enter you number"))
# for i in range(1,11):
#     print(i)

#ASSIGNMENT OPERATORS
# a = 120
# a += 130
# a += 150
# a += 150
# print(a)

# b = 20
# b-= 20
# b -= 40
# b-= 60
# print(b)

# a = 130
# a *= 120
# a *= 110
# a *= 100
# print(a)

# a = 600
# a /= 10
# a /= 8
# a /= 5
# print(a)

# a = 600
# a //= 10
# a //= 3
# a //= 2
# print(a)

# a = 39
# a %= 2
# a %= 3
# print(a)

# a = 5
# a **= 2
# a **= 2
# print(a)

#COMPARISM OPERATORS
# a = 12 
# b = 12 
# print(a == b)
# print(a != b)

# a = 12.1
# b = 12
# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)
# print(45<67)
# print(ord("A"))
# print(ord("B"))
# print("A" > "B")

#LOGICAL OPERATORS
#1 AND
# print(12>20 and 123>100 and 34==34 and 45>90)
# print(130>120 and 34==34 and 34!=35 and 45<90)

#2 or
# print(460<456 or 25==25 or 35!= 35 or 45<=34)
# print(12!=12 or 23==45 or 67==56 or 10>5)

#or not 
# print(not 12 == 12)

# num1 = int(input("please tell your fist number"))
# num2 = int(input("please tell your second number"))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")

# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")

# else:
#     print("both number are same")    



# gen = input("please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'm':
#     print("GOOD MORNING SIR")
# elif gen == 'F' or gen == 'f':
#     print("GOOD MORNING MAM")
    
# else:
#     print("unidentified gender")    



# num = int(input("please tell your number :-"))
# if num%2 == 0:
#     print("even number")    
# else:
#     print("odd number")

# Name = input("please tell your name :- ")
# Age = int(input("now tell your age :-"))

# if Age == 18:
#     print(f"hello {Name} you are a valid voter")
# else:
#     left_age = 18 - Age
#     print(f"hello {Name} you are not a valid voter")
#     print(f"you can vote after {left_age} years")    


# year = int(input("tell your number :-"))
# if year %100 == 0 and year %400 == 0:
#     print("its a leap year")
# elif year %100 != 0 and year %4 == 0:
#     print("its a leap year")
# else:
#     print("its a normal year")


# t = int(input("please tell the temperatur:-"))
# if t < 0:
#     print("freezing cold")
# elif t >= 0 and t <= 10:
#     print("very cold")    
# elif t >= 10 and t <= 20:
#     print("cold")
# elif t >= 20 and t <=30:
#     print("pleasant")    
# elif t >= 30 and t <=40:
#     print("hot")
# else:
#     print(" temperature is very hot")    

# for loops
# for i in range(1,101):
#     print(i,"hello world")

# for i in range (1,11,1):
#     print("sorry")

# a = range(1,21,1)
# for i in a:
#     print(i)

# for i in range (16,0,-1):
#     print(i)

# for i in range (-5,-16,-1):
#     print(i)

# for i in range (5,51,5):
#     print(i)

# for i in range (7,71,7):
#     print(i)


# n = int(input("which table you want ? :-"))
# for i in range (n,(n*10)+1,n):
#     print(i)

# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))
# for i in range (len(a)):
#     print(a[i])

# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i)


# even = 0
# odd = 0
# for i in range(1,51):
#     if 1 % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print(even)
# print(odd)        

#2. count vowels from a string
# s = "Hello Sherry"
# count = 0 
# for i in s:
#     if i in "aeiouAEIOU":
#         count = count + 1
# print(f"count of vowels are: {count}")        

#3 YOU HAVE A RANGE FROM 1 TO 20 YOU JUST TO PRINT NUMBER THAT ARE ONLY DIVISILBLE BY BOTH 3 AND 5 
# for i in range(1,21):
#     if i % 3 == 0 and 1 % 5 == 0:
#         print(i)

# n = int(input("which table you want :- "))
# for i in range (1,11):
#     print(f"{n} * {i} = {n*i}")

# n = int(input("please tell your number :- "))

# sum = 0 

# for i in range (1,n+1):
#     sum = sum + i

# print(f"your sum is {sum}")



# n = int(input("please tell your number :- "))

# fact = 1

# for i in range (1,n+1):
#     fact = fact*i

# print(f"your factorial is {fact}")


# n = int(input("tell your number :- "))
# even = 0
# odd = 0 
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else :
#         odd = odd + i
# print(f"your even and odd sum are {even},{odd}")            


# n = int(input("which number factor you want :-"))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = int(input("check your number is prefect or not :-"))
# sum = 0
# for i in range (1,n):
#     if n%1 == 0:
#         sum = sum + i
# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")            


# n = int(input("check your number is prime or not :-"))

# count = 0 

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("your number is prime")        
# else:
#     print("not a prime number")



# a = "SHERYIANS"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])



# a = "SHERYIANS TEACHS INDUSTRY THINGS" 
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)



# a = "SHERYIANS"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("your string is pallindrome")
# else:
#     print("its not a pallindrome")    

# n = 10
# for i in range(1,11,1):
#     if n % i == 0:
#         print(i)


# num = 10
# count = 0
# for i in range (1,num+1):
#     if num % i == 0:
#         count += 1
# print(count)


# # n = int(input("check your number is prime or not :-"))
# count = 50

# for i in range(1,51):
#     if 51%i == 0:
#          count = count + 1
# if count == 2:
#     print("your number is prime")        
# else:
#     print("not a prime number")



# sum = 0
# num = 10
# for i in range (1,num+1):
#     if num % 1 == 0:
#         sum = sum + 1
# print(sum)        



#ques print number from 1 to 50 prime number -> jinke factors 2 ho (1 and number itself)


# for num in range(1,51):
#     factor = 0

# for i in range(1,num+1):
#     if num % 1 == 0:
#         factor += 1 

# if factor == 2:
#     print(num)


# num = 1024
# num2 = str(num)
# for i in num2:
#     print(i)


# while loop -> condition true hai
#we have to make while condition false at some point otherwise it will become infinite loop 
# i = 0 
# while i < 11:#jab tak condition true ,while will keep executing.
#     if i == 5:
#         break
#     print(i)
#     i = i + 1

# num = 1054
# while num > 0:
#     print(num % 10 )#last digit ko print kar dega 
#     num = num//10 #last digit ko remove kar dega 
# print("num is" ,num)    









































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































