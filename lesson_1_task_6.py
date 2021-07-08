# По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника,
# составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.


a, b, c = map(float, input('Введите через пробел длины сторон для треугольника в см: ').split())

if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b or b == c or a == c:

        if a == b and a == c:
            print('Треугольник равносторонний')

        else:
            print('Треугольник равнобедренный')

    else:
        print('Треугольник разносторонний')

else:
    print('Такого треугольника не существует')
