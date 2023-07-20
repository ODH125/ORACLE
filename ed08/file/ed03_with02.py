
def main():
    # 새로운 txt 파일 생성
    with open("study.txt", "w", encoding="utf8") as study_file:
        study_file.write("파이썬을 열심히 공부하고 있어요.")
    # txt 파일 읽기
    with open("study.txt", "r", encoding="utf8") as study_file:
        print(study_file.read())

    str01 = "스프링,파이썬"
    #split()
    print(str01.split(","))
    str02 = "스프링 파이썬"
    print(str02.split())

    #endwith() 문자열이 어떤 값으로 끝나는지 확인할 때 사용
    str03 = "이 문장은 마침표로 끝나요."
    if str03.endswith("."):
        print(".로 끝났습니다.")
main()
