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
#-------------------------------------------------------------------------------------
findmax=lambda lst: "Empty List Can't Find Max" if len(lst)==0 else max(lst)
#-------------------------------------------------------------------------------------
#Main Program
lst=readvalues()
res=findmax(lst) # Anonymous Function Call
print("Max Element=",res)
