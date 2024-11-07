number = int(input('Число для ввода: '))
result = ''
for a in range(1, 20):
    for b in range(2, 20):
        sum = a + b
        if number % sum == 0 and a < b:
            result = result + str(a) + str(b)
        else:
            continue
print(result)
# check = input('Для проверки: ')
# if check == result:
#    print('Всё правильно!')
# else:
#    print('Где-то ошибка')
