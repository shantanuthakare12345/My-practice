#program for Accepting any value and Decide whether It is Palindrome or not
#AnonymousFunsEx2.py
palindrome=lambda value: "Palindrome" if value==value[::-1] else "Not Palindrome"

#Main Program
value=input("Enter Any Value:")
res=palindrome(value)
print("\t{} is {}".format(value,res))



