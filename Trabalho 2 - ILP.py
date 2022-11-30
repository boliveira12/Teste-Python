import csv

#Definição de variáveis:
listaMatriculas = []
listaAlunos = []
listaRespostas = []
listaNotas = []
respostasGeral = []
gabarito = []

#Funções:
def correcao():
    for respostasAluno in listaRespostas:
        nota = 0
        for x in range(len(respostasAluno)):
            if respostasAluno[x] == gabarito[x]:
                nota += 1
        listaNotas.append(nota)
    return listaNotas

#Entradas:
with open("./gabarito.csv") as dado1:
    elemento1 = csv.reader(dado1)
    for x in elemento1:
        gabarito.append(x[0])


with open("./dados.csv") as dado2:
    elemento2 = csv.reader(dado2)
    for x in elemento2:
        listaMatriculas.append(x[0])
        listaAlunos.append(x[1])
        respostasGeral.append(x[2])

#Correção das respostas:
for x in respostasGeral:
    respostas = []
    for y in x:
        if y != ',' and y != ' ':
            respostas.append(y)
    listaRespostas.append(respostas)

listaNotas = correcao()
print(listaAlunos)
print(listaRespostas)
print(listaNotas)
print(gabarito)

#Programa:
print('Dados armazenados!')
print('Função 1: A lista em ordem alfabética dos alunos com o número de matricula e a sua nota.')
print('Função 2: A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota.')
print('Função 3: A lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos aprovados.')
print('Função 4: A lista em ordem decrescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos reprovados.')
print('Função 5: O percentual de aprovação.')
print('Função 6: A nota que teve a maior frequência absoluta.')
print('Função 7: O aluno com a maior nota.')
print('Função 8: O aluno com a menor nota.')
print('Função 9: A media da turma.')

while True:
    adm = int(input('Qual das funções você gostaria de executar? [1 - 9]\n'))

    if adm == 1:
        alunoOrd = sorted(listaAlunos)
        for x in alunoOrd:
            p = listaAlunos.index(x)
            print(x, '-', listaMatriculas[p], '-', listaNotas[p])

    elif adm == 2:
        notasOrd = sorted(listaNotas)
        for x in notasOrd:
            p = listaNotas.index(x)
            print(listaAlunos[x], '-', listaMatriculas[p], '-', x)

    elif adm == 3:
        notasOrd = sorted(listaNotas)
        for x in notasOrd:
            if x >= 7:
                p = listaNotas.index(x)
                print(listaAlunos[x], '-', listaMatriculas[p], '-', x)

    elif adm == 4:
        notasOrd = sorted(listaNotas)
        for x in notasOrd:
            if x < 7:
                p = listaNotas.index(x)
                print(listaAlunos[x], '-', listaMatriculas[p], '-', x)

    elif adm == 5:
        aprovados = 0
        for x in listaNotas:
            if x >= 7:
                aprovados += 1
        aprovacao = (aprovados / len(listaNotas)) * 100
        print('O percentual de aprovados é de: %.1f' % aprovacao, '%.')

    elif adm == 6:
        pass
    
    elif adm == 7:
        maxima = max(listaNotas)
        p = listaNotas.index(maxima)
        print(listaAlunos[p], '-', listaMatriculas[p], '-', maxima)

    elif adm == 8:
        minima = min(listaNotas)
        p = listaNotas.index(minima)
        print(listaAlunos[p], '-', listaMatriculas[p], '-', minima)

    elif adm == 9:
        media = sum(listaNotas) / len(listaNotas)
        print('A média da turma é: %.1f' % media)

#valor inválido:
    else:
        print('O valor inserido é invalido! Insira um valor inteiro na faixa de 1 a 10!')
        continue

#continuação do sistema:
    sis = input('Deseja realizar mais uma função? [S/N]\n').lower()
    if sis == 'n':
        print('Programa finalizado.')
        break
    else:
        continue