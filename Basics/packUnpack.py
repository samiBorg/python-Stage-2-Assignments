# unpacking with "*"
args = [1, 2, 3]


def add(a, b, c):
    return a+b+c


print("addition is: ", add(*args))

# packing with "*"


def max_of(*args1):
    return max(args1)


print("maximum among: ", max_of(2, 5, 4))


# unpacking with "**"


def display(a, b, c):
    print("displaying dictionary content:")
    print(a, b, c)


d = {"a": 1, "b": 2, "c": 3}
display(**d)

# packing with "*"


def info(**d2):
    print("content in the form of dictionary:")
    for i in d2:
        print(i, ": ", d2[i])


info(name="sam", age="21", msg="hello")
