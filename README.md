# Projeto: NLP_analise_de_sentimentos
 
![text](https://github.com/CeLo93/NLP_analise_de_sentimentos/assets/92175791/b233c530-8d7d-4dd7-b185-1fcd6f687131)

----------

Trabalhar em processamento de linguagem natural pode ser desafiador, especialmente quando se trata da base de dados. É aí que entra o ChatGPT. Neste projeto, a ideia é realizar a análise de sentimentos usando o algoritmo de Naive Bayes. Inicialmente, realizo o pré-processamento de texto, o que é fundamental. Isso inclui a tokenização, conversão para letras minúsculas, remoção de caracteres não alfanuméricos, eliminação de stopwords e aplicação de stemming.

Classificamos os dados em duas colunas: "text" e "sentiment". Basicamente, o sentimento é composto por três categorias: Positivo, Negativo e Neutro. Surpreendentemente, essa é a parte relativamente tranquila.

No entanto, ter uma base de dados que reflita esses sentimentos pode ser um desafio. Existem modelos BERT pré-treinados em português, mas os formatos e especificações podem variar significativamente para cada caso, especialmente quando se trata de classificação em NLP.

É aqui que o ChatGPT se destaca. Integrar a API da OpenAI para geração de respostas, embora o ChatGPT não tenha a funcionalidade de "classificar" sentimentos, não seria uma solução neste caso, pois eu já havia desenvolvido o algoritmo. O único obstáculo era ter uma base de dados para treinamento e teste. Além disso, a API tem [muuitas] limitações na versão gratuita. Portanto, como mostrado no vídeo, cada frase ou texto precisa ser classificado para que o modelo possa aprender com cada "sentimento" positivo, negativo ou neutro. Ele precisa compreender o significado de cada combinação de palavras: "é positivo?", "é negativo?" ou "é neutro?". Isso é muito legal, não é?! Basicamente, ele aprende a interpretar os sentimentos a partir dos diálogos na base de dados.

Agora, você pode estar se perguntando por que o ChatGPT é tão incrível. Bem, criar dados com sentimentos classificados aleatoriamente é praticamente impossível. Sim, eu tentei criar em python, mas mesmo direcionando todas as palavras para serem criadas de acordo com o sentimento que eu queria, a falta de nexo fazia o desempenho despencar drásticamente. Então, o que fez? Mandei o ChatGPT criar. Foram mais de 1000 linhas de texto geradas. Claro, tive que ficar reiniciando, mas valeu a pena. Pense nisso: uma IA criou frases com sentimentos classificados para treinar outra IA a classificar os sentimentos nas entradas das pessoas! Quando pensei por esse lado, minha cabeça 💥 .

Assim, o objetivo final é ter uma base de dados sólida que possa ser aplicada em um contexto de produção, onde a partir de um comentário de um usuário, seja possível classificar esse sentimento e entender sua satisfação em relação a um produto ou analisar comentários em redes sociais sobre algo.

----------

![tel1](https://github.com/CeLo93/NLP_analise_de_sentimentos/assets/92175791/b3debc6f-8d5d-4550-9f37-09f3c4b18d7b)

----------

https://github.com/CeLo93/NLP_analise_de_sentimentos/assets/92175791/d5d64af1-977b-4eb3-b530-2f17ff991fd9


