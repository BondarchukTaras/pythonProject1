# if name =='Petro':
#     print(f'Hello {name}')
# elif name == 'John':
#     print('Hello John')
# else:
#     print('Hello, man')


while True:
    a = input()
    try:
        a = float(a)
        if a < 10:
            continue
        elif a > 100:
            break
    except Exception:
        continue
    print(a)


# Напишіть програму, яка зчитує з клавіатури два числа a та b,
# рахує та виводить в консоль середнє арифметичне всіх чисел з відрізка [a; b],
# які кратні числу 3


# a = int(input('a: '))
# b = int(input('b: '))
# s, c = 0, 0
# for item in range(a, b + 1):
#     if item % 3 ==0:
#         s += item
#         c += 1
#     item += 1
# print(s / c)

# if 1 = 1:
#     print('T')
# else:
#     print("f")
n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue
print(n)