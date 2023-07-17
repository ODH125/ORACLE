

def main():
    num_list = [1, 3, 5, 6, 2, 4]
    print(num_list)

    print(num_list[0:2])  # 0<=x<2 , [1, 2]
    print('-' * 50)

    #처음 부터 2까지 출력
    num_01 = num_list[:2]
    print(num_01)

    #2부터 끝까지 출력
    num_02 = num_list[2:]
    print(num_02)
    print('-' * 50)

    num_list = [1, 3, 5, 6,['b','a','c','d'], 2, 4]
    print(num_list)
    print(num_list[4][:2])
    print('-' * 50)

    num_01 = [1,2,3]
    num_02 = [4,5,6]

    print(num_01 + num_02)
    print(num_01 * 3)
    print(len(num_list))
main()
