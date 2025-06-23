# 🧠 Sumarização Abstrativa de Textos em Português

## 📋 Descrição do Projeto

Este projeto implementa um sistema de **sumarização abstrativa** para textos em português brasileiro, utilizando modelos Transformer pré-treinados da biblioteca **Hugging Face**. A sumarização abstrativa busca **gerar um novo texto**, com linguagem própria e criativa, mantendo o sentido e as informações centrais do conteúdo original.

## 🎯 Objetivos

- Implementar sumarização abstrativa real em português
- Adaptar código base para uso multilíngue com foco no idioma português
- Utilizar modelos pré-treinados com fine-tuning real para sumarização
- Processar textos de até 500 palavras
- Gerar sumários com cerca de 50% do tamanho original, mantendo coesão

## 🔧 Tecnologias Utilizadas

### 🧠 Modelos de IA
- [`csebuetnlp/mT5_multilingual_XLSum`](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum): modelo com fine-tuning real para sumarização de notícias em português e outros idiomas.
- Modelos alternativos testados (fallbacks):
  - `unicamp-dl/ptt5-base-portuguese-vocab`
  - `pierreguillou/t5-base-pt-br-summarization`
  - `google/mt5-base`
  - `facebook/mbart-large-50-many-to-many-mmt`

### 📚 Bibliotecas Python

```python
torch>=1.9.0
transformers>=4.21.0
sentencepiece>=0.1.97
```

## 📖 Fundamentação Teórica

### Técnicas de Sumarização

- **Extrativa**: copia trechos literais do texto original
- **Abstrativa**: reescreve com novas palavras, gerando um texto mais fluido e natural

### Modelos Transformer

A arquitetura Transformer revolucionou o NLP com:
- Atenção multi-head
- Paralelismo eficiente
- Capacidade de lidar com contexto longo

### Modelo Utilizado: `mT5_XLSum`

- Modelo `mT5` com fine-tuning para sumarização em mais de 40 idiomas
- Treinado com dados do **BBC News XLSum**
- Capaz de produzir resumos **naturais, coesos e criativos**

## 🚀 Como Executar

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar ambiente virtual 

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o código

```bash
python app.py
```

## ⚙️ Funcionalidades

- Interface em linha de comando
- Geração de sumário com controle de temperatura, top-k, top-p
- Comparação de diferentes versões do sumário
- Análise de qualidade do sumário:
  - Overlap lexical
  - Cobertura do texto original
  - Grau de abstração
- Redução percentual do texto original

## 📊 Exemplo de Resultado

### Texto Original (400 palavras)

> Texto sobre Inteligência Artificial com foco em aplicações e implicações éticas...

### Sumário Gerado (180 palavras)

> A IA transforma a sociedade ao permitir que máquinas executem tarefas humanas, como reconhecimento e decisões. Impulsionada por dados e algoritmos, ela já atua em saúde, finanças e entretenimento. Apesar dos avanços, levanta questões éticas como viés e desemprego. O desafio é equilibrar inovação e responsabilidade.

## 📽️ Demonstração em Vídeo

📹 [YouTube](https://youtu.be/4fzwEhTFcNM)

## 📂 Estrutura do Projeto

```
pln/
├── summarization/
│   ├── app.py              # Código principal com execução e análise
│   ├── README.md           # Documentação
│   └── requirements.txt    # Dependências
```

## 🔗 Referências

1. **Código Base Original**: [fabriciogmc/natural_language_processing](https://github.com/fabriciogmc/natural_language_processing/blob/main/python/nlp_summarization/abstractive_summarization_bart_en.py)
2. **XLSum Dataset**: Hasan et al. (2021). XLSum: A Cross-Lingual Abstractive Summarization Dataset.
3. **PTT5**: Carmo, D. et al. (2020). Pretraining and validating the T5 model on Brazilian Portuguese data.
4. **Transformers Library**: [Hugging Face](https://huggingface.co/transformers/)