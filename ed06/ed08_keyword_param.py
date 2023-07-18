def print_kwargs(**kwargs):
    print(kwargs,type(kwargs))
def main():
    print_kwargs(a=1)  # {'a': 1} <class 'dict'>
    print('-' * 80)
    print_kwargs(name='foo',age=22) # {'name': 'foo', 'age': 22} <class 'dict'>
main()
