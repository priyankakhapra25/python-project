
print("1-   ADDITION \n 2-   SUBTRACTION\n 3-   MULTIPLICATION\n4-  DIVISION\n")


n1=int(input("PRESS 1 to continue & PRESS 0 for exit"))
while n1==1:

    ch=int(input("Enter your choice:"))
    if ch<=4 and ch!=0:
        print("Enter two numbers\n")
        a=int(input("Enter a:"))
        b=int(input("Enter b"))

        if ch==1:
            print("Addition is:", a+b)        
        elif ch==2:
            print("Subtraction is:", a-b)
        elif ch==3:
            print("Multiplication is:", a*b)
        elif ch==4:
            print("Division is:", a/b) 
    elif ch==0:
        print("OK , Thank you!")
        break
    

    else:
        print("Wrong choice, Enter valid choice")           