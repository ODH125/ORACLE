class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        #$1 안내 문구 출력
        # {} 유닛을 생성하였습니다.
        print('{0} 유닛을 생성하였습니다.'.format(name))


    def move(self,location):
        #$2 출력문 삭제
        # print('[지상 유닛이동]')
        print('{0} : {1} 방향으로 이동합니다.[속도:{2}]'.format(self.name,location,self.speed))

        #$3 damage Unit으로 이동
        def damaged(self, damage):  # damage 만큼 유닛 피해
            # 피해 정보
            # 남은 체력
            # 남은 체력이 0이면 파괴
            print('{0}:{1}만큼 피해를 입었습니다.'.format(self.name, damage))
            self.hp = self.hp - damage
            print('{0}의 남은 체력{1}'.format(self.name, self.hp))

            if self.hp <= 0:
                print('{0}이 파괴되었습니다.'.format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, damage,speed):  # 생성자
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self, location):  # 전달 받은 방향으로 공격
        # 다음 줄 까지 이어쓰기
        print('{0}:{1} 방향의 적군을 공격합니다.[공격력:{2}]' \
        .format(self.name, location, self.damage))

        ''' #$4 여러줄 comment
            def damaged(self, damage):  # damage 만큼 유닛 피해
            # 피해 정보
            # 남은 체력
            # 남은 체력이 0이면 파괴
            print('{0}:{1}만큼 피해를 입었습니다.'.format(self.name, damage))
            self.hp = self.hp - damage
            print('{0}의 남은 체력{1}'.format(self.name, self.hp))

            if self.hp <= 0:
                print('{0}이 파괴되었습니다.'.format(self.name))
        '''
    # 메서드: 첫 번째 인자는 self
class Soldier(AttackUnit):
    #생성자
    def __init__(self):
        #  이름,체력,공격력,이동속도
        AttackUnit.__init__(self,"해병",40,5,1)

    #강화제 : 일정 시간동안 속도,공격력 증가,체력 10감소
    def booster(self):
        if self.hp>10:
            self.hp = self.hp - 10
            # {} 강화제를 사용합니다
            print('{0}가 강화제를 사용합니다.(10HP 감소)'.format(self.name))
        else:
            print('{0}의 체력이 부족합니다)'.format(self.name))


class Tank(AttackUnit):
    # 클래스 변수: 클래스명 바로 밑에 정의, 클래스로 부터 만들어진 모든 객체에 값이 일괗적용됨
    #시즈모드: 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,35,1)
        self.siege_mode = False

    # 시즈 모드 설정
    def set_siege_mode(self):
        if Tank.siege_developed == False:
            return

        if self.siege_mode == False:
            print('{0} : 시즈 모드로 전환합니다.'.format(self.name))
            self.damage = self.damage*2
            self.siege_mode = True

        if self.siege_mode == True:
            print('{0} : 시즈 모드를 해제합니다.'.format(self.name))
            self.damage = self.damage//2
            self.siege_mode = False

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name,location): #유닛 이름, 비행 방향
        print('{0}:{1} 방향으로 날아 갑니다.[속도:{2}]'.format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage,0)
        Flyable.__init__(self,flying_speed)

    def move(self,location): # Unit의 move 메서드를 오버라이딩
        # print("[공중 유닛 이동]")
        self.fly(self.name,location)

class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"전투기",80,20,5)
        self.cloaked = False

    def cloaKing(self):
        if self.cloaked == False:
            print('{0}의 은폐를 가동'.format(self.name))
            self.cloaked = True

        if self.cloaked == True:
            print('{0}의 은폐를 해제'.format(self.name))
            self.cloaked = False



class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        #  Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)
        self.location = location

def game_strat():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('player : Good Game')
    print('[player] 님이 게임에서 퇴장하였습니다.')

def main():
    game_strat()
    sol1 = Soldier()
    sol2 = Soldier()
    sol3 = Soldier()

    tank1 = Tank()
    tank2 = Tank()

    st1 = Stealth()
    print('-' * 80)

    attack_units = []
    attack_units.append(sol1)
    attack_units.append(sol2)
    attack_units.append(sol3)
    attack_units.append(tank1)
    attack_units.append(tank2)
    attack_units.append(st1)

    for unit in attack_units:
        unit.move('1시')
    print('-' * 80)

    Tank.siege_developed = True
    print('[알람] 시즈 모드 개발이 완료 되었습니다.')
    print('-' * 80)

    #하나의 리스트로 관리하는 다른 unit 구분 : isinstance(객체명,클래스)
    for unit in attack_units:
        if isinstance(unit,Soldier): #Soldier의 인스턴스이면 강화제 투여
            unit.booster()
        # if isinstance(unit,Tank):  # Tank의 인스턴스이면 시즈모드 활성화
        #     Tank.set_siege_mode()
        if isinstance(unit,Stealth):  # Stealth 인스턴스이면 클로킹 활성화
            Stealth.cloaKing()
    print('-' * 80)

    for unit in attack_units:
        unit.attack('1시')
# [알림] 새로운 게임을 시작합니다.
# 해병 유닛을 생성하였습니다.
# 해병 유닛을 생성하였습니다.
# 해병 유닛을 생성하였습니다.
# 탱크 유닛을 생성하였습니다.
# 탱크 유닛을 생성하였습니다.
# 전투기 유닛을 생성하였습니다.
main()
