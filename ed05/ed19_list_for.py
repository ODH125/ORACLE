
def main():
    data = [1,2,3,4]
    result = []
    for num in data:
        if num % 2 == 0:
            result.append(num*3)
    print(result)
    print('-' * 50)

    data = [1,2,3,4]
    result = [num*3 for num in data if num % 2 ==0]
    print(result)
main()
