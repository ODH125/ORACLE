class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self,location):
        print('[지상 유닛이동]')
        print('{0} : {1} 방향으로 이동합니다.[속도:{2}]'.format(self.name,location,self.speed))
class AttackUnit(Unit):
    def __init__(self, name, hp, damage,speed):  # 생성자
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self, location):  # 전달 받은 방향으로 공격
        # 다음 줄 까지 이어쓰기
        print('{0}:{1} 방향의 적군을 공격합니다.[공격력:{2}]' \
        .format(self.name, location, self.damage))

    # 메서드: 첫 번째 인자는 self
    def damaged(self, damage):  # damage 만큼 유닛 피해
        # 피해 정보
        # 남은 체력
        # 남은 체력이 0이면 파괴
        print('{0}:{1}만큼 피해를 입었습니다.'.format(self.name, damage))
        self.hp = self.hp - damage
        print('{0}의 남은 체력{1}'.format(self.name, self.hp))

        if self.hp <= 0:
            print('{0}이 파괴되었습니다.'.format(self.name))
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
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        #  Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)
        self.location = location


supply_depot=BuildingUnit("보급고",500,"7시")
