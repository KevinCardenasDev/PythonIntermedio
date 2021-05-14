
def main():
    my_list = [1, "Hello", True,  4.5]
    my_dict = {"firstname": "Kevin", "lastname":"Cardenas"}

    super_list = [
        {"firstname": "Kevin", "lastname":"Cardenas"},
        {"firstname": "Miguel", "lastname":"Lopez"},
        {"firstname": "Tania", "lastname":"Cardenas"},
        {"firstname": "Bryan", "lastname":"Duque"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for idx in super_list:
        for key, value in idx.items():
            print(key, "-", value)


    for idx in super_list:
        print(idx.items())

    for idx in super_list:
        print(idx["firstname"], "-", idx["lastname"])
if __name__ == "__main__":
    main()