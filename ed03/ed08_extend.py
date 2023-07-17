
def main():
    mix_list = ['이상무',True,20,[5,3,2,4,1]]
    print(mix_list)
    print('-' * 50)

    mix_list2 = ['이상무',True,20]
    num_list = [1,3,5,6,2,4]

    num_list.extend(mix_list2)
    print(num_list)
    print(mix_list2)

main()
