#program for Adding of Two Numbers by using Functions
#INPUT      : Taking Inside of Function Body
#PROCESS    : Processing Done in Function Body
#RESULT     : Returning the Result to Main Program
#ApproachEx4.py
def addop():
    a = float(input("Enter First Number:"))
    b = float(input("Enter Second Number:"))
    c=a+b
    return a,b,c

#main program
k,v,r=addop() # Function Call without Input with multi line assigment
print("Sum({},{})={}".format(k,v,r))
print("------------------------------------------------")
res=addop()  # Function Call without Input with single line assigment
# Here res is an object of type <class,tuple>
print("Sum({},{})={}".format(res[0],res[1],res[2]))
print("------------------------------------------------")