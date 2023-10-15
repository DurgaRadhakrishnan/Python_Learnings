a = int(input("Enter a value \n"))
b = int(input("Enter b Value \n"))

print("Sum is = ",a+b)
print("Sub is =",a-b)
print("Multiplication is = ",a*b)
print("modulo is = ",a%b)
print("divide is = ",a/b)
print("exponential is = ",a**b)
print("floor division is= ",a//b)

# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)
r = float(input("Enter the radius vaiue \n"))
area = float(3.14*r*r)
print("Area of the circle is:",area)


# Create a program that takes two numbers as input and prints whether the first number is
# greater than, less than, or equal to the second number.
num1 =int(input("Enter num1 value is = "))
num2 =int(input("Enter  num2 value is = "))
result = num1>num2
print("The output is",result)
result = num1<num2
print("The output is",result)
result = num1==num2
print("The output is",result)

# Use the ternary operator to find the maximum of three numbers entered by the user.
a,b = 30,25
value = a if a<b else b
print("The final  Ternary output is= ",value)
val_1 =int(input("Enter the first value = "))
val_2 =int(input("Enter the second value = "))
value2 =val_1 if a>b else Val_2
print("The final  Ternary output is= ",value2)

# Develop a Python script that calculates the square and cube of a given number.
x=float(input("Enter the  value of x is="))
y=float(input("Enter the  value of y is="))
square =x**y
print("The value of the Square is= ",square)
cube = x**y*x
print("The value of cube is = ",cube)






