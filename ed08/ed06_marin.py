'''

'''
def attack(name,location,damage):
    print("{0}:{1} 방향 적군을 공격 합니다.[공격력 {2}]".format(name,location,damage))

def main():
    name = '해병'
    hp = 40
    damage = 5

    print("{0} 유닛을 생성합니다.".format(name))
    print("체력{0} , 공격력{1} \n".format(hp,damage))

    tank_name = "퉁퉁이"
    tank_hp = 150
    tank_damage = 35

    print("{0} 유닛을 생성합니다.".format(tank_name))
    print("체력{0} , 공격력{1} \n".format(tank_hp, tank_damage))

    tank2_name = "비실이"
    tank2_hp = 150
    tank2_damage = 35

    print("{0} 유닛을 생성합니다.".format(tank2_name))
    print("체력{0} , 공격력{1} \n".format(tank2_hp, tank2_damage))

    print('-'*80)
    #해병과 탱크가 1시 방향으로 공격하도록
    attack(name,"1시",damage)
    attack(tank_name,"3시",tank_damage)
    attack(tank2_name,"5시",tank2_damage)
main()
