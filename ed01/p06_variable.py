'''

'''


def main():
    name = "연탄이"
    animal = '개'
    age = 4  # TypeError: can only concatenate str (not "int") to str
    is_male = True

    print("반려동물을 소개해 주세요.")
    print("우리 집 반려동물은 "+animal+"인데, 이름이 "+name+"예요.")
    print(""+name+"는 "+str(age)+" 살이고, 산책을 아주 좋아해요.")
    print(""+name+"는 수컷인가요? ")
    print(""+str(is_male)+".")
main()
