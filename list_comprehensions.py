

def main():
    
    squares = []

    # for i in range (1,101):
    #     squares.append(i**2)
    
    # print(squares)


    # for i in range (1,101):
    #     if i % 3 != 0: 
    #         squares.append(i**2)
    
    # print(squares)


    #Example of list comprehensions

    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(squares)


    #Example 2 of list comprenhensions

    new_list = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(new_list)


if __name__ == "__main__":
    main()