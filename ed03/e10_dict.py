
def main():
    cabinet = {3:'푸',100:'이상무'}

    print(cabinet[3])
    print(cabinet[100])
    print('-' * 50)

    # 딕셔너리.get(키)
    print(cabinet.get(3))
    # 딕셔너리 없는키
    print(cabinet.get(99,'없어요'))
    print('-' * 50)

    print(3 in cabinet)
    print(99 in cabinet)
main()
