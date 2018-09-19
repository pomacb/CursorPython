def multiply():
    res = 1
    n = 1
    while n != 0:
        try:
            n = float(input("Enter number: "))
        except:
            print("You entered not a number!")
        else:
            res = res * n
            print("{}".format(res))


multiply()
