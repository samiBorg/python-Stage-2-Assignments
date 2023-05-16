from binary_insertion_sort import binary_insertion_sort
from merge_sort import merge_sort
import merge_list


def main():
    list1 = [2, 7, 4, 6, 3, 5, 1]
    list2 = [14, 8, 10, 9, 13, 12, 11]
    print("list 1: {}".format(list1))
    print("list 2: {}".format(list2))
    print("Binary insertion sort on these list1: {}".format(binary_insertion_sort(list1)))
    print("Binary insertion sort on these list2: {}".format(binary_insertion_sort(list2)))

    list1 = [2, 7, 4, 6, 3, 5, 1]
    list2 = [14, 8, 10, 9, 13, 12, 11]

    print("Merge sort on list 1: {}".format(merge_sort(list1)))
    print("Merge sort on list 2: {}".format(merge_sort(list2)))
    list1.sort()
    list2.sort()
    print("Merging the lists!!: {}".format(merge_list.merge(list1, list2)))


if __name__ == "__main__":
    main()
