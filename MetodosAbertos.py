import math as ma
from scipy import misc as mi


class MetodosAbertos():

    def __init__(self, funcao, e):
        self.funcao = funcao
        self.e = e

    def newton(self, x):
        i = 0
        parar = False

        if abs(mi.derivative(self.funcao, x)) < 0.1:
            print(mi.derivative(self.funcao, x))
            print("Chute invalido")
            parar = True

        while abs(self.funcao(x)) > self.e:

            if parar:
                break

            x = x - (self.funcao(x) / mi.derivative(self.funcao, x))
            i = i + 1

        print(f"Foi necessario {i} interações " + f"para encontrar a raiz {x}")

    def secante(self, x0, x1):
        i = 0
        loop = False

        if abs(self.funcao(x0)) < self.e:
            print(f"Foi necessario {i} interações " + f"para encontrar a raiz {x0}")
            loop = True
        elif abs(self.funcao(x1)) < self.e:
            print(f"Foi necessario {i} interações " + f"para encontrar a raiz {x1}")
            loop = True

        while True:

            if loop:
                break

            x2 = x1 - ((self.funcao(x1) * (x1 - x0)) / (self.funcao(x1) - self.funcao(x0)))
            i = i + 1

            x0 = x1
            x1 = x2
            if abs(self.funcao(x0)) < self.e:
                print(f"Foi necessario {i} interações " + f"para encontrar a raiz {x0}")
                break
            elif abs(self.funcao(x1)) < self.e:
                print(f"Foi necessario {i} interações " + f"para encontrar a raiz {x1}")
                break

