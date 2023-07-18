def profile(name,age,lang1,lang2,lang3,lnag4,lnag5):
        print("이름: {0} \t 나이: {1}".format(name,age),end=" ")
        print(lang1,lang2,lang3,lnag4,lnag5,sep=" | ")

def profile2(name, age, *language):
        print("이름: {0} \t 나이: {1}".format(name, age),end=" ")
        print(language,type(language))
def main():
    profile("찰리",20,'자바','C','C++','C#','파이썬')
    profile("루시",20,'코틀리','스위프트','','','')
    print('-' * 80)

    profile2('찰리',20,'자바','C','C++','C#','파이썬')
    profile2('루시',20,'코틀리','스위프트')
main()
