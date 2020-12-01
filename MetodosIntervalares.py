import math as m

class MetodosIntervalares():

    def __init__(self,a,b,e,funcao):
        self.a = a
        self.b = b
        self.funcao = funcao
        self.e = e
        self.resultados = []

    def novoIntervalo(self,fx,Fa,i):
        if (fx * Fa) > 0:
            self.a = self.resultados[i]
        else:
            self.b = self.resultados[i]

    def criterioParada(self, fx, i,Fa):
        loop = ""
        # criterio de parada
        if abs(fx) < self.e:
            loop = (f"Foi necessario {i + 1} tentativas para encontrar a raiz " +
                  f"{self.resultados[i]} " + f"com precisão de {self.e} usando o criterio de parada 1")

        self.novoIntervalo(fx=fx,i=i,Fa=Fa)

        # criterio de parada
        if abs(self.b - self.a) < self.e:
            loop = (f"Foi necessario {i + 1} tentativas para encontrar a raiz " +
                  f"{self.resultados[i]} " + f"com precisão de {self.e} usando o criterio de parada 2")

        # criterio de parada
        if len(self.resultados) > 1:
            if abs(self.resultados[i] - self.resultados[i - 1]) < self.e:
                loop = (f"Foi necessario {i + 1} tentativas para encontrar a raiz " +
                        f"{self.resultados[i]} " + f"com precisão de {self.e} usando o criterio de parada 3")

        return loop

    def falsaPoscicao(self):
        self.resultados = []
        loop = ""
        i = 0
        aInicial = self.a
        bInicial = self.b

        if (self.funcao(self.a)*self.funcao(self.b))>0:
          print("O intervalo não tem raiz")
          loop = "x"

        while loop=="":
            Fa = self.funcao(self.a)
            Fb = self.funcao(self.b)

            x = ((self.b * Fa) - (self.a * Fb)) / (Fa - Fb)

            fx = self.funcao(x)
            self.resultados.append(x)

            loop = self.criterioParada(fx=fx,i=i,Fa=Fa)

            if loop!="":
                print(loop+" com o metodo da Falsa Posição")

            i = i + 1

        self.a = aInicial
        self.b = bInicial

    def bisseccao(self):
        self.resultados = []
        loop = ""
        i = 0
        aInicial = self.a
        bInicial = self.b

        if (self.funcao(self.a)*self.funcao(self.b))>0:
          print("O intervalo não tem raiz")
          loop = "x"


        while loop=="":
            Fa = self.funcao(self.a)

            x = (self.a + self.b)/2

            fx = self.funcao(x)
            self.resultados.append(x)

            loop = self.criterioParada(fx, i, Fa)

            if loop!="":
                print(loop+" com o metodo da Bissecção")

            i = i + 1

        self.a = aInicial
        self.b = bInicial