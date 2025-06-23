import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, BartForConditionalGeneration, BartTokenizer
import warnings
import re
warnings.filterwarnings("ignore")

def contar_palavras(texto):
    return len(texto.split())

def carregar_modelo_ptbr():
    print("Carregando modelo para português...")

    modelos_ptbr = [
        "unicamp-dl/ptt5-base-portuguese-vocab",
        "pierreguillou/t5-base-pt-br-summarization",
        "google/mt5-base",
        "facebook/mbart-large-50-many-to-many-mmt"
    ]

    for modelo_name in modelos_ptbr:
        try:
            print(f"Tentando carregar: {modelo_name}")

            if "t5" in modelo_name.lower() or "mt5" in modelo_name.lower():
                tokenizer = T5Tokenizer.from_pretrained(modelo_name)
                model = T5ForConditionalGeneration.from_pretrained(modelo_name)
            elif "bart" in modelo_name.lower() or "mbart" in modelo_name.lower():
                tokenizer = BartTokenizer.from_pretrained(modelo_name)
                model = BartForConditionalGeneration.from_pretrained(modelo_name)

            print(f"✓ Modelo {modelo_name} carregado com sucesso!")
            return tokenizer, model, modelo_name

        except Exception as e:
            print(f"❌ Erro com {modelo_name}: {e}")
            continue

    raise Exception("Não foi possível carregar nenhum modelo")

def preprocessar_texto(texto):
    texto = re.sub(r'\n+', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto)
    texto = re.sub(r'[^\w\s\.,;:!?()-]', '', texto)
    return texto.strip()

def pos_processar_sumario(sumario, texto_original):
    prefixos_remover = ["resuma:", "sumário:", "resumo:", "sumarize:", "texto:"]
    for prefixo in prefixos_remover:
        if sumario.lower().startswith(prefixo):
            sumario = sumario[len(prefixo):].strip()

    if sumario:
        sumario = sumario[0].upper() + sumario[1:]

    if sumario and not sumario.endswith(('.', '!', '?')):
        sumario += '.'

    palavras_originais = set(texto_original.lower().split())
    palavras_sumario = sumario.lower().split()

    overlap = len(set(palavras_sumario) & palavras_originais) / len(set(palavras_sumario))
    if overlap > 0.8:
        print("⚠️ Sumário muito similar ao original (possível extração)")

    return sumario

def sumarizar_abstrativo(texto, tokenizer, model, modelo_name, max_length=180, min_length=40):
    texto_limpo = preprocessar_texto(texto)

    if "t5" in modelo_name.lower():
        texto_preparado = (
            "Leia o texto a seguir e produza um resumo criativo, reescrevendo com suas próprias palavras. "
            "Evite copiar frases diretamente. Concentre-se nas ideias principais e em como a IA afeta a sociedade. "
            f"Texto: {texto_limpo}"
        )
    elif "bart" in modelo_name.lower():
        texto_preparado = texto_limpo
    else:
        texto_preparado = f"Sumário: {texto_limpo}"

    inputs = tokenizer.encode(
        texto_preparado,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    with torch.no_grad():
        summary_ids = model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            temperature=0.8,
            top_k=50,
            top_p=0.9,
            do_sample=True,
            num_beams=6,
            length_penalty=1.0,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3,
            early_stopping=False,
            eos_token_id=tokenizer.eos_token_id
        )

    sumario = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    sumario = pos_processar_sumario(sumario, texto_preparado)
    return sumario

def avaliar_qualidade_sumario(texto_original, sumario):
    palavras_original = set(texto_original.lower().split())
    palavras_sumario = set(sumario.lower().split())

    overlap_lexical = len(palavras_original & palavras_sumario) / len(palavras_sumario)
    cobertura = len(palavras_original & palavras_sumario) / len(palavras_original)
    nivel_abstracao = 1 - overlap_lexical

    print(f"\n📊 ANÁLISE DE QUALIDADE:")
    print(f"   Overlap lexical: {overlap_lexical:.2%}")
    print(f"   Cobertura do original: {cobertura:.2%}")
    print(f"   Nível de abstração: {nivel_abstracao:.2%}")

    if nivel_abstracao > 0.4:
        print("   ✓ Sumário com boa abstração")
    elif nivel_abstracao > 0.2:
        print("   ⚠️ Sumário moderadamente abstrativo")
    else:
        print("   ❌ Sumário muito extrativo")

    return {
        'overlap': overlap_lexical,
        'cobertura': cobertura,
        'abstracao': nivel_abstracao
    }

