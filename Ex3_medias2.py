n = 0
a = 0
i = 0

while True:
    n = float(raw_input('Digite a nota dos alunos: '))
    if n <0:
        break
    a = n + a
    i = i + 1
    media = a/i

print "A media dos seus alunos eh " + str(media)

# Nota: 1.0
# Comentario: *
