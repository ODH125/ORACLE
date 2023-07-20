'''

'''


def main():
    print("{0}".format(500))
    # 공간 창출
    print("{0: >10}".format(500))
    # 빈공간 b로 채우기
    print("{0:b>10}".format(500))
    # +기호 붙이기
    print("{0: >+10}".format(500))
    print("{0: >-10}".format(500))
    print("{0: >10}".format(-500))

    print("{0:_<10}".format(500))
    print("{0:,}".format(1000000000000000000))
    print("{0:+,}".format(1000000000000000000))
    print("{0:,}".format(-1000000000000000000))
main()
