#Program for Demonstrating Default Arguments
#DefaultArgsEx2.py
def   studinfo(sno,sname,marks,crs="PYTHON",city="HYD"):  # Here crs is Called Default Parameter
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,city))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE\tCITY")
print("-"*50)
studinfo(100,"RS",34.56) # Function Call with 3 Pos Args
studinfo(200,"TR",44.16) # Function Call with 3 Pos Args
studinfo(300,"JH",32.55) # Function Call with 3 Pos Args
studinfo(400,"DR",24.56) # Function Call with 3 Pos Args
studinfo(500,"DT",14.56,city="USA") # Function Call with 3 Pos args + 1 kwd Arg
studinfo(600,"PT",44.56,city="RSA",crs="Java") # Function Call with 3 Pos Args + 2kwd args
print("-"*50)


