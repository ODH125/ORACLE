

def main():
    print('나누기 전용 계산기 입니다.')
    try:
        num01 = int(input('첫번째 숫자를 입력하세요.>'))
        num02 = int(input('두번째 숫자를 입력하세요.>'))

        print('{0}/{1}={2}'.format(num01,num02,(num01/num02)))
    except ValueError:
        print('오류 발생!잘못 값을 입력 했습니다.')

    except ZeroDivisionError as err:
        print('ZeroDivisionError:', err)

    print('프로그램 종료!')
main()
