list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
print (list3)

print (list1[2])
list1[2]=1998 # substitute value in pos 2
print (list1)

##basic operations with list

#print (cmp(list2,list2))

print (len(list1))
print (max(list2))
print (min(list3))

tuple1=(1,2,3,6,7,8)
print(list(tuple1)) #convert tuple into list

## list method
list1.append(2000)
print(list1)

# return how many time obj occurs in the list
print (list1.count(2000))

list1.extend(list2); print (list1)

# returns the lowest index of mentioned object
print(list1.index(2000))

list1.insert(5,'new Object in position 5'); print (list1)


