'''
3. Create a List comprehension to get the files with .txt extension.
'''

import os
print(os.scandir())

# path for the file
path = "/DataStructures-2"

string_list = [i for i in os.listdir(path) if i.endswith("txt")]
print(string_list)

# reading the text file


