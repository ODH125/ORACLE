class BigNumError(Exception): # 사용자 정의 예외 , Exception 상속
    pass

def main():
    print('나누기 전용 계산기 입니다.')
    try:
        num01 = int(input('첫번째 숫자를 입력하세요.>'))
        num02 = int(input('두번째 숫자를 입력하세요.>'))

        if num01 >= 10 or num02 >= 10:
            raise BigNumError

        print('{0}/{1}={2}'.format(num01,num02,(num01/num02)))
    except ValueError as err:
        print('오류 발생!잘못 값을 입력 했습니다.',err)

    except ZeroDivisionError as err:
        print('ZeroDivisionError:',err)

    except BigNumError as err:
        print('BigNumError:',err)

    finally:
        print('계산기를 사용해 주셔서 감사합니다.')

    print('프로그램 종료!')
main()
