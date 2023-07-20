
def main():
    f = open("File01.txt", "w+", encoding="utf8")
    for i in range(10):
        f.write("이것은 줄번호 이다{0}\n".format(i))
    f.close

main()
