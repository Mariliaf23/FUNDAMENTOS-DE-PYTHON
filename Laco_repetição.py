'''nome = ''
while nome != "fim":
    nome = input('Digite seu nome ou "fim" para parar o programa ')
    print(f'Olá {nome}, seja bem vindo ao laço de repetição')
print('Saiu do laço de repetição')'''


'''contador = 0
while contador < 5:
    print(f'o valor de contador é {contador}, vamos rodar o laço novamente')
    contador += 1
print('Saiu do laço de repetição')'''    


'''secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")


# 1. Solicita que o usuário insira o primeiro número
guess = int(input("Digite o número: ")) #Converte o que o usuário digita em um número inteiro para que possamos compará-lo com 777

# 2. Inicia o loop while
while guess != secret_number: #Este laço continuará repetindo enquanto o palpite for diferente do número secreto.
   
    # 3. Se for diferente, imprime a mensagem de erro e pede novo input
    print("Ha ha! Você está preso no meu loop!")
    guess = int(input("Tente novamente: "))

# 4. Se o loop terminou, significa que ele acertou
print(guess)
print("Muito bem, trouxa! Você está livre agora.")'''



secret_number = 777

print(
"""
+================================+

| Bem vindo ao meu jogo, trouxa! |
| Insira um número inteiro       |
| e adivinhe o número que tenho  |
| escolhido para você.           |
| Então, qual é o número secreto?|
+================================+
""")

# Primeiro input fora do loop
guess = int(input("Digite o número: "))

# O loop só entra se o primeiro palpite for errado
while guess != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    # Pede um novo número. Se o usuário digitar 777 aqui, 
    # o loop volta ao topo, a condição vira 'False' e ele sai IMEDIATAMENTE.
    guess = int(input("Tente novamente: "))

# Só executa estas linhas quando o usuário digita 777
print(guess)
print("Muito bem, trouxa! Você está livre agora.")