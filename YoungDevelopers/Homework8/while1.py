total = 100
 
while total > 0:
    n = int(input())
    if total >= n:
        total = total - n
    else:
        print ("Not permitted")
        break
print("Ресурс вичерпано")
