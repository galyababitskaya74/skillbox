
c = 0
x = input('Введите операцию : *, + , - , / ')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if x == '*':
    print(a * b)
elif x == '+':
    print(a + b )   
elif x == '/':
    print(a / b )
elif x == '-':
    print(a - b )
else:
    print('Ошибка ввода')
      