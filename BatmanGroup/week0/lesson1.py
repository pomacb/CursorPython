#task2_1
list1 = list(range(1,29,3)); print(list1)

#task2_2
list1 = list1 + [1, 5, 13, 20]
print (list1)

#task2_3
set1 = set(list1); print(set1)

#task2_4
def compare_elements(a:list, b:set):
    if len(a) > len(b):
        print ('List is bigger!')
    else:
        print ('Set is bigger!')

compare_elements(list1,set1)

#task3
def get_value_from_list(data:list, index:int):
    try:
        return data[index]
    except IndexError:
       return None

print(get_value_from_list(list1,5))
print(get_value_from_list(list1,25))

#task4
my_dict = {"Name": "", "Age":"", "Hobby":""}
def create_dict(name:str, age:int, hobby:str):
    my_dict['Name'] = name
    my_dict['Age'] = age
    my_dict['Hobby'] = hobby
    return my_dict

print(create_dict('Denis', 26, 'Books'))

#Advanced Level
#Fibonacci
def calculate_fibo(n:int):
    fibo = []
    if n == 0:
        return fibo
    elif n == 1:
        fibo= [0]
        return fibo
    else:
        fibo= [0,1]
        while len(fibo) < n:
            fibo.append(fibo[len(fibo)-1]+fibo[len(fibo)-2])
        return fibo


print (calculate_fibo(10))

#Matrix

def create_matrix(fe:int, rows:int, col:int):

    #calculate first and last row
    max_lenght=len(str(fe+(rows*col-1)));
    fl_row =('#'*max_lenght*col)+'#'*((col-1)+3);

    #create bare matrix
    matrix=[]
    for r in range(rows):
        row_list=[]
        for i in range(col):
            row_list.append(fe)
            fe+=1
        matrix.append(row_list)

    #print beautiful matrix
    print(fl_row)
    for m in matrix:
        str1 = ''
        for l in m:
            str1 += ' '*(max_lenght-len(str(l)))+str(l)+' '
        print('#' + str1 + '#')
    print(fl_row)

create_matrix(40,5,5)
