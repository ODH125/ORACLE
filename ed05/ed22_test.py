
def main():
    total = 0
    count = int(input("구매수를 입력하세요"))
    for i in range(1,count+1):
        price = 1000
        print("2+1상품입니다")

        if (i % 3 ==0):
            pass
        else:
            total = total + price
    print("총금액은 {0}입니다".format(total))
main()
