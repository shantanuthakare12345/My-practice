#Program for Demonstrating the Functionality of Closure
#ClosureEx4.py
def getyear(year): # Outer Function
	print("Outer Function: Present Year:",year)
	def  monthname(monthval): # Inner Function--Closure
		print("Year:{}  Month:{}".format(year,monthval))
		print("---------------------------------------------------------")
	for i in range(1,13):
		monthname(i)

#Main Program
getyear(2026) # Outer Function Call
