string = raw_input('Digite seu texto: ')
i=0
a=''
string2 = []
while i < len(string):
    i = i + 1
    a = str(a) + string[-i]
print a
