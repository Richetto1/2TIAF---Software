import re

def dividir_texto_em_palavras(texto):
    palavras = texto.split()
    return palavras 

def identificar_complemento_nominal(frase):
    padrao = r'\b(?:de|para|por|a|ao|aos|da|do|em|com|sem)\b\s+(\w+)(?:\s+(\w+))?\s+(?:\w+o|a|os|as|um|uma|uns|umas)\b' # Lista com os abridores do complemento nominal
    match = re.search(padrao, frase)
    
    if match:
        # Captura a parte da frase a partir da palavra identificada até o final da frase
        complemento_nominal = frase[match.start():]
        return complemento_nominal
    else:
        return None

# teste utilizando a função:
texto = input("Digite o texto: ")
resultado = identificar_complemento_nominal(frase)
if resultado:
    print("Complemento nominal encontrado:", resultado)
else:
    print("Nenhum complemento nominal encontrado na frase.")

    #Programa ainda quebrado, necessita de uma correção na função para que retorne o complemento nominal 

def identificar_complemento_verbal(frase):
    # Lista de terminações de verbos
    terminacoes_verbais = ["ar", "er", "ir"]
 
    # Dividir a frase em palavras
    palavras = frase.split()
 
    # Verificar cada palavra na frase
    for palavra in palavras:
        # Verificar se a palavra termina com uma das terminações de verbos
        for terminacao in terminacoes_verbais:
            if palavra.endswith(terminacao):
                # Se a palavra for um verbo, procurar o próximo substantivo como complemento
                index_verbo = palavras.index(palavra)
                if index_verbo < len(palavras) - 1:
                    complemento = " ".join(palavras[index_verbo + 1:])
                    print("Complemento verbal encontrado:", complemento)
                    return
                else:
                    print("Verbo sem complemento.")
                    return
 
    print("Não foi encontrado nenhum verbo na frase.")
 
# Exemplo de uso
frase = "Ela gosta de nadar na piscina."
identificar_complemento_verbal(frase)