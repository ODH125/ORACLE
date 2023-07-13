'''
숫자형: 진수
'''
'''
def main():
    pass

main()
'''
def main():
    # 8진수(0ctal) 숫자0+알파벳 소문자 o : 0o
    # 16진수(Hex) 숫자0+알파벳 소문자 x : 0x
    num = 0o177
    print("{0}의 자료형은 {1}".format(num,type(num)))

    num = 0xB
    print("{0}의 자료형은 {1}".format(num, type(num)))

main()