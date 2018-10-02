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

# def addload(d: dict)-> dict:
#     d['load'] = d['age']*100/200
# def upmembers2(l: list) -> list:
#     l = [d for d in members]
#     return l


#l = [d['load']:d['age']*100/200 for d in members]


if __name__ == "__main__":
    print(upmembers(members))


    # my = {'age': 43, 'name': 'Denis'}
    #
    #
    # my['load'] = my['age']*100/200
    # print(my)


