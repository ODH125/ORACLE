'''

'''

from random import *  # random모듈의 모든 기능 사용
def main():
    jumin = "990102-1234567"
    # 성별 출력 : jumin[인덱스]
    print(jumin[7])

    #년 출력
    print("년:{}".format(jumin[0:2]))

    # 월 출력
    print("월:{}".format(jumin[2:4]))

    # 일 출력
    print("일:{}".format(jumin[4:6]))

    print('-' * 50,'양수')
    print("주민번호 앞자리:{}".format(jumin[:6]))
    print("주민번호 뒷자리:{}".format(jumin[7:]))

    print('-' * 50,'음수')
    print("주민번호 뒷자리:{}".format(jumin[-7:]))
    print("주민번호 뒷자리:{}".format(jumin[:-8]))



main()
