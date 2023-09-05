import string
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = pd.read_csv(
    'C:/Users/c3lu/OneDrive/Área de Trabalho/PROGRAMACAO E DEVGAME/Projeto_NLP_analiseDeSentimentos/NLP_analise_de_sentimentos/Dados/base_de_dados.csv', encoding='utf-8')

# Dados do NLTK estão baixados
nltk.download('stopwords')
nltk.download('punkt')

# Função de pré-processamento aprimorada


def preprocess_text(texto):
    # Tokenização das palavras
    tokens = word_tokenize(texto, language='portuguese')
    # Conversão para letras minúsculas e remoção de caracteres não alfanuméricos
    tokens = [word.lower() for word in tokens if word.isalnum()]
    # Remoção de stopwords (palavras comuns que geralmente não contribuem para o significado)
    stop_words = set(stopwords.words('portuguese'))
    tokens = [word for word in tokens if word not in stop_words]
    # Stemming (redução das palavras à sua forma raiz)
    stemmer = RSLPStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    # Recria o texto a partir dos tokens processados
    texto_limpo = " ".join(tokens)
    return texto_limpo


# Aplica o pré-processamento à coluna 'text' do conjunto de dados
data['text'] = data['text'].apply(preprocess_text)

# Divide o conjunto de dados em conjuntos de treinamento e teste
X = data['text']
y = data['sentiment']

# Defina o vetorizador TF-IDF
tfidf_vectorizer = TfidfVectorizer()

# Treinamento de um classificador Naive Bayes com validação cruzada
clf = MultinomialNB()

# Defina uma grade de hiperparâmetros para pesquisa em grade
param_grid = {
    'alpha': [0.1, 0.5, 1.0, 2.0, 5.0],
    'fit_prior': [True, False]
}

# Crie um objeto GridSearchCV
grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy')

# Realize a pesquisa em grade
grid_search.fit(tfidf_vectorizer.fit_transform(X), y)

# Mmelhores hiperparâmetros
best_params = grid_search.best_params_
best_alpha = best_params['alpha']
best_fit_prior = best_params['fit_prior']

# Treinamento do modelo final com todo o conjunto de treinamento usando os melhores hiperparâmetros
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

clf = MultinomialNB(alpha=best_alpha, fit_prior=best_fit_prior)
clf.fit(X_train_tfidf, y_train)

# Previsão do sentimento para um texto inserido pelo usuário
texto_input = input("Digite um texto para análise de sentimentos: ")
texto_input = preprocess_text(texto_input)
texto_input_tfidf = tfidf_vectorizer.transform([texto_input])
sentimento_previsto = clf.predict(texto_input_tfidf)

# Imprime o resultado
print("Sentimento:", sentimento_previsto[0])

# Avaliação do modelo
y_pred = clf.predict(X_test_tfidf)

# Cálculo das métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
confusion = confusion_matrix(y_test, y_pred)

# Exibe as métricas
print("Métricas de Avaliação:")
print(f"Acurácia: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")
print("Matriz de Confusão:")
print(confusion)
