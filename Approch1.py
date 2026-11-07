#Program for adding Two Numbers by using Fucntions
#Approch1.py
def addop(a,b): # here a,b, are called formal params
    c=a+b   # here c is Called Local Variable
    return c

#Main Program
res=addop(10,20) # Function Call
print("Sum=",res)
print("----------------------------------")
c=addop(-100,-200)  # Function Call
print("Sum=",c)