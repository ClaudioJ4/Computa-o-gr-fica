import matplotlib.pyplot as plt
import numpy as np



def desenhar(x1, x2, x3, y1, y2, y3, color):
    plt.plot([55, 70], [90, 50], color='black')
    plt.plot([70, 40], [50, 50], color='black')
    plt.plot([40, 55], [50, 90], color='black')

    plt.plot([x1, x2], [y1, y2], color=color)
    plt.plot([x2, x3], [y2, y3], color=color)
    plt.plot([x3, x1], [y3, y1], color=color)

    plt.axis('equal')
    plt.show()


def escala(x, y, Ex, Ey):
    m1 = np.array([[Ex, 0, 0], [0, Ey, 0], [0, 0, 1]])
    m2 = np.array([[x], [y], [1]])
    m3 = np.matmul(m1, m2)
    a = m3[0]
    b = m3[1]
    c = [a, b]
    return c


def rotacao(x, y, angulo):
    if angulo == 30:
        sen = 0.5
        cos = 1.7320508075/2
    elif angulo == 45:
        sen = 1.414213562/2
        cos = 1.414213562/2
    elif angulo == 60:
        sen = 1.7320508075/2
        cos = 0.5

    m1 = np.array([[cos, -1*(sen), 0], [sen, cos, 0], [0, 0, 1]])
    m2 = np.array([[x], [y], [1]])
    m3 = np.matmul(m1, m2)
    a = m3[0]
    b = m3[1]
    c = [a, b]
    return c


def translacao(x, y, T1, T2):
    m1 = np.array([[1, 0, T1], [0, 1, T2], [0, 0, 1]])
    m2 = np.array([[x], [y], [1]])
    m3 = np.matmul(m1, m2)
    a = m3[0]
    b = m3[1]
    c = [a, b]
    return c


def espelhamentoX(x, y):
    m1 = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m2 = np.array([[x], [y], [1]])
    m3 = np.matmul(m1, m2)
    a = m3[0]
    b = m3[1]
    c = [a, b]
    return c


def arbEscala(x, y, x0, y0, Ex, Ey):
    arbx = x0*(1-Ex)
    arby = y0*(1-Ey)
    m1 = np.array([[Ex, 0, arbx], [0, Ey, arby], [0, 0, 1]])
    m2 = np.array([[x], [y], [1]])
    m3 = np.matmul(m1, m2)
    a = m3[0]
    b = m3[1]
    c = [a, b]
    return c


def arbRotacao(x, y, x0, y0, angulo):
    if angulo == 30:
        sen = 0.5
        cos = 1.7320508075/2
    elif angulo == 45:
        sen = 1.414213562/2
        cos = 1.414213562/2
    elif angulo == 60:
        sen = 1.7320508075/2
        cos = 0.5

    arbx = x0*(1- cos) + y0*sen
    arby = y0*(1- cos) - x0*sen
    m1 = np.array([[cos, -1*(sen), arbx], [sen, cos, arby], [0, 0, 1]])
    m2 = np.array([[x], [y], [1]])
    m3 = np.matmul(m1, m2)
    a = m3[0]
    b = m3[1]
    c = [a, b]
    return c


def alternativaA():
    p1 = escala(55, 90, 2, 2)
    p2 = escala(70, 50, 2, 2)
    p3 = escala(40, 50, 2, 2)
    desenhar(p1[0], p2[0], p3[0], p1[1], p2[1], p3[1], 'red')
    print(p1, "\n________\n",  p2, "\n________\n", p3)




def alternativaB():
    p1 = rotacao(55, 90, 30)
    p2 = rotacao(70, 50, 30)
    p3 = rotacao(40, 50, 30)
    desenhar(p1[0], p2[0], p3[0], p1[1], p2[1], p3[1], 'red')
    print(p1, "\n________\n", p2, "\n________\n", p3)




def alternativaC():
    p1 = translacao(55, 90, -3, 4)
    p2 = translacao(70, 50, -3, 4)
    p3 = translacao(40, 50, -3, 4)
    desenhar(p1[0], p2[0], p3[0], p1[1], p2[1], p3[1], 'red')
    print(p1, "\n________\n", p2, "\n________\n", p3)




def alternativaD():
    p1 = espelhamentoX(55, 90)
    p2 = espelhamentoX(70, 50)
    p3 = espelhamentoX(40, 50)
    desenhar(p1[0], p2[0], p3[0], p1[1], p2[1], p3[1], 'red')
    print(p1, "\n________\n", p2, "\n________\n", p3)




def alternativaE():
    p1 = arbEscala(55, 90, 55, 65, 2, 2)
    p2 = arbEscala(70, 50, 55, 65, 2, 2)
    p3 = arbEscala(40, 50, 55, 65, 2, 2)
    desenhar(p1[0], p2[0], p3[0], p1[1], p2[1], p3[1], 'red')
    print(p1, "\n________\n", p2, "\n________\n", p3)

    p4 = arbRotacao(55, 90, 55, 65, 30)
    p5 = arbRotacao(70, 50, 55, 65, 30)
    p6 = arbRotacao(40, 50, 55, 65, 30)
    desenhar(p4[0], p5[0], p6[0], p4[1], p5[1], p6[1], 'blue')
    print("\n\n", p4, "\n________\n", p5, "\n________\n", p6)




while True:
    print("""
------------------------------------------------------------------------------------------------------------------------
    Digite 1 para obter a resposta da alternativa "a"
    Digite 2 para obter a resposta da alternativa "b"
    Digite 3 para obter a resposta da alternativa "c"
    Digite 4 para obter a resposta da alternativa "d"
    Digite 5 para obter a resposta da alternativa "e"
    Digite 0 para sair
------------------------------------------------------------------------------------------------------------------------    
    """)

    opcao = int(input("O que gostaria de fazer ? : "))

    if opcao == 1:
        alternativaA()

    elif opcao == 2:
        alternativaB()

    elif opcao == 3:
        alternativaC()

    elif opcao == 4:
        alternativaD()

    elif opcao == 5:
        alternativaE()

    elif opcao == 0:
        break
