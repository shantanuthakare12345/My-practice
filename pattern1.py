num = int(input("Enter the row in a pattern:- "))
x=0
for i in range(num):
    for j in range(i , num-1):
        print(" ",end=" ")
    if(i == 0):
        x=x+1
        print("*" , end=" ")
    else:
        x=x+2
        for k in range(x):
            print("*",end=" ")
    print()
x=num*2-3
for i  in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    if (j<num):
        for k in range(x):
            print("*",end=" ")
        x=x-2
        
        
    print()