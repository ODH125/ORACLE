

def main():
    print('나누기 전용 계산기 입니다.')
    try:
        nums = []
        nums.append(int(input('첫번째 숫자를 입력하세요.>')))
        nums.append(int(input('두번째 숫자를 입력하세요.>')))
        nums.append(nums[0]/nums[1])

        print('{0}/{1} = {2}'.format(nums[0],nums[1],nums[2]))

    except ValueError:
        print('오류 발생! 잘못 값을 입력 했습니다.')

    except ZeroDivisionError as err:
        print('ZeroDivisionError:', err)

    except Exception as err:
        print(err)
    print('프로그램 종료!')
main()
