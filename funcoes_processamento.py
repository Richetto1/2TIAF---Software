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