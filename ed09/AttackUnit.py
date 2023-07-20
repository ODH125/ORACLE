
class AttackUnit:

    def __init__(self,name,hp,damage): # 생성자
        self.name = name # self.name 인스턴스 변수
        self.hp = hp
        self.damage = damage

    def attack(self,location): # 전달 받은 방향으로 공격
                                                        # 다음 줄 까지 이어쓰기
        print('{0}:{1} 방향의 적군을 공격합니다.[공격력:{2}]'\
              .format(self.name,location,self.damage))

    # 메서드: 첫 번째 인자는 self
    def damaged(self,damage): #damage 만큼 유닛 피해
        # 피해 정보
        # 남은 체력
        # 남은 체력이 0이면 파괴
        print('{0}:{1}만큼 피해를 입었습니다.'.format(self.name,damage))
        self.hp = self.hp - damage
        print('{0}의 남은 체력{1}'.format(self.name,self.hp))

        if self.hp <= 0:
            print('{0}이 파괴되었습니다.'.format(self.name))

# 공격유닛 생성: 화염방사병 유닛, 5시방향으로 공격
flamethrower1 = AttackUnit('빨간바지',50,16) # 객체 생성: 체력50, 공:16
flamethrower1.attack("5시")
flamethrower1.damaged(50)