string = input("Digite um conjunto de palavras separando por espaços: ")
string = string.lower().split()

for palavra in string:
    if palavra == palavra[::-1]:
        print(f"A palavra {palavra} é um anagrama!")
    else:
        print(f"A palavra {palavra} não é um anagrama!")
        print(f"Porque {palavra} é diferente de {palavra[::-1]}")