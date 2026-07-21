def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0 :
        return "not valid cant divide by zero"
    else :
        return x/y
def power(x,y):
    return x**y
print("select the operation that you want to perform")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.power")
while True :
    choice= input("enter the choice: ")
    if choice in ('1','2','3','4','5'):
        num1=float(input("enter the first number: "))
        num2=float(input("enter the second number: "))
         
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} ={sub(num1,num2)}")
        elif choice == '3':
            print(f"{num1} x {num2} = {mul(num1,num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {div(num1,num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1,num2)}")
    
        nextcalc = input("want to do another calculation ? (yes/no)")
        if nextcalc ==  ' no ' :
            print("calculation over")
            break
        elif nextcalc != ' yes ' : 
            print("invalid input")
    else :
        print("invalid input choose from the given options")