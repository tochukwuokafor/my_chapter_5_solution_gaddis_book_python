def feet_to_inches(number):
    inch = number * 12
    return inch

my_feet = float(input('Enter the number of feet: '))
my_inch = feet_to_inches(my_feet)
print('The number of inches in', my_feet, 'feet is', my_inch, 'inches')