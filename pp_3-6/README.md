**PP.3.5.** Considerando um corpus de texto contendo revisões de produtos, selecione algumas revisões que possam ser caracterizadas como positivas, negativas ou neutras. Treine seu modelo de aprendizagem de máquina utilizando o K-Nearest Neighbors (KNN), tendo como base o código-fonte fornecido pelo professor, para que seja capaz de classificar uma determinada revisão informada pelo usuário, diferente daquela que foi utilizada no treinamento do modelo. No seu modelo utilize a modelagem usando bag of words com transformação TFIDF. Salve os dados do seu modelo treinado em um arquivo pickle, recarregue e demonstre a sua utilização para nova classificação (ou seja, para uma revisão que não tenha sido classificada).

**PP. 3.6.** Repita o exercício 3.5 mas utilizando um Multilayer Perceptron (MLP).

Passo a passo da utilização:

1. Ter Python3 instalado no computador
2. Clonar esse repositório
```
git clone https://github.com/gabidsbarbosa/pln.git
```
3. Entrar na pasta desse projeto pelo terminal
```
cd pp_3-6
```
4. Instalar as bibliotecas necessárias para o projeto
```
pip install -r requirements.txt
```
5. Rodar o app.py
```
python app.py
```
6. Para checar mais resultados depois que os arquivos .pkl foram gerados, rodar o arquivo usar_modelo.py
```
python usar_modelo.py
```
l.