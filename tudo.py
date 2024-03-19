import json

# Carregando o JSON externo
with open('sentiment_dict.json', 'r') as file:
    sentiment_dict = json.load(file)

emoji_dict = {'positivas': ['😊', '😂', '😍', '😎', '😁', '🙂','😀'], 'negativas': ['😢', '😒', '😓', '😔','😕','☹']}


# Função para determinar o sentimento da frase
def determinar_sentimento(frase):
    palavras = frase.split()
    num_positivas = sum(1 for palavra in palavras if palavra in sentiment_dict['positivas'] or palavra in emoji_dict['positivas'])
    num_negativas = sum(1 for palavra in palavras if palavra in sentiment_dict['negativas'] or palavra in emoji_dict['negativas'])
    if num_positivas > num_negativas:
        return "positiva"
    elif num_negativas > num_positivas:
        return "negativa"
    else:
        return "neutra"


# Obtendo a entrada do usuário
entrada_usuario = input("Digite uma frase ou texto: ")

# Determinando o sentimento da frase
sentimento = determinar_sentimento(entrada_usuario)
print(f"O sentimento da frase é: {sentimento}")
