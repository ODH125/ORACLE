'''
문자열
'''


def main():
    print('-' * 45);
    print('풍선')  # 풍선
    print("나비")  # 나비
    print("나비"*5)  # 나비나비나비나비나비
    print("10")
    print("10'20")
    print('-' * 45);

    #이스케이프 코드 : \'
    # print('I don't want to go to school.') xxx
    print('I don\'t want to go to school.')
    print('-' * 45);

    # 여러 줄인 문자열을 변수에 대입하고 싶을때
    # 이스케이프 코드 : \n
    multiline = "Life is too short\nYou need python"
    print(multiline)
    # Life is too short
    # You need python
    print('-' * 45);

    multiline = '''
    Life is too short
    You need python
    '''
    print(multiline)
    print('-' * 45);
main()
