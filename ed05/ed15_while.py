
def main():
    customer = '토르'
    index = 5

    while index >= 1:
        print("{}님, 커피가 준비됐습니다.".format(customer))
        index = index-1
        print("{0}번 남았습니다.".format(index))

        if index == 0:
            print("커피커피")

main()
