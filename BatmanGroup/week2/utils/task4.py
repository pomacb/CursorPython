def with_O(l: list) -> list:
    return list(filter(lambda x: 'o' in x['name'].lower(), l))
