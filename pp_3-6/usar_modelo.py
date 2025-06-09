import pickle

with open("modelo_mlp.pkl", "rb") as f:
    clf, vectorizer = pickle.load(f)

frases = [
    "o atendimento foi ótimo",
    "produto chegou com defeito",
    "não gostei do serviço",
    "a embalagem estava intacta",
    "gostei do produto"
]

vetores = vectorizer.transform(frases)
predicoes = clf.predict(vetores)

rotulos = {0: "Negativa", 1: "Positiva", 2: "Neutra"}

for frase, pred in zip(frases, predicoes):
    print(f'Frase: "{frase}"\nClassificação: {rotulos[pred]}\n')