'''

'''


def main():
    file01 = open("File01.txt","r",encoding="utf8")
    lines = file01.readlines()
    for line in lines:
        print(line, end="")
    file01.close()


main()
