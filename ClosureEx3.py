#Program for Demonstrating the Functionality of Closure
#ClosureEx3.py
def getyear(year): # Outer Function
	print("Outer Function: Present Year:",year)
	def  monthname(monthval): # Inner Function--Closure
		print("Year:{}  Month:{}".format(year,monthval))
		print("---------------------------------------------------------")
	return monthname
#Main Program
mn=getyear(2026) # Outer Function Call
for i in range(1,13):
	mn(i)
