from functools import reduce

members = [
  {'age': 43, 'name': 'Denis'},
  {'age': 49, 'name': 'Roman'},
  {'age': 36, 'name': 'Godzilla'},
  {'age': 47, 'name': 'Spike'},
  {'age': 31, 'name': 'SuperMan'},
  {'age': 49, 'name': 'Batman'},
  {'age': 37, 'name': 'Claus'},
  {'age': 55, 'name': 'Frank'},
  {'age': 83, 'name': 'Homer'}
]

if __name__ == "__main__":
    print(list(map(lambda x: x['name'].upper(), members)))
  #  print([me for x in members])
    for i in members:
        for key in i.items():
            i['name'] = i['name'].upper()
    print(members)