def main():
    print("SUMARIZAÇÃO ABSTRATIVA AVANÇADA - PORTUGUÊS")

    try:
        tokenizer, model, modelo_name = carregar_modelo_ptbr()
        print(f"✓ Usando modelo: {modelo_name}")

        texto_original = """
        A Inteligência Artificial (IA) representa uma das maiores transformações tecnológicas do século XXI. Ela se refere à capacidade de máquinas e sistemas computacionais de realizar tarefas que normalmente exigiriam inteligência humana, como reconhecimento de padrões, tomada de decisões, processamento de linguagem natural, aprendizado e adaptação. Seu desenvolvimento tem sido impulsionado por avanços em algoritmos, poder computacional e disponibilidade massiva de dados.

        Um dos ramos mais importantes da IA é o machine learning (aprendizado de máquina), no qual os sistemas são treinados a partir de grandes volumes de dados para identificar padrões e fazer previsões ou tomar decisões com base neles. O aprendizado profundo (deep learning), por sua vez, é uma subárea que utiliza redes neurais artificiais para resolver problemas complexos, como reconhecimento facial, tradução automática e diagnósticos médicos.

        A IA já está presente em diversas áreas do nosso cotidiano. Nos smartphones, ela auxilia na digitação preditiva, no reconhecimento de voz e na organização de fotos. Em serviços de streaming, algoritmos de IA recomendam músicas, filmes e séries com base nos hábitos dos usuários. No setor financeiro, a tecnologia é usada para detectar fraudes e automatizar investimentos. Na saúde, algoritmos ajudam no diagnóstico precoce de doenças, como câncer e Alzheimer, aumentando as chances de tratamento eficaz.

        Apesar dos benefícios, a IA também levanta preocupações éticas e sociais. O uso de algoritmos pode reforçar preconceitos existentes, se forem treinados com dados enviesados. Além disso, há o receio de substituição de empregos humanos por máquinas, o que exige uma requalificação da força de trabalho. A discussão sobre a regulação e uso responsável da IA tem se intensificado, buscando garantir transparência, privacidade e justiça.

        Nos próximos anos, espera-se que a IA se torne ainda mais integrada à sociedade, com o avanço de carros autônomos, assistentes virtuais mais inteligentes, robôs colaborativos na indústria e sistemas educativos personalizados. O grande desafio será equilibrar o desenvolvimento tecnológico com princípios éticos e humanos, promovendo uma IA a serviço da melhoria da qualidade de vida.

        Em resumo, a Inteligência Artificial é uma ferramenta poderosa que pode transformar positivamente o mundo, desde que seja desenvolvida e aplicada com responsabilidade, respeito à diversidade e foco no bem-estar coletivo.
        """

        texto_original = " ".join(texto_original.split())
        palavras_original = contar_palavras(texto_original)

        print(f"\n📄 TEXTO ORIGINAL ({palavras_original} palavras):")
        print("-" * 50)
        print(texto_original[:300] + "..." if len(texto_original) > 300 else texto_original)

        print(f"\n🤖 Gerando sumário abstrativo...")
        sumario_principal = sumarizar_abstrativo(texto_original, tokenizer, model, modelo_name)
        palavras_sumario = contar_palavras(sumario_principal)

        print(f"\n📋 SUMÁRIO ABSTRATIVO ({palavras_sumario} palavras):")
        print("-" * 50)
        print(sumario_principal)

        avaliar_qualidade_sumario(texto_original, sumario_principal)

        percentual_reducao = (1 - palavras_sumario / palavras_original) * 100
        print(f"\n📊 ESTATÍSTICAS:")
        print(f"   Palavras originais: {palavras_original}")
        print(f"   Palavras no sumário: {palavras_sumario}")
        print(f"   Redução: {percentual_reducao:.1f}%")

    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("Verifique se instalou corretamente:")
        print("pip install torch transformers sentencepiece protobuf")

if __name__ == "__main__":
    main()
