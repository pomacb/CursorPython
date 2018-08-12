def positive():
    print('Positive')

def test():
    try:
        n=int(input('Enter Integer: '))
        if n >= 0:
            positive()
        else:
            negative()
    except:
        print('Wrong input!')

def negative():
    print('Negative')

test()

