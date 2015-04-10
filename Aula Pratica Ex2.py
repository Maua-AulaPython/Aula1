import math

def distancia(x,y):
    d = math.sqrt(x**2+y**2)
    return d

x = []
y = []
d = []
n = int(raw_input('Quantidade de pontos: '))
for i in range(n):
    x.append(float(raw_input('Coordenada x: ')))
    y.append(float(raw_input('Coordenada y: ')))
    d.append(distancia(x[i],y[i]))  

print 'A maior distancia entre os pontos digitados eh ' + str(max(d))
