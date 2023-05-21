#handle TypeError():
    try:
        x = 5 + "10"
    except TypeError as e:
        print("Caught TypeError:", e)
