while True:
    try:
        age = input('How old are you? >>> ')
        age = int(age)
        if age >= 18:
            print('Access allowed')
            break
        else:
            print("Access denied")
            break
    except ValueError:
        print(f"{age} is not a number. Please write a number!")