'''
Write a program using pathlib lib that
- prints the home directory
- getting the current working directory
- get the file extension from a filename
- read and write text files
- Delete files
- Copy files from one directory to another
'''


from pathlib import Path

# home dir
home_dir = Path.home()
print("Home Directory:", home_dir)

# working dir
cwd = Path.cwd()
print("Current Working Directory:", cwd)

# extension from a filename
filename = "example.txt"
file_extension = Path(filename).suffix
print("File Extension:", file_extension)

# Read and write text files
file_path = Path("example.txt")
file_content = "This is the content of the file."

# Write to a text file
with open(file_path, "w") as file:
    file.write(file_content)

# Read from a text file
with open(file_path, "r") as file:
    content = file.read()
    print("File Content:", content)

# Delete files
file_path.unlink()
print("File deleted.")


