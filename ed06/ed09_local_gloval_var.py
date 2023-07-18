glasses_value = 10 #3D안경
def rent_return(glasses,people):  # 3D안경을 대여한 관격의 수
    # people = int(input('3D안경을 대여한 관객은 몇명 입니까?'))
    glasses = glasses - people #glasses는 위의 glasses와 다르다
    print('[함수내부] 남은 3D안경 개수:{0}'.format(glasses))
    return glasses
def main():
    print("3D 안경 개수:{0}".format(glasses_value))
    glasses = rent_return(glasses_value,2)
    print("남은 3D안경의 개수:{0}".format(glasses))


main()
