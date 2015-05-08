import math

x =float((raw_input('Coordenada x: ')))
y =float((raw_input('Coordenada y: ')))
z =float((raw_input('Coordenada z: ')))


lambida = math.atan2(y,x)

e = 0.00669454185
a = 6378160
h = 0
n = 1
p = math.sqrt(x**2+y**2)
teta = math.atan((z/p)*(1-(e*n/(n+h)))**(-1))

for i in range(5):
    n = a/(math.sqrt(1-(e*math.sin(teta)*math.sin(teta))))
    h = (p/math.cos(teta))-n
    teta = math.atan(z/(p*(1-(e*n/(n+h)))))

teta = math.degrees(teta)
lambida = math.degrees(lambida)
h = h*1000
print 'teta: ' + str(teta)
print 'lambida: ' + str(lambida)
print 'h: ' +str(h)

# Nota: 0.8
# O enunciado pedia para escrever uma função!
