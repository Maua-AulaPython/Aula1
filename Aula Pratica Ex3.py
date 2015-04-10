import math

def distancia(x,y):
    d = math.sqrt(x**2+y**2)
    return d

def polar(x,y):
    r = distancia(x,y)
    teta = math.atan2(y/x)
    


x = float(raw_input('Coordenada x: '))
y = float(raw_input('Coordenada y: '))

r = distancia (x,y)
teta = math.atan2(y,x)

print 'Coordenada polar:   x = %f*cos(%f)    y = %f*sen(%f)'%(r,teta,r,teta)
