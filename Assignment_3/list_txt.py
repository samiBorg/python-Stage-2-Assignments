'''
3. Create a List comprehension to get the files with .txt extension.
'''

import os
print(os.scandir())
l = [i for i in os.listdir("C:/Users/Samiksha.B/sam/Assignments/Assignment_3") if i.endswith("txt")]
print(l)

# reading the text file


