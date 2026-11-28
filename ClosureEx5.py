#Program for Demonstrating the Functionality of Closure
#ClosureEx5.py
import calendar
def getyear(year): # Outer Function
	print("Outer Function: Present Year:",year)
	def  monthname(monthval): # Inner Function--Closure
		print(calendar.month(year,monthval))
		print("---------------------------------------------------------")
	for i in range(1,13):
		monthname(i)

#Main Program
getyear(2026) # Outer Function Call
