'''
    사칙 연산자
'''
def main():
    x = 3;
    y = 4;
    z = 6;
    print('-' * 45); #문자*숫자: 숫자만큼 반복
    print("{0}+{1}={2}".format(x, y, (x + y)))  #3+4=7
    print("{0}-{1}={2}".format(x, y, (x - y)))  # 3-4=-1
    print("{0}*{1}={2}".format(x, y, (x * y)))  # 3*4=12
    print("{0}/{1}={2}".format(x, y, (x / y)))  # 3/4=0.75
    # ** : x의 y제곱
    print("{0}**{1}={2}".format(x, y, (x ** y)))  # 3**4=81
    print("{0}**{1}={2}".format(x, y, (x % y)))  # 3**4=81
    # // : 나눗셈후의 몫을 반환
    print("{0}//{1}={2}".format(z, y, (z // y)))  # 3**4=81
    print('-' * 45);


main()