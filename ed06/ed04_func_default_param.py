def profile(name,age=20,main_lang='자바'):
    print("이름: {0} | 나이: {1} | 주 사용 언어:{2}".format(name,age,main_lang))
def main():
    profile("이상문",22,"파이썬")
    profile("이문상")
    profile("오동훈")
# 이름: 이상문 | 나이: 22 | 주 사용 언어: 파이썬
# 이름: 이문상 | 나이: 20 | 주 사용 언어: 자바
# 이름: 오동훈 | 나이: 20 | 주 사용 언어: 자바


main()
