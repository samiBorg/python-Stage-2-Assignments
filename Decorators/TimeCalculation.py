'''
Write a custome decorator that calculates the execution time of any function
'''


import time


def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time of", func.__name__, ": ", execution_time, "seconds")
        return result
    return wrapper


@calculate_execution_time
def my_function():
    time.sleep(2)


my_function()
