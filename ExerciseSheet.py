#  Write a program to input 2 number & print their sum

num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))
sum = num1 +num2
print(sum)


# Write a program to input side of a square and  print its area

side = int(input("Enter side of Square "))
area_square = side**2
print(area_square)

# Write to input  2 Floating point number & print their average 

num1 = float(input("Enter num1 "))    
num2 = float(input("Enter num2 "))    
average = (num1 +num2)/2
print(average)

# Write a program to input 2 int number a and b 
#   print  True if  a is greater  than or equal  to b . If not print False

a = int(input("Enter a number "))
b = int(input("Enter a number "))
if(a>=b):
    print("True")
else:
    print("False")

                                        # Chapter 2

# Write a program to input  user's first name  & print its length.

name = input("Enter a name ")
print(len(name))

# Write a program to find  number occurrence of $ in a String.

str = "The price of $ in compare to rupees is higher"
print(str.count("$"))   

# Write a program  to check numbeer entered by the user is odd or even 

num = int(input("Enter a number"))
if(num % 2 ==0):
    print("Number is Even")
else:
    print("Number is Odd")

# Write a program to find the greatest of 3 number entered  by user.

num1 =int(input("Enter a number"))
num2 =int(input("Enter a number"))
num3 =int(input("Enter a number"))
if(num1>=num2 and num1>=num3):
    print("Num1 is greater")
elif(num2>=num1 and num2>=num3):
    print("Num2 is greater")
else:
    print("Num3 is greater")

# Write a program to check user input is multiple of 7 or not .

num1 = int(input("Enter a number"))
if(num1 % 7 ==0):
    print("Number is a multiple of 7")
else:
    print("Number is not a multiple of 7")

                                            # Chapter 3
