import random #Importa a biblioteca random
import string #Importa a bibliotecaa string

# def define uma função que recebe um parâmetro length (tamanho da senha)
def generate_password(length):
    
    # Caracteres disponíveis
    letters = string.ascii_letters  # Letras maiúsculas e minúsculas
    digits = string.digits          # Números (0-9)
    symbols = string.punctuation    # Caracteres especiais (!@#$...)

    # Garantir pelo menos um de cada tipo de caractere na senha
    password = [
        random.choice(letters),  # Escolhe uma letra aleatória
        random.choice(digits),   # Escolhe um número aleatório
        random.choice(symbols)   # Escolhe um caractere especial aleatório
    ]

    # Preencher o restante da senha com caracteres aleatórios de qualquer tipo
    all_characters = letters + digits + symbols  # Junta todos os tipos de caracteres
    password += [random.choice(all_characters) for _ in range(length - 3)]  # Adiciona mais caracteres até atingir o tamanho desejado

    # Embaralhar para deixar aleatório
    random.shuffle(password)  # Mistura os caracteres para não ficarem previsíveis

    # Juntar tudo em uma string
    return ''.join(password)  # Retorna a senha gerada como uma string única

# Pedir o tamanho da senha ao usuário, garantindo que seja válido
while True:
    length = int(input("Enter the desired password length (minimum 3): "))  # Solicita o tamanho da senha ao usuário
    if length >= 3:  # Verifica se o tamanho é válido (pelo menos 3 caracteres)
        break  # Sai do loop se o tamanho for válido
    print("Error: Password length must be at least 3. Try again.")  # Exibe mensagem de erro se o valor for inválido

# Exibe a senha gerada
print("Generated password:", generate_password(length))
