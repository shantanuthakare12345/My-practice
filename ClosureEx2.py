#Program for Demonstrating the Functionality of Closure
#ClosureEx2.py
def   fun1(a): # Outer Function 
	print("Outer Function:",a)
	def fun2():  # Closure
		print("\tInner Function:",a)
	fun2()
	fun2()
	fun2()

#Main Program
fun1(10) # Outer Function Call
