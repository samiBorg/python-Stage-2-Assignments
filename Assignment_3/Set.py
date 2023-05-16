'''
2. Create a Set comprehension to get the unique words in
 the string.
'''

s = 'this not so unique string and haves alot of not so unique words. sam, sam, sam, sam'
subset_list = {var for var in s.split(" ")}
print("Here is the set of unique words from a string: ", subset_list)