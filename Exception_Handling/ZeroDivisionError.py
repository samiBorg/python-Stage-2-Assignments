#handle ZeroDivisionError():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
