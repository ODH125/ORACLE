'''

'''

from random import *  # random모듈의 모든 기능 사용
def main():
    print('-' * 50)
    print("오프라인 스터디 모임 날짜는 매월 {0}일로 선정됐습니다.".format(randint(4,28)))
    print('-' * 50)

    fdo = 30
    do = (fdo * 9 / 5) + 32
    print('#섭씨 온도가 30도일 때')
    print('섭씨 온도:{0}\n화씨 온도:{1}'.format(fdo,do))

    print('\n#섭씨 온도가 10도일 때')
    fdo = 10
    do = (fdo * 9 / 5) + 32
    print('섭씨 온도:{0}\n화씨 온도:{1}'.format(fdo, do))
    print('-' * 50)


main()
