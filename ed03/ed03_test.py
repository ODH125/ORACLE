
def main():
    url = 'http://google.com'
    http = url.find('/')
    http2 = url[http+2:]

    mainhome = http2.find('.')
    mainhome2 = http2[:mainhome]

    password = mainhome2[:3]
    password2 = len(mainhome2)
    password3 = mainhome2.count("e")

    print(http)
    print(http2)
    print('-'*50)
    print(mainhome)
    print(mainhome2)
    print('-' * 50)
    print("{}{}{}".format(password,password2,password3))

main()
