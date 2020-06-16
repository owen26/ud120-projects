print('hello world')

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict2 = {k: v for (k, v) in dict1.items() if v > 3 and v < 5}

print(dict2)
