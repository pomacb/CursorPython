import math 

C = 0
L = 0

def cylinder():
    def circle():
        global C
        C = math.pi*(r**2)
    
    def lateral():
        global L
        L = 2*math.pi*r*h
    
    try:
        h = float(input("Enter height: "))
        r = float(input("Enter radius: "))
        ch = input("Lateral Area - 1, Surface Area - 2: ")
    except:
        print ("Wrong input")
    else:
        if ch == '1':
            lateral()
            print ("{:.2f}".format (L))
        elif ch == '2':
            lateral()
            circle()
            res = L+2*C
            print("{:.2f}".format (res))
        else:
            print ("Incorrect choise")
cylinder()
