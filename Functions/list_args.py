'''
2. Write a function that will take one list as input and return three different types of list as illustrated in the output. In object2, you can append a list containing triplet of a number but object 3 should be evaluated based on the elements present in the object2 (Note:You have to take care of both the space and time complexities as well)
Input: object1 = [[1,1,1],[2,2,2],[3,3,3]]
Output:
object1 = [[1,1,1],[2,2,2],[3,3,3]]
object2 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
object3 = [[1,1,1],[2,4,2],[3,9,3],[4,16,4]]
'''

def process_lists(input_list):
    object2 = input_list[:]
    object3 = []

    object2.append([object2[-1][0] + 1, object2[-1][0] + 1, object2[-1][0] + 1])

    # Evaluate object3 based on elements in object2
    for sublist in object2:
        new_sublist = [sublist[0], sublist[0] ** 2, sublist[0]]
        object3.append(new_sublist)

    return object2, object3


object1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
object2, object3 = process_lists(object1)

print("object1 =", object1)
print("object2 =", object2)
print("object3 =", object3)

