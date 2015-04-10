notas = []
n = 0
a = 0
i = 0

while True:
    try:
        n = float(raw_input('Digite a nota dos alunos: '))
    except:
        print('Numero nao eh valido')
        
    if n <0:
        break
        
    notas.append(n)
    a = n + a
    i = i + 1
    media = a/i

try:
    print "\nA media dos seus alunos eh: " + str(media)
    print 'A nota mais alta eh: ' + str(max(notas))
except:
    print 'Nenhuma nota foi digitada'
