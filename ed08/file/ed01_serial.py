import pickle


def main():
    profile_file = open('profile.pickle', 'wb')
    profile = {"이름":"스누피","나이":22,"취미":["자전거","골프","코딩"]}
    print(profile)

    # pickle : 파일에 저장
    pickle.dump(profile,profile_file) #profile 데이터를 파일에 저장
    print('-'*80)
    profile_file = open('profile.pickle', 'rb')

    profile = pickle.load(profile_file)
    print(profile)

    profile_file.close


main()
