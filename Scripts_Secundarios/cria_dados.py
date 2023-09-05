import random

# Listas de palavras agrupadas por contexto
contextos = [
    ["Estou", "indo", "para", "o", "trabalho"],
    ["Hoje", "é", "um", "dia", "comum", "para", "mim"],
    ["Eu", "fiz", "minhas", "tarefas", "diárias"],
    ["A", "rotina", "segue", "seu", "curso"],
    ["Nada", "de", "excepcional", "aconteceu", "hoje"],
    ["Estou", "em", "um", "estado", "neutro"],
    ["O", "pensamento", "é", "inexpressivo", "na",
        "vida", "de", "quem", "está", "neutro"]
]

sentimentos = ["Neutro"]

# Número desejado de exemplos
numero_exemplos = 1000

# Função para gerar uma frase aleatória


def gerar_frase():
    # Escolhe aleatoriamente um contexto
    contexto = random.choice(contextos)
    # Embaralha o contexto para que as palavras apareçam em uma ordem aleatória
    random.shuffle(contexto)
    # Escolhe aleatoriamente o número de palavras a serem usadas (entre 5 e o tamanho do contexto)
    num_palavras = random.randint(1, min(len(contexto), 10))
    # Seleciona as primeiras num_palavras do contexto
    frase = " ".join(contexto[:num_palavras])
    # Deixa a primeira letra em maiúscula e adiciona um ponto no final
    frase = frase.capitalize() + '.'
    return frase


# Gerar exemplos aleatórios
exemplos = []

for _ in range(numero_exemplos):
    frase = gerar_frase()
    sentimento = random.choice(sentimentos)
    exemplo = f'"{frase}",{sentimento}'
    exemplos.append(exemplo)

# Salvar os exemplos em um arquivo CSV
with open("base_de_dados_neutro.csv", "w", newline='', encoding='utf-8') as arquivo:
    arquivo.write("text,sentiment\n")
    for exemplo in exemplos:
        arquivo.write(exemplo + "\n")

print(
    f"Foram gerados {numero_exemplos} exemplos e salvos no arquivo base_de_dados_neutro.csv.")
