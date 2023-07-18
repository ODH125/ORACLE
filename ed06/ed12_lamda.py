
def add(a,b):
    return a+b
add_lam = lambda a,b : a+b
def main():
    result = add(12,14)
    print(result)
    print('-' * 80)
    
    result = add_lam(2,4)
    print(result)


main()
