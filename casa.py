def Medidas (*areatot):
    global casa
    global dic
    result = 0
    result = areatot[1] * areatot[2]
    casa = casa + result
    dic = {'Nome do cômodo': areatot[0], 'Área do cômodo': result}
    lis.append(dic)
    del(dic)
    dic = []


lis = list()
dic = dict()
casa = 0
while True:
    nome = input(f'Insira o nome do cômodo: ')

    c = input(f'Insira o comprimento do(a) {nome}: ')
    while c.isspace() or c.isalpha():
        c = input('O comprimento precisa ser um número, redigite: ')
    c = int(c)

    l = input(f'Insira a largura do(a) {nome}: ')
    while l.isspace() or l.isalpha():
        l = input('A largura precisa ser um número, redigite: ')
    l = int(l)

    Medidas (nome, c, l)

    resp = input('Deseja adicionar mais cômodos (s para sim, outra tecla para sair): ')
    if resp != 's':
        break

dic = {'Área total': casa}
lis.append(dic)
print(lis)

