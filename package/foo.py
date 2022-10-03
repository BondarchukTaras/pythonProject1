def foo(name: str) -> str:
    return f'Hello: {name}'


# щоб в main не друкувало
print(('*' * 100))
if __name__ == '__main__': #foo
    print(foo('Igor'))
