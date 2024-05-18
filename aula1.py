
'''
#mostrar

print(nome_inteiro)
print(numero_real)
print(texto)
print(dado_boleano)

#type 
print(type(texto))
print(type(nome_inteiro))
print(type(numero_real))
print(type(dado_boleano))

#concatenar 

text = type(texto)
inteiro = type(nome_inteiro)
numero = type(numero_real)
boleano = type(dado_boleano)

print('Essa variavel ->',texto,'é do tipo',text)
print('Essa variavel ->',nome_inteiro,'é do tipo',inteiro)
print('Essa variavel ->',numero_real,'é do tipo',numero)
print('Essa variavel ->',dado_boleano,'é do tipo',boleano)

print(f'Essa variavel -> {texto} é do tipo,text')
print(f'Essa variavel -> {nome_inteiro} é do tipo,inteiro')
print(f'Essa variavel -> {numero_real} é do tipo, numero')
print(f'Essa variavel -> {dado_boleano} é do tipo,boleano')
def nome():
    name = 'Iniciar '
    return name
nome = nome()
print(nome)
nome = 'Programa '
print(nome)
print(22*14)
n = 24*5
l = n/5
print(n,'   ',l)


#valor1 = float(input('Valor 1 : '))
#valor2 = float(input('Valor 2:' ))
#operacao = input('Operação = ')
#
#if operacao == '+':
#    print('Soma =', valor1 + valor2)

#elif operacao == '-':
#    print('Subtração =', valor1 - valor2)
#elif operacao == '*':
#    print('Multiplicação =', valor1 * valor2)
#elif operacao == '/':
#    print('Divisão =', valor1 / valor2)
#else :
#    print('Erro')


numeros = [10,2,0,3,6,4,5,91,True,80.8]
print(numeros)
numeros[2] = -69
print(numeros)

lista = [2,447,836,825,4,1]
indice = lista[2]
indice1 = lista[1]
    
print(indice + indice1)
numeros1 = list(range(1,111))
print(numeros1)
numeros2= list(range(1,104,3))
print(numeros2)

print(len(lista))

lista.append(10)
print(lista)

variavel = 'text'

print(list(variavel))

cria_sequencia = list(range(1,101))
print(cria_sequencia)

soma = sum(cria_sequencia)
print(soma)

minimo = min(cria_sequencia)
maximo = max(cria_sequencia)
print(minimo, maximo)

lista3 = [654,346,6416,4612,6415,4561,5641,64]
organizar = sorted(lista3)
print(organizar)
organizar.pop(1)
print(organizar)
organizar.remove(64)
print(organizar)

#tuplas

tupla = (1,4,5,67,3,23,45,3,345)
print(tupla)

print(tupla[3])
print(tupla.count(3))
contar = tupla.count(3)
indice = tupla.index(3)
print(indice,'vezes', contar)
tupla1 = tuple(lista3)
print(tupla1)

maior = max(tupla)
menor = min(tupla)

ordenar = sorted(tupla)
print(maior, menor, ordenar)
tupla4 = (1,2354,34,653,21,651,4,31,561,31615,65)
sorted(tupla4)
a,b,c,d,e,f,g,h,i,j,k = tupla4
print(b + c)
print(sum(tupla4))

#conjutos

nome = {1,5,6,6,56,3,2,16,16,51,52651,651,65,165}
conjunto2 ={1,1,5,6,9,8}
print(nome.union(conjunto2))
inter = nome & conjunto2
print(inter)

diferenca = nome.difference(conjunto2)
print(diferenca)

dicionairo = {
'nome' : 'Pedro' ,
'idade' : 25,
'endereço ' : 'Rua 100',
'curso' : 'Python',
}

print(dicionairo)
print(dicionairo.items)
print(dicionairo.values)

dicionairo['curso'] = 'oratoria'

print(dicionairo)
print(dicionairo.items())
print(dicionairo.get('nome'))

'''
import random 
pedido  =  input('>>')
valor  =  random.randrange(10,150)
dicionario ={'calça': 50.00 , 'camiseta': 45.00, 'meias': 20.00 }
dicionario[pedido] = float(valor)
print('Seu carrinho: ', dicionario)


nome1 = input('Nome do aluno: ')
nota1 = int(input('Nota do aluno: '))
nome2 = input('Nome do aluno: ')
nota2 = int(input('Nota do aluno: '))
nome3 = input('Nome do aluno: ')
nota3 = int(input('Nota do aluno: '))
nome4 = input('Nome do aluno: ')
nota4 = int(input('Nota do aluno: '))



notas = {nota1,nota2,nota3,nota4}
maior = max(notas)
menor = min(notas)








