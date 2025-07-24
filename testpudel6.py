while True:
    vopros_input = input('Введіть перше число\n')
    if not vopros_input.isdigit():
        print("Це не число. Спробуйте ще раз.")
        continue
    vopros = int(vopros_input)

    vopros1 = input('Введіть оператора (+,-,*,/)\n')
    if vopros1 not in ['+', '-', '*', '/']:
        print("Невірно. Спробуйте ще раз.")
        continue

    vopros3_input = input('Введіть друге число\n')
    if not vopros3_input.isdigit():
        print("Це не число. Спробуйте ще раз.")
        continue
    vopros3 = int(vopros3_input)

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
    elif otvetfinal == '1':
        break

