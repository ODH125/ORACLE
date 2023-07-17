
def main():
    temp = int(input('오늘은 기온은 어때?'))
    print(temp,type(temp))

    if temp >= 30:
        print('너무 더워요')
    elif temp >= 10:
        print('활동하기 좋은 날씨입니다.')
    elif 0<= temp < 10:
        print('외투를 입으세요.')
    else:
        print('너무 추워요')

main()
