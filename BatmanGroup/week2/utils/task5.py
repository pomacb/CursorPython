from functools import reduce

def calc_amount(l: list) -> list:
    out = [reduce(lambda x, y: x+y, list(map(lambda x: x['age'], l)))] + list(filter(lambda x: x['age'] == min(list(map(lambda x: x['age'], l))), l)) + list(filter(lambda x: x['age'] == max(list(map(lambda x: x['age'], l))), l))
    return out
        #min(list(map(lambda x: x['age'], l)))
        # reduce(lambda x, y: x+y, list(map(lambda x: x['age'], l)))


members = [
  {'age': 43, 'name': 'Denis'},
  {'age': 49, 'name': 'Roman'},
  {'age': 36, 'name': 'Godzilla'},
  {'age': 47, 'name': 'Spike'},
  {'age': 31, 'name': 'SuperMan'},
  {'age': 230, 'name': 'Batman'},
  {'age': 37, 'name': 'Claus'},
  {'age': 55, 'name': 'Frank'},
  {'age': 83, 'name': 'Homer'}
]

print(calc_amount(members))
