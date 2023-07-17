'''

'''


def main():
    print("나는 {}살 입니다".format(22))
    print("나는 {}를 좋아 합니다.".format("딸기"))

    print("나는 {0}색과 {1}색을 좋아합니다".format("빨강","흰"))
    # print("문자열{이름1}문자열{이름2}...".format("이름1=값","이름2=값"))
    print("나는{age}살이며,{color}색을 좋아합니다".format(age=22,color="빨강"))
    age =22
    color = "파랑"
    print(f"나는 {age}살이며, {color}색을 좋아해요")

main()