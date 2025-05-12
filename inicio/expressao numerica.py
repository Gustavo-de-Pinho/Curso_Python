#CALCULADORA
#Variáveis
Bool = True #Variavel booleana para loop while

#Funções
def operador(lista:list): #Função para indentificar o operador na expressão
    if lista[1] == "+":
        variavel = "Soma"
    elif lista[1] == "-":
        variavel = "Subtração"
    elif lista[1] == "*":
        variavel = "Mutiplicação"
    elif lista[1] == "/":
        variavel = "Divisão"
        
    return variavel #Retorno de uma string com o nome por extenso do operador

def resultado(operador:str, lista:list): #Função de calcular expressão
    if operador == "Soma":
        result = int(lista[0]) + int(lista[2])
    elif operador == "Subtração":
        result = int(lista[0]) - int(lista[2])
    elif operador == "Mutiplicação":
        result = int(lista[0]) * int(lista[2])
    elif operador == "Divisão":
        result = int(lista[0]) / int(lista[2])
        
    return result #retorno de um número inteiro

#Esqueleto
print("!!! CALCULADORA !!!")
print("-------------------")
print("Digite uma expressão")
print("ex¹: 2 + 5")
print("ex²: 3 - 2")
print("ex³: 8 / 4")

while Bool: #Loop até que o usuário insira uma expressão válida
    expressao = input()
    if expressao.find(" ") > 0: #É preciso ter espaço 
        Bool = False
    print("Insira espaços ' ' antes do operador e depois")
    
print("-------------------")

lista = expressao.split() #Retirada dos espaços para operações
operador = operador(lista) #Registro do retorno da função que "descobre" o operador
print(f"O primeiro operante é o número {lista[0]}")
print(f"A operação efetuada na expressão é de {operador}")
print(f"O primeiro operante é o número {lista[2]}")
print(f"O resultado é {resultado(operador, lista)}") 