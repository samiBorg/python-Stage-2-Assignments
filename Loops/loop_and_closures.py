'''
3. Write a program using loops and closure to find the multipliers of 4 (4,8,12,16,....,40)?
'''


def iterator(num):
    def multiply_by_4(num):
        return num*4

    for i in range(num):
        print(multiply_by_4(i))


iterator(11)
