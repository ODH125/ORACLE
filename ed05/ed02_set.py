
def main():
    java = {"이상무","홍길동","강백호"}
    python = set(["푸","이요르"])
    print('-' * 50)

    print(java)
    print(python, type(python))
    print(java & python)
    print(java.intersection(python))
    print('-' * 50)
    s2 = set("HELLO")
    print(s2)
    print('-'*50)

    print(java | python)
    print(java.union(python))
    print('-' * 50)

    print(java - python)
    print(java.difference(python))
    print('-' * 50)

    python.add('피글렛')
    print(python)

    java.remove("푸")
    print(java)

main()
