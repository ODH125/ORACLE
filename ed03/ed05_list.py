
def main():
    subway = ['Java','Oracle','Html','CSS','Javascript','Jsp','Spring']
    print(subway)

    subway.append('DJango')
    print(subway)
    print('-' * 50)

    subway.insert(4,'JQuery')
    print(subway)
    print('-' * 50)

    print(subway.pop(5)) # 꺼낸 후에 제거
    print(subway)
    print('-' * 50)

    subway.clear()
    print(subway)




main()
