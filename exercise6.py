# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 
# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("please enter a month (Jan-Dec):")
day = int(input("Enter day of the month:"))

if month in( "Dec", 'Jan',"Feb" ,"Mar"):
    if month == "Jan" and day >=1:
        print(f"{month} {day} is in Winter")
    if month == "Dec" and day >=21:
        print(f"{month} {day} is in Winter")
    if month == "Dec" and day <=21:
        print(f"{month} {day} is in Fall")
    if month == "Mar" and day <=19:
        print(f"{month} {day} is in Winter")
    if month == "Mar" and day >=20:
        print(f"{month} {day} is in Spring")
if month in( "Apr", 'May',"Jun"):
    if month == "Apr" and day >=1:
        print(f"{month} {day} is in Spring")
    if month == "May" and day >=1:
        print(f"{month} {day} is in Spring")
    if month == "Jun" and day <=20:
        print(f"{month} {day} is in Spring")
    if month == "Jun" and day >20:
        print(f"{month} {day} is in Summer")
if month in( "Jul", 'Aug',"Sep"):
    if month == "Jul" and day >=1:
        print(f"{month} {day} is in Summer")
    if month == "Aug" and day >=1:
        print(f"{month} {day} is in Summer")
    if month == "Sep" and day <=21:
        print(f"{month} {day} is in Summer")
    if month == "Sep" and day >=22:
        print(f"{month} {day} is in Fall")
if month in( "Oct", 'Nov'):
    if month == "Oct" and day >=1:
        print(f"{month} {day} is in Fall")
    if month == "Nov" and day >=1:
        print(f"{month} {day} is in Fall")