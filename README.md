# Projeto: NLP_analise_de_sentimentos
 
![tel1](https://github.com/CeLo93/NLP_analise_de_sentimentos/assets/92175791/37f9a85b-2cd8-4ac6-a409-8cda42129a43)
<div align="center">
 📸 Imagem 01 - Visão desenvolvimento 📸
</div>

----------

Trabalhar em processamento de linguagem natural pode ser desafiador, especialmente quando se trata da base de dados. É aí que entra o ChatGPT. Neste projeto, a ideia é realizar a análise de sentimentos usando o algoritmo de Naive Bayes. Inicialmente, realizo o pré-processamento de texto, o que é fundamental. Isso inclui a tokenização, conversão para letras minúsculas, remoção de caracteres não alfanuméricos, eliminação de stopwords e aplicação de stemming.

Classificamos os dados em duas colunas: "text" e "sentiment". Basicamente, o sentimento é composto por três categorias: Positivo, Negativo e Neutro. Surpreendentemente, essa é a parte relativamente tranquila.

No entanto, ter uma base de dados que reflita esses sentimentos pode ser um desafio. Existem modelos BERT pré-treinados em português, mas os formatos e especificações podem variar significativamente para cada caso, especialmente quando se trata de classificação em NLP.

É aqui que o ChatGPT se destaca. Integrar a API da OpenAI para geração de respostas, embora o ChatGPT não tenha a funcionalidade de "classificar" sentimentos, não seria uma solução neste caso, pois eu já havia desenvolvido o algoritmo. O único obstáculo era ter uma base de dados para treinamento e teste. Além disso, a API tem [muuitas] limitações na versão gratuita. Portanto, como mostrado no vídeo, cada frase ou texto precisa ser classificado para que o modelo possa aprender com cada "sentimento" positivo, negativo ou neutro. Ele precisa compreender o significado de cada combinação de palavras: "é positivo?", "é negativo?" ou "é neutro?". Isso é muito legal, não é?! Basicamente, ele aprende a interpretar os sentimentos a partir dos diálogos na base de dados.

Agora, você pode estar se perguntando por que o ChatGPT é tão incrível. Bem, criar dados com sentimentos classificados aleatoriamente é praticamente impossível. Sim, eu tentei criar em python, mas mesmo direcionando todas as palavras para serem criadas de acordo com o sentimento que eu queria, a falta de nexo fazia o desempenho despencar drásticamente. Então, o que fez? Mandei o ChatGPT criar. Foram mais de 1000 linhas de texto geradas. Claro, tive que ficar reiniciando, mas valeu a pena. Pense nisso: uma IA criou frases com sentimentos classificados para treinar outra IA a classificar os sentimentos nas entradas das pessoas! Quando pensei por esse lado, minha cabeça 💥 .

Assim, o objetivo final é ter uma base de dados sólida que possa ser aplicada em um contexto de produção, onde a partir de um comentário de um usuário, seja possível classificar esse sentimento e entender sua satisfação em relação a um produto ou analisar comentários em redes sociais sobre algo.

----------

![text](https://github.com/CeLo93/NLP_analise_de_sentimentos/assets/92175791/7aef57a1-e764-47f3-950a-203920ce4bd4)


<div align="center">
 📸 Imagem 02 - Visão Dados 📸
</div>
----------



https://github.com/CeLo93/NLP_analise_de_sentimentos/assets/92175791/a5d05715-a9e4-42b6-a016-9b6e2bb6939e



<div align="center">
 📸 Video 01 
</div>

