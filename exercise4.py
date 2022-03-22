# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


print("Enter the lengths of three side of a triangle:")
sidea = int(input("Enter the lengths of side A:"))
sideb = int(input("Enter the lengths of side B:"))
sidec = int(input("Enter the lengths of side C:"))

if sidea== sideb == sidec:
    print(f"A triangle with sides of {sidea}, {sideb} & {sidec} is an equilateral triangle")
elif sidea == sideb or sidea ==sidec or sideb == sidec:
    print(f"A triangle with sides of {sidea}, {sideb} & {sidec} is a scalene triangle")
else:
    print(f"A triangle with sides of {sidea}, {sideb} & {sidec} is an isosceles triangle")

