'''

1. Write a program to create a list of tuples from given list
having number and its square in each tuple? Also, convert
the list of tuples to a dictionary. (Using Comprehension)
'''

list_user = [1, 2, 3, 4, 5]
tuple_list = [(x, x ** 2) for x in list_user]
dict_square = {x: x_sq for (x, x_sq) in tuple_list}
dict_list = {list_user.index(i)+1: i**2 for i in list_user}
dict_enu = {x: x_sq**2 for x, x_sq in enumerate(list_user, start=1)}
print("the list-->", list_user)
print("the tuple list of squares from list-->", tuple_list)
print("the dictionary of squared numbers from list of tuple-->", dict_square)
print("dictionary with the list-->", dict_list)
print("dictionary enumerated-->", dict_enu)

