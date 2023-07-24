class ThailandPackage:
    def detail(self):
        print('[태국 3박 5일 패키지] 방콕, 파타야 50만원')

print('__name__:{0}'.format(__name__))        
if __name__ == "__main__":  # 모듈에서 직접 실행
    print('ThailandPackage 모듈 직접 실행')
    print('이문장은 모듈을 직접 실행시만 출력됨')
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print('이문장은 외부에서 모듈 실행시 출력됨')