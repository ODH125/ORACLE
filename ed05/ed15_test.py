
def main():
    absent = [2, 5]
    no_book = [7]
    for student in range(1,11):
        if student in absent:
            continue
        elif student in no_book:
            break
        print("{}번 학생,책 읽음.".format(student))

main()
