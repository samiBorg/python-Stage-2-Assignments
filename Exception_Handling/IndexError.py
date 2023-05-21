
#handle IndexError():
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print("Caught IndexError:", e)