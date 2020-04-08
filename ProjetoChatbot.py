def saudacao_GUI(nome):
    import random 
    frases=["Bom dia! Meu nome é "+nome+". Como vai você?", "Olá!", "Oi! Tudo bom?"] 
    return frases[random.randint(0,2)]

def saudacao(nome):
    import random 
    frases=["Bom dia! Meu nome é "+nome+". Como vai você?", "Olá!", "Oi! Tudo bom?"] 
    print(frases[random.randint(0,2)])
    

def recebeTexto():
    texto = input("Cliente: ")
    palavrasProibida = ["bocó"]
    for p in palavrasProibida:
        if p in texto:
            print("Não vem não! Me respeite!")
            return recebeTexto()
    return texto

def buscaResposta_GUI(texto):
    with open("BaseDeConhecimento.txt","a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if jaccard(texto, viu)>0.3:
                    proximaLinha = conhecimento.readline()
                    if "Chatbot: " in proximaLinha:
                        return proximaLinha
            else:
                conhecimento.write(texto)
                return "Me desculpe, não sei o que falar"
             
def salva_sugestao(sugestao):
    with open("BaseDeConhecimento.txt","a+") as conhecimento:
        conhecimento.write("Chatbot: "+sugestao+"\n")
        
def buscaResposta(texto):
    with open("BaseDeConhecimento.txt","a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto == viu:
                    proximaLinha = conhecimento.readline()
                    if "Chatbot: " in proximaLinha:
                        return proximaLinha
            else:
                print("Me desculpe, não sei o que falar")
                conhecimento.write(texto)
                resposta_user = input("O que você esperava?\n")
                conhecimento.write("Chatbot: "+resposta_user+"\n")
                return "Hum..."


def exibeResposta(texto, resposta, nome):
    print(resposta.replace("Chatbot", nome))
    if texto == "tenho que ir":
        print("Mas já...pois tá né? Tchau!")
        return "fim"
    return "continua"

def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("Chatbot", nome)

def jaccard(textoUsuario,textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum+=1
        
        return palavras_em_comum/len(textoUsuario.split()) + len(textoBase.split()) -(len(textoBase.split(" ")))
                                     
                           
    
def limpa_frase(frase):
    tirar = ["?","!","...",".",",", "Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase
                       