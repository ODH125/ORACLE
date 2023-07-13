'''
Bool : 참(True)/거짓(False)
'''


def main():
    print('-'*45)
    x = True
    y = False

    print("{}{}".format(x,type(x)))
    print("{}{}".format(y, type(y)))

    print(5 > 10)
    print(5 < 10)
    print('-' * 45)

    #not연산자 : True => False , False => True
    print("x:{} | x type:{} | not x :{}".format(x,type(x),(not x)))
    print("y:{} | y type:{} | not y :{}".format(y,type(y),(not y)))
    print('-' * 45)

main()
