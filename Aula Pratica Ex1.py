import math

def distancia(x,y):
    d = math.sqrt(x**2+y**2)
    return d




x = float(raw_input('Coordenada x: '))
y = float(raw_input('coordenada y: '))

print 'A distancia entre pontos eh ' + str(distancia(x,y))
