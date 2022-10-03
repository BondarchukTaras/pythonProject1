from datetime import datetime
# date = datetime(year=2022, month=9, day=21, hour=19, minute=9, second=55)
# print(date)
# print(type(date))
# print(date.date())
# print(date.time()) #заданий
# print(datetime.now()) # поточна дата/час
# print(datetime.today())
# print(date.isoformat()) #почитати
# #
td = '18.04.1985'
print(type(td))
# d = datetime.strptime(td, '%d.%m.%Y')
# print(d)
# print(type(d))
# print(2023-d.year)
# print(d.year, d.month, d.day)
#
# other = d.replace(month=4, day=1)
# print(other)

# from datetime import datetime, timedelta

# d_now = datetime.now()
# interval = timedelta(weeks=4)
# finish = d_now + interval
# print(finish) #має виконатись через 4 тижні

# birthday = datetime(1985, 4, 18) # кільсть днів з дня народження
# result = datetime.now() - birthday
# print(result)

# import random

# random.seed()
# print(random.random())
# print(random.randint(1,10)) # випадкове число в діапазоні 1-10
# for _ in range(10):
#     print(random.randrange(1, 10), end = ' ')

# a = 'Python'
# a = list(range(1, 37))
# b = random.shuffle(a)
# print(a)

# from decimal import Decimal, getcontext
#
# f = 0.2 + 0.1 + 0.3 - 0.5
# print(f)
#
# test = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
# print(test)
# test1 = Decimal(str(0.2)) + Decimal(str(0.1)) + Decimal(str(0.3)) - Decimal(str(0.5))
# print(test1)
#
# getcontext().prec = 6 # кількість значущих знаків
# precission = Decimal('1') / Decimal('3')
# print(precission)
#
# precission = Decimal('11') / Decimal('3')
# print(precission)

# from decimal import  Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP
#
# # num = Decimal("1.45")
# # print(num.quantize(Decimal("1.0"), rounding=ROUND_HALF_EVEN)) # defolte
# #
# # num = Decimal('1.45')
# # print(num.quantize(Decimal("1.0"), rounding=ROUND_HALF_UP))
#
# precission = Decimal('11') / Decimal('3')
# print(precission)
# r = (Decimal('11') / Decimal('3')).quantize(Decimal(0000))
# print(r)

# from  decimal import  Decimal
# print(Decimal('1.2').compare(Decimal('1.1')))
# print(Decimal('1.2').compare(Decimal('1.2')))
# print(Decimal('1.2').compare(Decimal('1.3')))

# import  math
# print(math.pow(2, 2))
# print(math.sqrt(64))
#
# print(0.1 + 0.2 == 0.3)
# print(math.isclose(0.1 + 0.2, 0.3)) # порівняти

# підрахувати парність скобок ()
# text = '((()))()){{{}}}[]'
# count1 = 0  # (
# count2 = 0  # [
# count3 = 0  # {
# for item in text:
#     if item == '(':
#         count1 += 1
#     elif item in text:
#         item == '['
#     elif item in text:
#         item == '{'
#         count3 += 1
#     elif item == ')':
#         count1 += 1
#     elif item == ']':
#         count2 += 1
#     elif item == '}':
#         count3 += 1
#
# if count1 == 0:
#     print(f"Bracket '()': {True}")
# else:
#     print(f'Bracket "()": {False}')
# if count2 == 0:
#     print(f'Bracket "[]": {True}')
# else:
#     print(f'Bracket "[]": {False}')
# if count3 == 0:
#     print('Bracket {}', True)
# else:
#     print('Bracket {}', False)

