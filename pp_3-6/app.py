import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

documents = [
    # Positivas
    "o produto é excelente e chegou rápido",
    "gostei muito do atendimento",
    "qualidade superior, recomendo",
    "excelente custo-benefício",
    "produto chegou antes do prazo",
    "serviço muito eficiente e rápido",
    "estou satisfeito com a compra",

    # Negativas
    "não gostei do produto, veio quebrado",
    "atrasou demais a entrega",
    "o atendimento foi ruim e demorado",
    "produto veio com defeito",
    "péssima experiência de compra",
    "produto chegou danificado e sem garantia",
    "não recomendaria esse produto a ninguém",

    # Neutras
    "recebi o pedido ontem",
    "produto está funcionando",
    "a embalagem estava intacta",
    "a cor do produto é azul",
    "o tamanho é o que eu esperava",
    "a compra foi processada com sucesso",
    "envio realizado conforme combinado"
]

labels = [
    1, 1, 1, 1, 1, 1, 1,    # Positivas
    0, 0, 0, 0, 0, 0, 0,    # Negativas
    2, 2, 2, 2, 2, 2, 2     # Neutras
]


# Vetorização TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Separando dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42, stratify=labels)

# Treinando o MLP
clf = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
clf.fit(X_train, y_train)

# Salvando modelo e vetor TF-IDF
with open("modelo_mlp.pkl", "wb") as f:
    pickle.dump((clf, vectorizer), f)

# Carregando modelo salvo
with open("modelo_mlp.pkl", "rb") as f:
    loaded_clf, loaded_vectorizer = pickle.load(f)

# Avaliação
y_pred = loaded_clf.predict(X_test)
print("== Relatório de Classificação ==")
print(classification_report(y_test, y_pred, labels=[0, 1, 2], target_names=["Negativo", "Positivo", "Neutro"]))

# Nova frase para classificação
nova_frase = "excelente superior recomendo"
vetor_novo = loaded_vectorizer.transform([nova_frase])
predicao = loaded_clf.predict(vetor_novo)[0]

rotulos = {0: "Negativa", 1: "Positiva", 2: "Neutra"}
print(f"\nFrase: \"{nova_frase}\"\nClassificação: {rotulos[predicao]}")