from  random import *
class turnoff(Exception):
    def __init__(self,msg):
        self.msg =msg
    def __str__(self):
        return self.msg
def main():
    try:
        save_battery = int(input('베터리 잔량: '))

        if save_battery >= 30:
            print('일반_모드')

        if 5 <= save_battery < 30:
            print('절전_모드')

        if  5 > save_battery:
            raise turnoff("베터리가 부족하여 종료됩니다.")

    except turnoff as err:
        print('turnoff:',err)
main()
