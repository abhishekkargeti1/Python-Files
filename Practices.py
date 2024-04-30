# a = 2
# b = 4
# result = a+b
# print(result)
# a = 13
# b = 4
# result = a-b
# print(result)
# a = 2
# b = 4
# result = a*b
# print(result)

# Expression Execution 

# A,B= 2,3
# Txt ="@"
# print(2*Txt*3)


# A,B="2",3
# Txt ="@"
# print((A+Txt)*B)

# A,B=2,3
# C=4
# print(A+B*C) 

# A,B= 10,5.0
# C =A*B
# print(C)

# A,B=1,2
# C=A/B
# print(C)


# A,B = 1.5,3
# C= A //B  
# print(C,A/B) 

# A,B=5,-2
# C=A%B
# print(C)

# Taking input from user

# string input 

# name = input("name :")


# # int input
# age = int(input("age : "))

# # float input
# price = float(input("price :"))
# print("My name is ",name," My age is ",age," year old"," My salary is ",price)


# Conditional Statement 

# age = int(input("Enter your Age "))
# if(age>=18):
#     print("You are Eligible")
# else:
#     print("You are not Eligible")


# light =input("Enter the color of light ")
# if(light == "red"):
#     print("Stop")
# elif(light =="Yellow"):
#     print("Look")
# elif(light == "Green"):
#     print("Go")
# else:
#     print("Incorrect Light Color")


# A = int(input("Enter a number "))
# Gender = input("Enter M/F ")
# if((A==1 or A == 2)and Gender == "M"):
#     print(" If is Excuted ")
# elif(A == 3 or B == 4 or Gender =="F"):
#     print(" Elif 1 is Excuted ")
# elif(A == 5 and Gender =="M"):
#     print(" Elif 2 is Excuted ")
# else:
#     print(" Input is wrong ")

# Ternary Operator

# Food = input(" Enter a Food Name ")
# eat = "Yes"if Food== "cake" else "No"
# print(eat)


# Food = input("Enter Any Food name ")
# print("Yes") if Food == "cake" or Food == "Paties" else print("No")

# age = int(input("Enter your age"))
# vote = ("No","Yes")[age<18]
# print(vote)

# Type Conversion

# a =2 
# b= 2.34
# sum = a+b   # (Here integer automatically convert integer into float because float is higher in compare to integer).


# a = "2"
# b= 2.34
# sum = a+b   # (here error comes because String will not add into float value)

# To overcome the above error we can do this :-

# a = int("2")
# b =10
# sum = a+b
# print(type(a))
# print(sum)

# String

# Concatenation and length

# str1 ="Hello"
# str2 = "World"
# final_string = str1+str2
# print(final_string)
# print(len(str1))

# Indexing

# str1 = "Abhishek"
# print(str1[0])

# Slicing

# str = "Abhishek"
# print(str[1:7]) 

# str = "Abhishek"
# print(str[:8])

# str ="Abhishek"
# print(str[0:])

# str = "APPLE"
# print(str[-3:-1])

# Function of String

# str = "Abhishek Kargeti"
# print(str.endswith("ti"))

# str = "abhishek"
# str = str.capitalize()
# print(str)

# str = "I am a boy"
# str = str.replace("a","b")
# print(str)

# str = "I am from Delhi"
# print(str.find("Delhi"))

# str = "I am from Delhi"
# print(str.find("hello"))

# str = "I am Abhshek . I am from delhi"
# str=str.count("am")
# print(str)

# Lists 


# marks =[12,43,54,64,34]
# print(marks)
# print(marks[0])
# print(len(marks))
# print(type(marks))


# marks= [23,45,67,89,"Abhishek"]
# print(len(marks))
# marks[0]="abhi"
# print(marks)

# marks = [85,94,63,48]
# print(marks[1:4])

# list = [1,2,3,4]
# list.append(5)
# print(list)

# list = [2,5,6,1,3]
# list.sort()
# print(list)

# list = [2,5,6,1,3]
# list.sort(reverse=True)
# print(list)

# list =[1,2,3,4,5,6]
# list.reverse()
# print(list)

# list = [1,2,4,5,6]
# list.insert(2,3)
# print(list)

# list = [1,32,1,2]
# list.remove(1)
# print(list)

# list =[1,2,3,4,5]
# list.pop(3)
# print(list)

# tup = (1,2,3,4,5)
# print(tup)
# print(type(tup))
# print(tup[1])

# tup=()
# print(tup)

# tup =(1,)
# print(tup)

# tup = (1,2,3,4,5)
# print(tup[1:2])

# tup = (1,2,3,4,5,1,3,4,5,2)
# print(tup.index(1))

# tup =(1,2,3,4,5,5,4,3,2,1)
# print(tup.count(2))