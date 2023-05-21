'''
2. Create an iterator that returns numbers, starting with 1, and each sequence will increase by one
(returning 1,2,3,4,5...) and raise StopIteration exception when the number is greater than 10 ?
'''

for i in range(1, 11):
    print(i)

else:
    print("Sorry!! Number is greater than 10!!")
    raise StopIteration
