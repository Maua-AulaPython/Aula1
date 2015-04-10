def eh_retangulo(a,b,c):
    if c < a+b:
        return 'A area do tringulo retangulo eh: ' +str(b*a/2)
    else:
        return 'A, B e C nao formam um triangulo retangulo!'



a = int(raw_input('Digite a dimensao A do primeiro cateto: '))
b = int(raw_input('Digite a dimensao B do segundo cateto: '))
c = int(raw_input('Digite a dimensao C da hipotenuza: '))

while type(a) != int or type(b) != int or type(c) != int or a<0 or b<0 or c <0:
    print('Os numeros devem ser inteiros e positivos!\n\n')
    print '________________________________________________'
    a = int(raw_input('Digite a dimensao A: '))
    b = int(raw_input('Digite a dimensao B: '))
    c = int(raw_input('Digite a dimensao C: '))
    

print eh_retangulo(a,b,c)
