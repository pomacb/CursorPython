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


def upmembers(l: list) -> list:
    l = [{k: (v.upper() if k == 'name' else v) for (k, v) in d.items()} for d in members]
    return l


# def upmembers2(l: list) -> list:
#     l = [dict(zip(d.keys(), list(map(lambda d: d['name'].upper(), members)))) for d in members]
#     return l


if __name__ == "__main__":
    print(upmembers(members))




    # print(list(map(lambda x: x['name'].upper(), members)))
    # for i in members:
    #     for key in i.items():
    #         i['name'] = i['name'].upper()
    # print(members)

