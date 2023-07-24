# 사람수에 따른 영화 가격을 계산하는 함수3개를 정의
# 일반, 조조, 군인할인
# 일반
def price(people):
    print('{0}명, 영화표 가격을 {1}원 입니다.'.format(people, people*15000))

def price_morning(people):
    print('{0}명, 영화표 가격을 {1}원 입니다.'.format(people, people*9000))

def price_soldier(people):
    print('{0}명, 영화표 가격을 {1}원 입니다.'.format(people, people*100))

