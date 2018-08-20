def getInput():
    string = input ('Enter something: ')
    return string

def testInput(param1):
    try:
        i = int(param1)
    except ValueError:
        return False
    else:
        return True

def strToInt(param2):
    i = int(param2)
    return i

def printInt(number):
    print (number)


string = getInput()

if testInput(string) == True:
    num = strToInt(string)
    printInt(num)
else:
    print ('The end')


