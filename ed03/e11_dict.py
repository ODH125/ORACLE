
def main():
    cabinet = {'A-3':'이상무', 'B-100':'홍길동'}
    print(cabinet)
    print('-' * 50)

    cabinet['C-3'] = '장마'
    print(cabinet)

    cabinet['B-100'] = '꺽정임'
    print(cabinet)
    print('-' * 50)

    print(cabinet.keys())
    print(cabinet.values())
    print(cabinet.items())
    print('-' * 50)

    cabinet.clear()
    print(cabinet)
main()
