
def main():
    with open("class.txt", "w", encoding="utf8") as class_file:
        class_file.write("초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명")

    with open("class.txt", "r", encoding="utf8") as class_file:
        #print(class_file.read(),type(class_file.read()))
        d = class_file.read()
        print("d",d)
        f = d.split()
        print(f)

        for g in f:
            if g.endswith("명"):
                print(g)
            else:
                print(g,end=" ")


main()
