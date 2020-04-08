import ProjetoChatbot as pc

nome_maquina = "Maria"
pc.saudacao(nome_maquina)
while True:
    texto = pc.recebeTexto()
    resposta = pc.buscaResposta("Cliente: "+texto+"\n")
    if pc.exibeResposta(texto,resposta, nome_maquina) == "fim":
        break
