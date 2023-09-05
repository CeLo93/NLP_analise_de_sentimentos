from textblob import TextBlob

# Texto de entrada
texto = "i'm in home today."

# Criar um objeto TextBlob com o texto
blob = TextBlob(texto)

# Obter a polaridade do sentimento (-1 a 1, onde -1 é negativo, 0 é neutro e 1 é positivo)
polaridade = blob.sentiment.polarity

# Mapear a polaridade para rótulos
if polaridade > 0:
    sentimento_final = "Positivo"
elif polaridade < 0:
    sentimento_final = "Negativo"
else:
    sentimento_final = "Neutro"

# Imprimir o resultado
print(f"Sentimento: {sentimento_final}")
