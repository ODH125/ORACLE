'''

'''


def main():
    file01 = open("File01.txt","r",encoding="utf8")
    while True:
        line = file01.readline()
        if not line:
            break
        print(line, end = "")
    file01.close()


main()
