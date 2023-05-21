'''
3. Write a program to illustrate Append, Delete and Display Elements of a List using classes
'''


class ListManipulator:
    def __init__(self):
        self.my_list = []

    def append_element(self, element):
        self.my_list.append(element)

    def delete_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
        else:
            print(f"Element '{element}' not found in the list.")

    def display_list(self):
        print("List elements:")
        for element in self.my_list:
            print(element)


if __name__ == "__main__":

    manipulator = ListManipulator()

    manipulator.append_element(10)
    manipulator.append_element(20)
    manipulator.append_element(30)
    manipulator.display_list()

    manipulator.delete_element(20)
    manipulator.display_list()

    manipulator.delete_element(40)
    manipulator.display_list()
