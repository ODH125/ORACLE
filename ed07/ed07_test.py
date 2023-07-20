
def main():
    for i in range(1,51):
        f = open("{0}주차 주간보고.txt".format(i), "w+", encoding="utf8")
        f.write("- {0}주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :".format(i))
    f.close
main()
