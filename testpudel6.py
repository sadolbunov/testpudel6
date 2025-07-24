while True:
    try:
        vopros = float(input('Введіть перше число\n'))
    except ValueError:
        print("Це не число. Спробуйте ще раз.")
        continue

    vopros1 = input('Введіть оператора (+,-,*,/)\n')
    if vopros1 not in ['+', '-', '*', '/']:
        print("Невірно. Спробуйте ще раз.")
        continue

    try:
        vopros3 = float(input('Введіть друге число\n'))
    except ValueError:
        print("Це не число. Спробуйте ще раз.")
        continue

    if vopros1 == '+':
        otvet = vopros + vopros3
    elif vopros1 == '-':
        otvet = vopros - vopros3
    elif vopros1 == '*':
        otvet = vopros * vopros3
    elif vopros1 == '/':
        if vopros3 == 0:
            print("На нуль ділити не можна.")
            continue
        otvet = vopros / vopros3
    print('Відповідь =', int(otvet))
    otvetfinal = input('1. Вихід 2. Продовжити\n')
    if otvetfinal == '2':
        continue
    elif otvetfinal =='1':
        break
