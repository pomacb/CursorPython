# def strange_list(start: int, finish: int):
#     list2print = []
#     for i in range(start, finish+1):
#         if i%3==0 and i%5==0:
#             list2print.append('FizzBuzz')
#         elif  i%3==0:
#             list2print.append('Fizz')
#         elif i%5==0:
#             list2print.append('Buzz')
#         else:
#             list2print.append(i)
#     return list2print
#
#
# print(strange_list(1,30))


# New way using list Comprehension
def cool_list(start: int, finish: int) -> list:
    return ['Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i for i in range(start, finish + 1)]


if __name__ == "__main__":
    print(cool_list(1, 30))
