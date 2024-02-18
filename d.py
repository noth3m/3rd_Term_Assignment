# def sum(a,b):
#     c = a + b
#     print(f"the sum of the two numbers is {c}")
# def difference(a,b):
#     c = a - b 
#     print(f"the difference of the two numbers is {c}")
# def product(a,b):
#     c = a*b 
#     print(f"the product of the two numbers is {c}")
# def division(a,b):
#     c = a//b
#     print(f"the quotient of the two numbers is {c}")   
# x = input("Input the operation you want to perform (ALL CAPS) ")
# def assign_str(str1,str2):
#     global a 
#     global b
#     a = int(input(str1)) 
#     b = int(input(str2))
# if x == "ADDITION":
#     assign_str("Enter First Number ", "Enter Second Number ")
#     sum(a,b)
# elif x == "SUBTRACTION":
#     assign_str("Enter Minuend ", "Enter Subtrahend ")
#     difference(a,b)
# elif x == "MULTIPLICATION":
#     assign_str("Enter First Multiple ", "Enter Second Multiple ")
#     product(a,b)
# elif x == "DIVISION":
#     assign_str("Enter Dividend ","Enter Divisor ")
#     division(a,b)
# else:
#     print("Input Error")
### lodu sa program ###
# def Weather_to_Emoji(weather):
#     if weather == "rain ":
#         print("☔")
#     elif weather == "cloudy":
#         print("⛅")
#     elif weather == "sunny":
#         print(":sun:")
# Weather_to_Emoji("sunny")
### lodi si exercise ###
# def BiggerNum(a,b):
#     if a > b :
#         return a
#     elif b > a :
#         return b 
#     else:
#         return "both are equal" 
# n1 = int(input("Enter First Num "))
# n2 = int(input("Enter Second Num "))
# print(f'The Bigger number is {BiggerNum(n1,n2)}')
'''Calculator remake using Lambda'''
sum = lambda a,b: a + b
difference = lambda a, b : a - b
product = lambda a , b : a*b
division = lambda a , b : a//b
x = (input("Name the operation you want to perform: "))
def InputStatement(str1 , str2):
    global a ,b 
    a = int(input(f'Enter {str1}')) 
    b = int(input(f'Enter {str2}'))
if x.upper() == "ADDITION":
    InputStatement("First Number ","Second Number ")
    print(f'Sum of the two numbers is {sum(a,b)}')
elif x.upper() == "SUBTRACTION":
    InputStatement("Mineund ","Subtrahend ")
    print(f'Difference of the two numbers is {difference(a,b)}')
elif x.upper() == "MULTIPLICATION":
    InputStatement("Multiple ","Multiple ")
    print(f'Product of the two numbers is {product(a,b)}')
elif x.upper() == "DIVISION":
    InputStatement("Dividend ","Divisor ")
    print(f'The Quotient of the two numbers is {division(a,b)} and remainder is {a%b}')
else:
    print("INPUT ERROR")