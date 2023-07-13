'''

'''

from random import *  # random모듈의 모든 기능 사용
def main():
    print(random()) # 0 <= ? < 1
    print(random())
    print(random())
    print('-'*50)

    print(random() * 10)
    print(int(random() * 10))
    print(int(random() * 10)+1)
    print('-' * 50)

    print(int(random() * 45)+1)
    print('-' * 50)

    print(randint(0,10)) # 10(끝숫자) 포함
    print(randrange(1,100)) # 100(끝 숫자)는 미포함
    print('-' * 50)

main()
