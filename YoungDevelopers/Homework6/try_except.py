try: 
	var1 = input("Enter 1st number: ")
	var2 = input("Enter 2nd number: ")
	var1 = int (var1)
	var2 = int (var2)
except ValueError:
	print ("One of the variables isn't a number. Concatenation -> {0}".format (str(var1)+str(var2)))
else:
	print ("{0} + {1} = {2}".format (var1, var2, var1+var2))
