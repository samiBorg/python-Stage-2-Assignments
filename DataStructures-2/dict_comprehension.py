'''
5. Create a Dictionary comprehension to get the length of each word in the list?
'''

s = 'this not so unique string and haves alot of not so unique words. sam, sam, sam, sam'
dict_wordLength = {var: len(var) for var in s.split(" ")}
print(dict_wordLength)