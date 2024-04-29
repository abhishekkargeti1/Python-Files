a = 2
b = 4
result = a+b
print(result)
a = 13
b = 4
result = a-b
print(result)
a = 2
b = 4
result = a*b
print(result)

# Expression Execution 
A,B= 2,3
Txt ="@"
print(2*Txt*3)


A,B="2",3
Txt ="@"
print((A+Txt)*B)

A,B=2,3
C=4
print(A+B*C) 

A,B= 10,5.0
C =A*B
print(C)

A,B=1,2
C=A/B
print(C)


A,B = 1.5,3
C= A //B  
print(C,A/B) 

A,B=5,-2
C=A%B
print(C)

# Taking input from user

# string input 
name = input("name :")


# int input
age = int(input("age : "))

# float input
price = float(input("price :"))
print("My name is ",name," My age is ",age," year old"," My salary is ",price)


# Conditional Statement 

age = int(input("Enter your Age "))
if(age>=18):
    print("You are Eligible")
else:
    print("You are not Eligible")


light =input("Enter the color of light ")
if(light == "red"):
    print("Stop")
elif(light =="Yellow"):
    print("Look")
elif(light == "Green"):
    print("Go")
else:
    print("Incorrect Light Color")


A = int(input("Enter a number "))
Gender = input("Enter M/F ")
if((A==1 or A == 2)and Gender == "M"):
    print(" If is Excuted ")
elif(A == 3 or B == 4 or Gender =="F"):
    print(" Elif 1 is Excuted ")
elif(A == 5 and Gender =="M"):
    print(" Elif 2 is Excuted ")
else:
    print(" Input is wrong ")

# Ternary Operator

Food = input(" Enter a Food Name ")
eat = "Yes"if Food== "cake" else "No"
print(eat)


Food = input("Enter Any Food name ")
print("Yes") if Food == "cake" or Food == "Paties" else print("No")