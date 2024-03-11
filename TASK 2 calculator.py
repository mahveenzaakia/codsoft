num1=float(input("enter the number:"))
num2=float(input("enter the number:"))
print("press 1 for addition\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division\npress 5 for modulus")
choice=int(input("enter the choice :"))
if choice==1:
    print("the addition of two number is",num1+num2)
elif choice==2:
    print(" the subtraction of two number is",num1-num2)
elif choice==3:
    print(" the multiplication of two number is",num1*num2)
elif choice==4:
    print("the division of two number is ",num1/num2)
elif choice==5:
    print(" the modulyus of two number is",num1%num2)
else:
    print("invalid choice")
    
