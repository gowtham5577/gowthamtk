print("******************SIMPLE CALCULATOR******************")
print('''Select Your Option
      1.ADD
      2.SUBSTRACT
      3.DIVISION
      4.MULTIPLICATION''')
op=input("->")
if op=='1':
    num1=int(input("enter your first number:"))
    num2=int(input("enter yoiur second number:"))
    print("sum of two number is:",num1+num2)
elif op=='2':
    num1=int(input("enter your first number:"))
    num2=int(input("enter yoiur second number:"))
    print("sum of two number is:",num1-num2)
elif op=='3':
    num1=int(input("enter your first number:"))
    num2=int(input("enter yoiur second number:"))
    print("sum of two number is:",num1/num2)
elif op=='4':
    num1=int(input("enter your first number:"))
    num2=int(input("enter yoiur second number:"))
    print("sum of two number is:",num1*num2)
else:
    print("Invalid command")

