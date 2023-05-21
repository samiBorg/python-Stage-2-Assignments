'''
1. Define a class which has at least two methods:
    get_string: to get a string from console input
    print_string: to print the string in upper case.
'''


class InputOutput:

    def __init__(self):
        self.str_in = ""

    def get_string(self):
        str_in = input("Please enter a string: ")
        self.str_in = str_in
        print(self.str_in)

    def print_string(self,):
        print(self.str_in.upper())


if __name__ == '__main__':
    obj = InputOutput()
    print("this in the get_string method:")
    obj.get_string()
    print("this is the print_string method:")
    obj.print_string()
