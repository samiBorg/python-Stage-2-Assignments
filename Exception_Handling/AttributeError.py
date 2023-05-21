#handle AttributeError():
    try:
        person = {"name": "John"}
        print(person.age)
    except AttributeError as e:
        print("Caught AttributeError:", e)