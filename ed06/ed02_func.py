'''

'''
def open_account():
    print("새로운 계좌를 개설합니다.")

def deposit(balance, money):  # 입금 처리
    print("{0}원을 입금했습니다. 잔액은{1}원 입니다.".format(money,balance+money))
    return balance+money  # 입금 후 잔액 정보 반환
def withdraw(balance,money):  # 출금 금액
    if balance >= money:  # 잔액이 출금 금액보다 많으면
        print("{0}원을 출금 했습니다.잔액은 {1}원 입니다.".format(money,balance-money))
        return balance-money #출금후 잔액 반환
    else:
        print("잔액이 부족합니다.현재 남은 잔액은{0}원 입니다".format(balance))
        return balance
def main():
    open_account()

    balance = 0  # 초기 잔액
    print("입금 이전 잔액 {0}".format(balance))
    balance = deposit(balance,1000)  # 1000원 입금
    print("입금 이후 잔액 {0}".format(balance))

    print("출금 이전 잔액 {0}".format(balance))
    balance = withdraw(balance, 2000)# 1000원 입금
    print("출금 이후 잔액 {0}".format(balance))

main()
