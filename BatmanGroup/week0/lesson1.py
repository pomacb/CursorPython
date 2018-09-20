#task2_1
list1 = list(range(1,29,3)); print(list1)

#task2_2
list1 = list1 + [1, 5, 13, 20]
print (list1)

#task2_3
set1 = set(list1); print(set1)

#task2_4
def compare_elements(a:list, b:set):
    list_len = len(a)
    set_len = len(b)
    if list_len > set_len:
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
#Task1
def calculate_fibo(n:int):
    fibo = []
    if n == 0:
        fibo = [1]
        return fibo
    elif n == 1:
        fibo= [1,1]
        return fibo
    else:
        fibo= [1,1]
        while len(fibo) <= n:
            fl = len(fibo)
            v1 = fibo[fl-1]
            v2 = fibo[fl-2]
            fibo.append(v1+v2)
        return fibo
print (calculate_fibo(10))
