from services.math import roots
from services.math import fibonacci


def main():
    num = int(input("Enter a number to perform square and cube root: "))
    print("The square root is: {}".format(roots.squareRoot(num)))
    print("The cube root is: {}".format(roots.cubeRoot(num)))

    print("Now lets print a Fibonacci Series:")
    end = int(input("Enter the length of series you want: "))
    print("Here is your Fibonacci Series: {}".format(fibonacci.fibonacci_series(end)))


if __name__ == "__main__":
    main()
