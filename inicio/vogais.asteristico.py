string = input("Digite uma frase: ")
vogais = ["a", "e", "i", "o", "u"]

for vogal in vogais:
    string = string.lower().replace(vogal,"*")
    
print(string)