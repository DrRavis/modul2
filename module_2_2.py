first = input('Введи первое число: ')
second = input('Введи второе число: ')
third = input('Введи третье число: ')
if first == second == third:
    print(3)
elif first == second or second==third or first==third:
    print(2)
else:
    print(0)
