#Program for Demonstrating Default Arguments
#DefaultArgsEx1.py
def   studinfo(sno,sname,marks,crs="PYTHON"):  # Here crs is Called Default Parameter
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
studinfo(100,"RS",34.56) # Function Call with 3 Pos Args
studinfo(200,"TR",44.16) # Function Call with 3 Pos Args
studinfo(300,"JH",32.55) # Function Call with 3 Pos Args
studinfo(400,"DR",24.56) # Function Call with 3 Pos Args
studinfo(500,"DT",14.56,"HTML") # Function Call with 4 Pos Args
studinfo(600,"PT",44.56) # Function Call with 3 Pos Args
studinfo(crs="Java",marks=23.78,sno=700,sname="AR") # Function Call with 4 Kwd Args
print("-"*50)


