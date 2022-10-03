# функція
# def is_valie(value):
#     if value is None:
#         print("None")
#     elif value:
#         print("True")
#     else:
#         print("False")
# print(None)
# print(True)
# print(False)
# is_valie(0)
# is_valie(0.0)
# is_valie([])
# is_valie({})
# is_valie(0)
# is_valie(())
# is_valie(set())
# is_valie(3)
# is_valie(-3)
# is_valie("")
# is_valie("+")
# is_valie(" ")

# a=1
# b=2
# c=3
# def temp(a, b, c):
#     print(f'a: {a}')
#     print(f'b: {b}')
#     print(f'c: {c}')
#     #return None
# temp(a, b, c) # print неивикористовувати щоб не виводилось None

# def temp(a, b, c, *args):
#     print(f'a: {a}')
#     print(f'b: {b}')
#     print(f'c: {c}')
#     print(args)
# temp('sdfdsfsd', False, 12, 45, 21, 8, 4, 'fd', True) # переводе в дуплекс

# def temp(a, b, c, **kwargs):
#     print(f'a: {a}')
#     print(f'b: {b}')
#     print(f'c: {c}')
#     print(kwargs)
# temp('sdfdsfsd', False, 12, test_1=45, test_2='aaa', test_3=21, test_4=8, test_5=4, test_6='fd',
#      test_7=True)  # переводе в словник

# lambda - Aнонімні функції
# print((lambda x, y: x + y)(4, 5))
# def add (x, y):
#     return  x+y
# print(add(4,5))

# months = [(1, "January"), (5, 'May'), (4, "April")]
# print(sorted(months, key=lambda x: x[0]))

# {'h': ASCII}
# def convert(string):
#     codes = {}
#     for ch in string:
#         if not ch in codes:
#             codes[ch]=ord(ch)
#     return  codes
# s= input("Please enter str: ")
# print(convert(s))

# чи число є просте
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# def main():
#     value = int(input('Plase enter the number: '))
#     if is_prime(value):
#         print(f'{value} - is prime number')
#     else:
#         print(f'{value} - is not prime number')
# main()

# func(minutes=50, days=1)) => задачка кількість секунд в задоних параметрах
# def to_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):
#     seconds_in_minutes = 60
#     seconds_in_hours = 60 * seconds_in_minutes
#     seconds_in_days = 24 * seconds_in_hours
#     seconds_in_weeks = 7 * seconds_in_days
#
#     return seconds + minutes * seconds_in_minutes + \
#            hours * seconds_in_hours + \
#            days * seconds_in_days + \
#            weeks * seconds_in_weeks
#
#
# print((to_seconds(minutes=50, days=1)))

# def car(model, color):
#     print('My car is a ' + model + ' ' + color)
# car('Volvo', 'red') # позиційні
# car( model='Volvo', color= 'red') # іменовані

# def incremet_values(l):
#     for i in range(len(l)):
#         l[i] +=1
#     print("List inside of function: " + str(l))
# original =[ 1, 2,3]
# incremet_values(original)
# print("List uotside of function: " + str(original))

# def incremet_values(l):
#     l = [4, 5, 6]
#     print("List inside of function: " + str(l))
#
# original = [1, 2, 3]
# incremet_values(original)
# print("List uotside of function: " + str(original))

# def sum_of_s(*args):
#     return_value = 0
#     for num in args:
#        return_value += num**2
#     return return_value
#
# print(sum_of_s(2, 3, 3, 5, 1, 6))

# def build_pet(spesies, name, **pet_info):  # dict
#     pet = {}
#     pet['spesies'] = spesies #
#     pet['name'] = name
#     for key, value in pet_info.items():
#         pet[key] = value
#     return pet
#
#
# my_pet = build_pet('Husky', 'Doge', color='White', age=2)
# print(my_pet)


# Tree of size
def print_tree(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2 * i + 1):
            print('*', end='')
        print()


print_tree(10)
