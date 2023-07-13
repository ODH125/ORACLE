'''
숫자형: 정수,실수


def main():
    pass

main()
'''

'''
숫자형: 정수,실수
'''

def main():
    # 정수형
    num = 123
    print("num:{0},type={1}".format(num,type(num)))
    print("hggggggggggggggggggggggggggggg")

    # 실수형
    # fNum:1.2,type=<class 'float'>
    fNum = 1.2
    print("fNum:{0},type={1}".format(fNum,type(fNum)))

    fNum = 4.12E10
    # fNum:41200000000.0,type=<class 'float'>
    print("fNum:{0},type={1}".format(fNum, type(fNum)))


    fNum = 4.12E-10
    print("fNum:{0},type={1}".format(fNum,type(fNum)))

    # 8진수(0ctal) 숫자0+알파벳 소문자 o : 0o
main()