

def calcular_segundo_grau():




    print('F(x) = ax^2 + bx + c')

    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))


    if a == 0:
        x = -c/b
        print(f'A raiz é {x}')


    if  b**2 -4 * a * c < 0:
        print('Não existe raizes reais')

    elif a != 0:

        x1_sg = (-b + (b**2 -4 * a * c)**(1/2)) / (2*a)
        x2_sg = (-b - (b**2 -4 * a * c)**(1/2)) / (2 * a)

        print(f'As raizes são {x1_sg}, {x2_sg}')




