print("Welcome to the calculator")
def add(num1,num2):
    value=num1+num2
    print(f"The addition value of {num1} and {num2}={value}")
    
def subtract(num1,num2):
    value=num1-num2
    print(f"The subtraction value of {num1} and {num2}={value}")
    
def multiply(num1,num2):
    value=num1*num2
    print(f"The multiplication value of {num1} and {num2}={value}")
    
def division(num1,num2):
    if num2==0:
        print(f"{num1} cannot be devided by 0 ")
    else:
        value=num1/num2
    print(f"The division value of {num1} and {num2}={value}")
    
while(True):
    choice=int(input("Enter your choice:\n 1.add\n2.subtract\n 3.multiplication \n 4.division\n5.exit\n"))
    if choice==1:
        num1=float(input("enter the first number:\n"))
        num2=float(input("enter the second number:\n"))
        add(num1,num2)
    elif choice==2:
        num1=float(input("enter the first number:\n"))
        num2=float(input("enter the second number:\n"))
        subtract(num1,num2)
    elif choice==3:
        num1=float(input("enter the first number:\n"))
        num2=float(input("enter the second number:\n"))
        multiply(num1,num2)
    elif choice==4:
        num1=float(input("enter the first number:\n"))
        num2=float(input("enter the second number:\n"))
        division(num1,num2)
    elif choice==5:
        break
    else:
        print("please enter the valid choice\n")