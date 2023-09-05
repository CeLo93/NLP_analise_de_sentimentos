import csv

# Dados de exemplo
dados = [
    ["Eu amo esse produto! É incrível.", "Positivo"],
    ["Preciso de alguém que me olhe nos olhos quando falo. Que ouça a minha tristeza, com paciência, e ainda que não compreenda, respeite meus sentimentos. Preciso de alguém amigo o suficiente para dizer-me a verdade, mesmo sabendo, que posso odiá-lo por isso. Que teime em ser leal, simples e justo.", "Negativo"],
    ["O clima hoje está bom.", "Neutro"],
    ["Este filme é maravilhoso.", "Positivo"],
    ["Assim, minha tristeza voltando sempre, e me achando mais perdida aos meus olhos, se eu não tivesse sido condenada para sempre ao esquecimento de todos.", "Negativo"],
    ["O almoço foi aceitável.", "Neutro"],
    ["Doutor Armando seguiu até a esquina para encontrar o filho que chegava da escola, enquanto Maria, sua esposa, preparava o almoço.", "Neutro"],
    ["O pensamento tem poder infinito. Ele mexe com o destino, acompanha a sua vontade.", "Positivo"],
    ["Deposite suas melhores energias em algo que acredite, aceite sentir o que de melhor lhe é oferecido pelo destino. Exercite a delicadeza, a gentileza, o carinho no dizer, a doçura nas palavras, maneire seu tom de voz, trate os outros como um espelho, assim tudo isso regressa a você.", "Positivo"],
    ["Acreditar que a nossa vida não é melhor ou pior do que a de ninguém. Nunca sentir-se maior ou menor, mas igual. Fazer o bem sem olhar à quem e não esperar nada em troca, é uma maneira de encontrar a felicidade.", "Positivo"],
]

# Caminho para o arquivo CSV que você deseja criar
caminho_arquivo_csv = 'meuArquivo.csv'

# Abra o arquivo CSV em modo de escrita com codificação UTF-8
with open(caminho_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    # Escreva os dados no arquivo CSV
    for linha in dados:
        escritor_csv.writerow(linha)

print("Arquivo CSV criado com sucesso!")
