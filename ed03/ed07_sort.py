
def main():
    num_list = [5,2,4,3,1]
    num_list.sort()
    print(num_list)
    print('-' * 50)

    num_list.sort(reverse=True)
    print(num_list)
    print('-' * 50)

    num_list.reverse()
    print(num_list)
    print('-' * 50)

    my_list = [1,3,2]
    mys_list = my_list.sort()
    print(my_list)
    print('-' * 50)

    your_list = [1,5,6,3,2,4]
    you_list = sorted(your_list)
    print(your_list)
    print(you_list)


main()
