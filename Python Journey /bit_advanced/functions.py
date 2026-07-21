def factorial(number):
    if(number == 0):
        return 1
    else :    
        return number*factorial(number-1)
number = int(input("enter and integer"))
result = factorial(number)
print("the factorial of the", number , "is" ,result)