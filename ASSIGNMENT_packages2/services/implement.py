from services.math import roots
from services.sorting import merge_sort


def main():
    arr = []
    for i in range(5):
        arr.append(int(input("Enter elements upto 5: ")))

    arr_sq = []
    for i in arr:
        arr_sq.append(roots.squareRoot(i))

    print("squared elements in the list: {}".format(arr_sq))

    print("Merge sort on the squared list: {}".format(merge_sort.merge_sort(arr_sq)))


if __name__ == "__main__":
    main()
