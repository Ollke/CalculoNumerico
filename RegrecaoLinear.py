import EquacoesLineares as el

def MMQ(xi,yi):
    XiXi = []
    XiYi = []

    for i in range(0,len(xi)):
        XiXi.append(xi[i]**2)
        XiYi.append(xi[i]*yi[i])

    M = [[sum(XiXi),sum(xi),sum(XiYi)],[sum(xi),len(xi),sum(yi)]]
    x = el.CalculoNumericoLinear(M)
    return x.eliminacaoGauss()


distancia = [2.4,1.5,2.4,1.8,1.8,2.9,1.2,3,1.2]
largura = [2.9,2.1,2.3,2.1,1.8,2.7,1.5,2.9,1.5]
z = MMQ(distancia,largura)

print("\nQuestão 2:\n")
print(f"Coeficiente Angular: {z[0]}")
print(f"Coeficiente Linear: {z[1]}")

f = lambda x: (z[0]*x)+z[1]
print(f"\nLargura mínima com 1.8m: {f(1.8)}")












