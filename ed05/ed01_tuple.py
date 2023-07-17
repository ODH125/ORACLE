
def main():
    menu = ("돈까스","냉모밀","라멘","순대국")
    print(menu[0])
    print(menu[1])
    print('-' * 50)

    name = "이상무"
    age = 22
    hobby = '코딩'

    print(name,age,hobby)
    print('-'*50)

    (name,age,hobby) = ("이상무",22,'코딩')
    print(name,age,hobby)
    print('-' * 50)

    (start,end) = ("용산","춘천")
    print(start,"=>",end)
    (start, end) = (end,start)
    print(start,"=>",end)
main()
