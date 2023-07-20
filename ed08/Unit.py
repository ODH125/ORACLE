class Unit:
    def __init__(self,name,hp,damage):
        # 인스턴스 변수 : self.변수명 = 값
        self.name = name  # 인스턴스 변수 name에  전달값 name 할당
        self.hp = hp  # 인스턴스 변수 hp에 전달값 hp 할당
        self.damage = damage  # 인스턴스 변수 damage에 전달값 damage 할당

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력{0} , 공격력{1}".format(self.hp,self.damage))
        print('-'*80)

#  객체 생성 : 객체명 = 클래스명(전달값1,전달값2,...)

marin1 = Unit("해병1",40,5)
marin2 = Unit("해병2",40,5)
tank = Unit("탱크1",150,35)

#전투기 유닛: 공중 유닛, 은폐 불가
stralth1 = Unit("레이스",80,5) #  체력80, 공격력5
print('유닛 이름:{0}, 공격력:{1}'.format(stralth1.name,stralth1.damage))

stralth2 = Unit("레이스2",80,5) #  체력80, 공격력5
#  은폐 기능 추가
#업그레이드한 전투기만 위한 특별한 인스턴스 변수 정의, 은폐 상태
stralth2.cloaking = True
if stralth2.cloaking == True: #은폐 상태
    print("{0}는 현재 은폐 상태 입니다.".format(stralth2.cloaking))

def main():
    pass


main()
