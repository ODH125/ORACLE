class chickenZero(Exception): # 사용자 정의 예외 , Exception 상속
    def __init__(self, msg):
        self.msg = msg

class ordererror(Exception): # 사용자 정의 예외 , Exception 상속
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class soldouterror(Exception): # 사용자 정의 예외 , Exception 상속
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
def main():
    try:

        chicken = 10
        waiting = 1

        while True:
            if chicken == 0:
                raise chickenZero("남은 치킨이 없습니다.\n장사 끝!")

            print("남은 치킨 : {0}".format(chicken))
            order = int(input("치킨을 몇마리 주문하시겠습니까?"))

            if order <= 0:
                raise ordererror("주문 수량이 잘못되었습니다.")

            if order >= 11:
                raise soldouterror("최대 주문 수량은 10마리입니다.")

            if order > chicken:
                print("재료가 부족합니다")

            else:
                print("[대기번호 {0}] {1}마리 주문했습니다.".format(waiting, order))
                waiting += 1
                chicken -= order

    except chickenZero as err:
        print('chickenZero:',err)

    except ordererror as err:
        print('ordererror:',err)

    except soldouterror as err:
        print('soldouterror:',err)

    finally:
        print('남은치킨: {}'.format(chicken))
main()
