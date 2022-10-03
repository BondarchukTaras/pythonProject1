# from package import foo
# print(foo.foo('David'))

# varivant 1 без інформації в info

# from package.foo import foo
# from package.baz.operation import minus, division
# from package.bar.info import log
# print(foo('David'))
# print(minus(35, 5))
# print(division(44, 11))
# log('Hi friend')


# variant 2.1 з інформацією в info
# from package import foo, minus, division, log
# print(foo('David'))
# print(minus(35, 5))
# print(division(44, 11))
# log('Hi friend')

# variant 2.2 з інформацією в info
# import package
# print(package.foo('David'))
# print(package.minus(35, 5))
# print(package.division(44, 11))
# package.log('Hi friend')

# variant 3 з інформацією в info і зміною назви
# import package as my_import
# print((my_import.foo('Devid')))
# print(my_import.minus(35, 5))
# print(my_import.division(44, 11))
# my_import.log('Hi friend')
# print((my_import.another_foo()))

# variant 4 з інформацією в info
# import package
#
#
# def division(x):
#     return x / 3
#
#
# print(package.foo('David'))
# print(package.minus(35, 5))
# print(package.division(44, 11))
# package.log('Hi friend')
# print(package.another_foo())
# print((division(30)))

# variant 5 з інформацією в info
from package import *


def division_second(x):
    return x / 3


if __name__ == '__main__':
    print(foo('David'))
    print(minus(35, 5))
    print(division(44, 11))
    log('Hi friend')
    print(another_foo())
    print((division_second(30)))
