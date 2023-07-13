'''
캐스팅
    정수형 : int()
    실수형 : float()
'''


def main():
    x = 3
    print("{}{}".format(x,type(x)))
    x = "3"
    print("{}{}".format(x, type(x)))
    print("{}|{}|casting:int x:{}".format(x, type(x),type(int(x))))

    x=3.5
    print("{}{}".format(x, type(x)))
    print("{}|{}|casting:int=> x:{} ,type x:{}".format(x, type(x),int(x), type(int(x))))

    print(float("3.5"))
    print(float(3))

main()
