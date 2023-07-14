'''

'''

from random import *  # random모듈의 모든 기능 사용
def main():
    print('-' * 50)
    python = 'Python is Amazing'

    print(python.lower())
    print(python.upper())
    print(python[1:3].islower())

    #python을 자바로 변경

    print(python.replace("Python","Java"))
    print('-'*50)

    print(python)
    find = python.find('n')
    print(find)

    find = python.find('n',find+1)
    print(find)

    find = python.find('java')
    print(find)
    print('-' * 50)

    index = python.index("n")
    print(index)

    index = python.index("n", index+1)
    print(index)

    index=python.index("n",2,6)
    print(index)

    # index=python.index("spring")
    # print(index)
    print('-' * 50)

    print(python.count("n"))
    print(python.count("G"))


main()
