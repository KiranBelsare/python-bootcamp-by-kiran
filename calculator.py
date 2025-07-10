#que6
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

num1 = int(input("enter 1 num: "))
num2 = int(input("enter 2 num: "))
op = input("operation to perform(+,-,*,/): ")

if(op=="+"):
   print(add(num1, num2))
elif(op=="-"):
    print(sub(num1,num2))
elif(op=="*"):
    print(mul( num1, num2))
else:
    print(div(num1, num2))