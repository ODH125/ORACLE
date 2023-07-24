class ParkingManager:
    def __init__(self,capacity):
        self.capacity = capacity
        self.count = 0
    def register(self):
        self.count += 1
        if(self.count < self.capacity+1):
            print('차량 신규 등록[{0}/{1}]'.format(self.count,self.capacity))
        else:
            print('더 이상 등록할 수 없습니다.')
car = int(input('최대 주차가능 차량수를 입력하십시오>'))
manager = ParkingManager(car)
for i in range(car+1):
    manager.register()

