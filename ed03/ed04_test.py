
def main():
    word = "PRACTICE MAKES PERFECT"
    firstword = word[0]
    lowerworld = word[1:]

    print('-' * 50)

    print(firstword)
    print(lowerworld)
    upperword = firstword.upper()
    lowerworld2 = lowerworld.lower()
    print('-' * 50)

    print("{}{}".format(upperword,lowerworld2))
main()
