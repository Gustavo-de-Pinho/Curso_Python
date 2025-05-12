#NÚMEROS PRIMOS

#variaveis

#Funções
def primo(numero:int): #Função que verifica se é primo ou não
    Bool = True #Todo número começa sendo considerado primo
    
    for i in range(2, round(numero/2)+1): #For de 2 até metade o número.
        if numero % i == 0: 
            Bool = False #Se a condição dele ser divisivel por algo for atendida, 
            # ele é desconsiderado primo
            
    return Bool
   
def lista_primos(numero:int): #Função que retornará uma lista de primos em um intervalo
    lista = []
    
    for i in range(2, numero+1): #For do 2 até número digitado
        if primo(i): #Função que verifica primo é acionada para cada i do For
            lista.append(i) #Adição a uma lista os números primos.
            
    return lista
    
    
#Esqueleto
numero = int(input("Digite um número: ")) #entrada do usuário

lista = lista_primos(numero) #retorno das funções atribuido a variavel lista

print(lista) #Exibição do resultado