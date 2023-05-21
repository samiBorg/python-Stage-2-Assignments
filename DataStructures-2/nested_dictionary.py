'''
6. Print values from a nested dictionary
'''

d = {'a': {1: 'apple', 2: 'air', 3: 'airoplane'}, 'b': {1: 'ball', 2: 'bat', 3: 'biscuits', 4: 'banglow'},
     'c': {1: 'cat'}, 'd': {1: 'doll', 2: 'dish'}}

for alpha, words in d:
    print(alpha, ": ")
    for word in words:
        print(words[word])