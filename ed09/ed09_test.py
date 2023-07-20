class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print('{0}  {1}  {2}  {3}  {4}'.format(self.location,self.house_type,self.deal_type\
        ,self.price,self.completion_year))

print('총 3가지 매물이 있습니다.')
강남 = House('강남','아파트','매매','10억원','2010년')
강남.show_detail()
마포 = House('마포','오피스텔','전세','5억원','2007년')
마포.show_detail()
송파 = House('송파','빌라','월세','500/50만원','2000년')
송파.show_detail()
