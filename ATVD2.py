import math
import matplotlib.pyplot as plt


def desenha_circulo(raio, centro=(0, 0)):
    x_centro, y_centro = centro

    def circulo(t):
        x = x_centro + raio * math.cos(t)
        y = y_centro + raio * math.sin(t)
        return x, y

    t = [i/50for i in range(0, 360)]

    x = [circulo(i)[0] for i in t]
    y = [circulo(i)[1] for i in t]

    plt.plot(x, y)
    plt.axis('equal')
    plt.show()


def auxliarPM(xc, yc, x, y):
    plt.scatter(xc + x, yc + y, color='black')
    plt.scatter(xc - x, yc + y, color='black')
    plt.scatter(xc + x, yc - y, color='black')
    plt.scatter(xc - x, yc - y, color='black')
    plt.scatter(xc + y, yc + x, color='black')
    plt.scatter(xc - y, yc + x, color='black')
    plt.scatter(xc + y, yc - x, color='black')
    plt.scatter(xc - y, yc - x, color='black')


def pontoMedio(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    auxliarPM(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        auxliarPM(xc, yc, x, y)

    plt.axis('equal')
    plt.show()


def circulo_fill(raio, centro=(0, 0)):
    x_centro, y_centro = centro

    while raio >= 0:
        def circulo(t):
            x = x_centro + raio * math.cos(t)
            y = y_centro + raio * math.sin(t)
            return x, y

        t = [i / 50 for i in range(0, 360)]

        x = [circulo(i)[0] for i in t]
        y = [circulo(i)[1] for i in t]
        plt.plot(x, y, color='black')
        raio = raio -0.1

    plt.axis('equal')
    plt.show()


def elipse_ponto_medio(a, b, xc, yc):
    while a and b > 0:
        x = 0
        y = b
        d1 = (b ** 2) - (a ** 2 * b) + ((a ** 2) / 4)

        while ((a ** 2) * (y - 0.5)) > ((b ** 2) * (x + 1)):
            plt.scatter(xc + x, yc + y, color='black')
            plt.scatter(xc + x, yc - y, color='black')
            plt.scatter(xc - x, yc + y, color='black')
            plt.scatter(xc - x, yc - y, color='black')


            if d1 < 0:
                x += 1
                d1 += (b ** 2) * (2 * x + 3)
            else:
                x += 1
                y -= 1
                d1 += (b ** 2) * (2 * x + 3) + (a ** 2) * (-2 * y + 2)


        d2 = ((b ** 2) * (x + 0.5) ** 2) + ((a ** 2) * (y - 1) ** 2) - (a ** 2) * (b ** 2)

        while y > 0:
            plt.scatter(xc + x, yc + y, color='black')
            plt.scatter(xc + x, yc - y, color='black')
            plt.scatter(xc - x, yc + y, color='black')
            plt.scatter(xc - x, yc - y, color='black')

            if d2 < 0:
                x += 1
                y -= 1
                d2 += (b ** 2) * (2 * x + 2) + (a ** 2) * (-2 * y + 3)
            else:
                y -= 1
                d2 += (a ** 2) * (-2 * y + 3)
        a = a - 2
        b = b - 2

    plt.axis('equal')
    plt.show()




while True:
    print("""
------------------------------------------------------------------------------------------------------------------------
    Digite 1 para obter a resposta da alternativa "i"
    Digite 2 para obter a resposta da alternativa "ii"
    Digite 3 para obter a resposta da alternativa "iii"
    Digite 4 para obter a resposta da alternativa "d"
    Digite 5 para obter a resposta da alternativa "e"
    Digite 0 para sair
------------------------------------------------------------------------------------------------------------------------    
    """)

    opcao = int(input("O que gostaria de fazer ? : "))

    if opcao == 1:
        raio = float(input("Raio do circulo: "))
        xcent = float(input("X do centro: "))
        ycent = float(input("Y do centro: "))
        desenha_circulo(raio, (xcent, ycent))

    elif opcao == 2:
        raio = float(input("Raio do circulo: "))
        xcent = float(input("X do centro: "))
        ycent = float(input("Y do centro: "))
        pontoMedio(xcent, ycent, raio)

    elif opcao == 3:
        raio = float(input("Raio do circulo: "))
        xcent = float(input("X do centro: "))
        ycent = float(input("Y do centro: "))
        circulo_fill(raio, (xcent, ycent))

    elif opcao == 4:
        xaxis = float(input("Eixo X: "))
        yaxis = float(input("Eixo Y: "))
        xcent = float(input("X do centro: "))
        ycent = float(input("Y do centro: "))
        elipse_ponto_medio(xaxis, yaxis, xcent, ycent)

    elif opcao == 5:
        print("a")

    elif opcao == 0:
        break
