
def main():
    menu = {'아이스 아메리카노','모히토','수박주스'}
    print(menu,type(menu))

    menu = list(menu)
    print(menu,type(menu))

    menu = tuple(menu)
    print(menu, type(menu))

    menu = set(menu)
    print(menu, type(menu))
main()
