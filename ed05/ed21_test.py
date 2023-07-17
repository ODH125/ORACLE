from random import *
def main():
    total = 0
    for i in range(1,51):
        time = round(random() * 50)
        if 5 <= time <=15 :
            num = 0
            print("[{0}] {1}번째 손님 (소요 시간 : {2}분 )".format(num,i,time))
            total = total + 1

        else:
            num = ' '
            print("[{0}] {1}번째 손님 (소요 시간 : {2}분 )".format(num,i,time))

    print("총 탑승객 : {}".format(total))
main()
