# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:



# input- score - 89

# output- B

# A: 90-100
# B: 80-89

# C: 70-79

# D: 60-69

# F: 0-59

# If, elif, else

mark =int(input("Please Enter your Mark here \n "))
if mark >= 90 and mark <=100:
    print("Your grade is A")
elif mark <=89 and mark >= 80:
    print("Your grade is B")
elif mark >= 70 and mark <= 79:
    print("Your grade is C " )
elif mark >= 60 and mark<=69:
    print("Your grade is D ")
else :
    print("Your grade is  F")
print("-------------------------------------------------------------- ")

# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

#Input = 2024
#Output = Leap year
Leap_year= int(input("Please enter year \n"))
if Leap_year%4==0 or Leap_year%100!=0 and Leap_year%400==0 :
    print ("You're entered year is Leap year",Leap_year)

else :
    print("this year is not Leap year ")

print("-------------------------------------------------------------- ")

# Write a program that classifies a triangle based on its side lengths.
#
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

x =int(input("Enter the X value\n"))
y =int(input("Enter the y value\n"))
z =int(input("Enter the z value\n"))
if x == y == z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")







