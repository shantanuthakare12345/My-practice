#program for Adding of Two Numbers by using Functions
#INPUT      : Taking INPUT from Main Program i.e through Function Call
#PROCESS    : Processing Done in Function Body
#RESULT     : Displayed in Function Body
#ApproachEx3.py
def addop(a,b):
    c=a+b
    print("Sum({},{})={}".format(a,b,c))

#main program
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
addop(a,b) # Function Call with Input
