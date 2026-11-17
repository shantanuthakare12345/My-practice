#program for accepting List of Values
# and Find max and Min By using anonymous Functions
#AnonymousFunsEx3.py
def readvalues():
    n = int(input("Enter How Many values u have:"))
    if (n <= 0):
        return list()  # empty List
    else:
        lst = []  # lst=list() --empty list--for adding values
        for i in range(1, n + 1):
            value = float(input("Enter {} Value:".format(i)))
            lst.append(value)
        else:
            return lst
def kvrmax(lst): # programmer-Defined Function
    maxv=lst[0]
    for value in lst[1:]:
        if value > maxv:
            maxv=value
    return maxv
#-------------------------------------------------------------------------------------
findmax=lambda lst: "Empty List Can't Find Max" if len(lst)==0 else kvrmax(lst)
#-------------------------------------------------------------------------------------
#Main Program
lst=readvalues()
res=findmax(lst) # Anonymous Function Call
print("Max Element=",res)
