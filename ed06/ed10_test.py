def std_weight(height):
    gender = str(input("당신의 성별은 무엇입니까?"))
    if gender == '남자':
        weight = height/100
        weight = weight * weight * 22
        print("남성의 당신의 키:{0}대의 평균 체중은{1}kg입니다".format(height,weight))

    # 남성의 당신의 키999대의 평균 체중은2195.6022kg입니다

    if gender == '여자':
        weight = height/100
        weight = weight * weight * 21
        print("여성의 당신의 키:{0}대의 평균 체중은{1}kg입니다".format(height,weight))

    else:
        print("성별의 똑바로 기입해주세요.")
    # 여성의 당신의 키:999대의 평균 체중은2095.8021kg입니다
def main():
    height = int(input("당신의 키는 몇입니까?"))
    std_weight(height)
main()
