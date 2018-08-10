try:
	num = float (input("Enter number: "))

except ValueError:
	print ("You entered not a number")
else:
	if num > 0:
		print ("1")
	elif num < 0:
		print ("-1")
	else:
		print ("0")
