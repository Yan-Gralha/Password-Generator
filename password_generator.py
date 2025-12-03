import random
import string

def gerar_senha(tamanho):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    senha = [
        random.choice(letras),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    todos = letras + numeros + simbolos
    senha += [random.choice(todos) for _ in range(tamanho - 3)]

    random.shuffle(senha)

    return ''.join(senha)

while True:
    tamanho = int(input("Digite o tamanho desejado para a senha (mínimo 3): "))
    if tamanho >= 3:
        break
    print("Erro: a senha deve ter pelo menos 3 caracteres.")

print("Senha gerada:", gerar_senha(tamanho))
