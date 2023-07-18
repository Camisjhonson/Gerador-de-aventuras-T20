import random

ENREDO = ["trabalho de aventureiro", "jornada", "perseguicao", "conflito", "diplomacia", "misterio","resgate"]
NPC = ["autoridade", "aliado", "rival", "protegido", "mentor", "profeta", "bufão", "capanga", "Ídolo","entidade"]
AMEACA = ["clérigos_e_celestiais", "arcanistas_e_magicos", "criminosos", "dragoes", "duyshidakk", "espiritos_da_natureza", "feras", "humanoides" , "lefeu", "mortos_vivos"]
LOCAL = ["Local urbano", "fortificação", "Area rural", "Local deermos", "Fronteiras", "Subterraneo", "lar de vilao","covil de monstros", "Local arcano", "local divino", "nas ruinas", "Local de infestacoes"]
OBJETO = ["armas_e_armaduras", "riquezas","mercadorias","quinquilharias","mercado_clandestinos", "algum item magico"]
EVENTO = ["Um acidente", "Anomalia sobrenatural", "Celebracao", "Dadiva", "Fenômeno Natural","Guerra", "Negociacao", "Praga", "Presenca_divina", "Traicao"]

enredo_escolhido = random.choice(ENREDO)
#enredo_escolhido = "conflito"

#trabalho de avetureiro - esta pronto
if enredo_escolhido == "Trabalho de Aventureiro":
    NPC_ESCOLHIDO = random.sample(NPC, k=2)
    LOCAL_ESCOLHIDO = random.sample(LOCAL, k=2)
    OBJETO_ESCOLHIDO = random.choice(OBJETO)
    EVENTO_ESCOLHIDO = random.choice(EVENTO)
    print (f"O enredo escolhido foi: {enredo_escolhido}\n Você deve usar os NPCs: {NPC_ESCOLHIDO[0]} e {NPC_ESCOLHIDO[1]}\n Ter como ameaça os capangas do vilão!, eles podem ser lacaios puxa-saco, escudeiros, um aprendiz fiel ou até mesmo uma Ama muito Severa.\n Passe a historia nestes 2 locais: {LOCAL_ESCOLHIDO[0]} e {LOCAL_ESCOLHIDO[1]} para encontrarem {OBJETO_ESCOLHIDO}.\n Dica: O objeto pode ser encontrado em qualquer um dos lugares, eles podem usar para ajudar na luta contra o vilão!. Boa aventura ;) ")

#Jornada - esta pronto
elif enredo_escolhido == "jornada":
    LOCAL_ESCOLHIDO = random.sample(LOCAL, k=3)
    OBJETO_ESCOLHIDO = random.choices(OBJETO)
    NPC_ESCOLHIDO = random.choices(NPC)
    EVENTO_ESCOLHIDO = random.choices(EVENTO)
    print(f"O enredo escolhido foi: {enredo_escolhido}\nUma Jornada pode se iniciar por diversos motivos. Nesta, você deve usar UMA dessas opções abaixo:\nNPCs: {NPC_ESCOLHIDO[0]} (ideia: uma escolta ou uma proteção)\nUMA BUSCA POR: {OBJETO_ESCOLHIDO[0]}\nEVENTO: {EVENTO_ESCOLHIDO[0]} \n Os seus aventureiros devem passar por 3 Lugares nesta jornada: {LOCAL_ESCOLHIDO[0]}, {LOCAL_ESCOLHIDO[1]} e {LOCAL_ESCOLHIDO[2]}\nNestes locais, você deve incluir três acontecimentos, podendo ser: 3x evento, 3x personagem ou 3x ameaça. Qual você gostaria de usar?")
    RESPOSTA = input("Digite qual você gostaria de usar? ")
    if RESPOSTA == "evento":
        EVENTO_ESCOLHIDO = random.sample(EVENTO, k=3)
        print(f"Você escolheu: {RESPOSTA}\nNa sua aventura vai ocorrer: {EVENTO_ESCOLHIDO[0]}, {EVENTO_ESCOLHIDO[1]} e {EVENTO_ESCOLHIDO[2]}. O mestre deve escolher a ordem que quiser e associar ao seu planejamento")
    elif RESPOSTA == "personagem":
        NPC_ESCOLHIDO = random.sample(NPC, k=3)
        print(f"Você escolheu: {RESPOSTA}\nNa sua aventura vai ter os NPCs: {NPC_ESCOLHIDO[0]}, {NPC_ESCOLHIDO[1]} e {NPC_ESCOLHIDO[2]}. O mestre deve escolher a ordem que quiser e associar ao seu planejamento")
    elif RESPOSTA == "ameaça":
        AMEACA_ESCOLHIDO = random.sample(AMEACA, k=3)
        print(f"Você escolheu: {RESPOSTA}\nNa sua aventura vai ter as ameaças: {AMEACA_ESCOLHIDO[0]}, {AMEACA_ESCOLHIDO[1]} e {AMEACA_ESCOLHIDO[2]}. O mestre deve escolher a ordem que quiser e associar ao seu planejamento")
    else:
        print("Não entendi sua resposta, por favor role novamente")

#resgate - esta pronto
elif enredo_escolhido == "resgate":
    AMEACA_ESCOLHIDA = random.choices(AMEACA, k=4)
    LOCAL_ESCOLHIDO = random.sample(LOCAL, k=2)
    RESPOSTA = input(f"O enredo escolhido foi: {enredo_escolhido}\nPara esta aventura você deve escolher o que vai ser resgatado: Um NPC ou Um Objeto. Qual você gostaria de usar?")
    if RESPOSTA == "NPC":
        NPC_ESCOLHIDO = random.choice(NPC)
        print(f"Você escolheu: {RESPOSTA}, Boa escolha!\nVamos continuar!\nVocê vai resgatar nesta aventura um NPC: {NPC_ESCOLHIDO}\nPara chegar no local de resgate, será necessário que os aventureiros passem por {LOCAL_ESCOLHIDO[1]} e enfrentem os perigos: {AMEACA_ESCOLHIDA[2]} e {AMEACA_ESCOLHIDA[3]}. Seguindo em frente, o NPC se encontra em um {LOCAL_ESCOLHIDO[0]} e está sob os perigos: {AMEACA_ESCOLHIDA[0]} e {AMEACA_ESCOLHIDA[1]}. Assim você criará a sua aventura! Boa sorte!")
    
    elif RESPOSTA == "objeto":
        OBJETO_ESCOLHIDO = random.choice(OBJETO)
        print(f"Você escolheu: {RESPOSTA} Boa escolha!\nVamos continuar!\nVocê vai resgatar nesta aventura um objeto: {OBJETO_ESCOLHIDO}\nPara chegar no local de resgate, será necessário que os aventureiros passem por {LOCAL_ESCOLHIDO[1]} e enfrentem os perigos: {AMEACA_ESCOLHIDA[2]} e {AMEACA_ESCOLHIDA[3]}. Seguindo em frente, o objeto se encontra em um {LOCAL_ESCOLHIDO[0]} e está sob os perigos: {AMEACA_ESCOLHIDA[0]} e {AMEACA_ESCOLHIDA[1]}. Assim você criará a sua aventura! Boa sorte!")

    else:
        print("Opção inválida. Por favor, role novamente.")

#perseguição : vou declarar esta parte mais a frente pois estou em duvidas de como formar a sequencia de acontecimentos.
elif enredo_escolhido == "perseguicao":
    AMEACA_ESCOLHIDA = random.choice(AMEACA)
    LOCAL_ESCOLHIDO = random.sample(LOCAL, k=3)
    RESULTADO = random.choice(["ser perseguidos por", "perseguir"])
    print(f"Nesta aventura os aventureiros vão {RESULTADO} uma ameaça.")
    print(f"A ameaça é: {AMEACA_ESCOLHIDA}")
    print("O motivo desta perseguição pode ser um objeto ou um evento.")
    RESULTADO = input("Nesta ocasião, qual você gostaria de escolher? (objeto/evento) ")
    if RESULTADO == "evento":
        EVENTO_ESCOLHIDO = random.choice(EVENTO)
        print(f"Você escolheu Evento.\n O seu evento será: {EVENTO_ESCOLHIDO}")
        print(f"Esta perseguição vai acontecer em 3 locais diferentes: {LOCAL_ESCOLHIDO[0]}, {LOCAL_ESCOLHIDO[1]} e {LOCAL_ESCOLHIDO[2]}.")
        print("Para complementar a história, você deve utilizar 3 NPCs ou 3 Ameaças.")
        RESPOSTA = input("Qual você gostaria de usar? (NPC/ameaça) ")
        if RESPOSTA == "NPC":
            NPC_ESCOLHIDO = random.sample(NPC, k=3)
            print(f"Você escolheu NPCs\n Os NPCs que vão complementar sua historia são:{NPC_ESCOLHIDO[0]},{NPC_ESCOLHIDO[1]} e {NPC_ESCOLHIDO[2]}.")
            print("Caso a perseguição se estenda até o ultimo local, a presa(aquele que esta sendo perseguido) estara a salvo!)")
        elif RESPOSTA == "ameaça":
            AMEACA_ESCOLHIDA = random.sample(AMEACA, k=3)
            print(f"Você escolheu Ameaça\n As ameaças que vão complementar sua historia são:{AMEACA_ESCOLHIDA[0]},{AMEACA_ESCOLHIDA[1]} e {AMEACA_ESCOLHIDA[2]}.")
            print("Caso a perseguição se estenda até o ultimo local, a presa(aquele que esta sendo perseguido) estara a salvo!)")
        else:
            print("Resposta não identificada. Role novamente!")
    elif RESULTADO == "objeto":
            OBJETO_ESCOLHIDO = random.sample(OBJETO, k=3)
            print(f"Você escolheu Objeto\n O objeto que vão complementar sua historia são:{OBJETO_ESCOLHIDO[0]},{OBJETO_ESCOLHIDO[1]} e {OBJETO_ESCOLHIDO[2]}.")
        
    else:
        print("Resposta inválida. Role novamente.")


#conflito
elif enredo_escolhido == "conflito":
    DADO = random.randint(1, 4)
    NPC_ESCOLHIDO = random.choices(NPC, k=4)
    AMEACA_ESCOLHIDA = random.choices(AMEACA, k=4)
  
    if DADO == 1 :
        print (f"O enredo escolhido foi: {enredo_escolhido}\n Nesta aventura vai ter uma facção liderada por {NPC_ESCOLHIDO[0]},\n com a ameaça:{AMEACA_ESCOLHIDA[0]}\n Este quebra pau esta acontecendo pois todos querem a posse de um lugar ou de um objeto;)")
        RESPOSTA = input ("Qual você gostaria de usar?(objeto / local)") 
            
        if RESPOSTA == "local":
                LOCAL_ESCOLHIDO = random.choices(LOCAL)
                print (f"Você escolheu Local, Boa escolha \n O local escolhido foi {LOCAL_ESCOLHIDO[0]}. Boa aventura!")
        elif RESPOSTA == "objeto":
                OBJETO_ESCOLHIDO = random.choices(OBJETO)
                print (f"Você escolheu objeto, Boa escolha \n O objeto escolhido foi {OBJETO_ESCOLHIDO[0]}. Boa aventura!")
        else :
            print ("Comando invalido, role novamente!")
   
    elif DADO == 2 :
        print (f"O enredo escolhido foi: {enredo_escolhido}\n Nesta aventura vão ter 2 facções lideradas por {NPC_ESCOLHIDO[0]} e {NPC_ESCOLHIDO[1]},\n com as ameaças:{AMEACA_ESCOLHIDA[0]} e {AMEACA_ESCOLHIDA[1]}\n Este quebra pau esta acontecendo pois todos querem a posse de um lugar ou de um objeto;)")
        RESPOSTA = input ("Qual você gostaria de usar?(objeto / local)") 
            
        if RESPOSTA == "local":
                LOCAL_ESCOLHIDO = random.choices(LOCAL)
                print (f"Você escolheu Local, Boa escolha \n O local escolhido foi {LOCAL_ESCOLHIDO[0]}. Boa aventura!")
        elif RESPOSTA == "objeto":
                OBJETO_ESCOLHIDO = random.choices(OBJETO)
                print (f"Você escolheu objeto, Boa escolha \n O objeto escolhido foi {OBJETO_ESCOLHIDO}. Boa aventura!")
        else :
            print ("Comando invalido, role novamente!")

    elif DADO == 3 :
            print (f"O enredo escolhido foi: {enredo_escolhido}\n Nesta aventura vão ter 3 facções lideradas por {NPC_ESCOLHIDO[0]}, {NPC_ESCOLHIDO[1]} e {NPC_ESCOLHIDO[0]}\n com as ameaças:{AMEACA_ESCOLHIDA[0]}, {AMEACA_ESCOLHIDA[1]} e {AMEACA_ESCOLHIDA[2]} \n Este quebra pau esta acontecendo pois todos querem a posse de um lugar ou de um objeto;)")
            RESPOSTA = input ("Qual você gostaria de usar?(objeto / local)")
            if RESPOSTA == "local":
                LOCAL_ESCOLHIDO = random.choices(LOCAL)
                print (f"Você escolheu Local, Boa escolha \n O local escolhido foi {LOCAL_ESCOLHIDO[0]}. Boa aventura!")
            elif RESPOSTA == "objeto":
                OBJETO_ESCOLHIDO = random.choices(OBJETO)
                print (f"Você escolheu objeto, Boa escolha \n O objeto escolhido foi {OBJETO_ESCOLHIDO[0]}. Boa aventura!")
            else :
               print ("Comando invalido, role novamente!")

    elif DADO == 4 :
        print (f"O enredo escolhido foi: {enredo_escolhido}\n Nesta aventura vão ter 3 facções lideradas por {NPC_ESCOLHIDO[0]}, {NPC_ESCOLHIDO[1]}, {NPC_ESCOLHIDO[2]} e {NPC_ESCOLHIDO[3]}\n com as ameaças:{AMEACA_ESCOLHIDA[0]}, {AMEACA_ESCOLHIDA[1]}, {AMEACA_ESCOLHIDA[2]} e {AMEACA_ESCOLHIDA[3]} \n Este quebra pau esta acontecendo pois todos querem a posse de um lugar ou de um objeto;)")
        RESPOSTA = input ("Qual você gostaria de usar?(objeto / local)") 
            
        if RESPOSTA == "local":
                LOCAL_ESCOLHIDO = random.choices(LOCAL)
                print (f"Você escolheu Local, Boa escolha \n O local escolhido foi {LOCAL_ESCOLHIDO[0]}. Boa aventura!")
        elif RESPOSTA == "objeto":
                OBJETO_ESCOLHIDO = random.choices(OBJETO)
                print (f"Você escolheu objeto, Boa escolha \n O objeto escolhido foi {OBJETO_ESCOLHIDO}. Boa aventura!")
        else :
            print ("Comando invalido, role novamente!")
    else:
        print("role novamente!")
            

#diplomacia
elif enredo_escolhido == "diplomacia":
    NPC_ESCOLHIDO = random.choices(NPC, k=2)
    AMEACA_ESCOLHIDA = random.choices(AMEACA)
    LOCAL_ESCOLHIDO = random.choices(LOCAL)
    OBJETO_ESCOLHIDO = random.choices(OBJETO)
    EVENTO_ESCOLHIDO = random.choices(EVENTO)
    print (f"O enredo escolhido foi: {enredo_escolhido}\n Você deve usar os NPCs: {NPC_ESCOLHIDO[0]} e {NPC_ESCOLHIDO[1]}\n Ter como ameaça {AMEACA_ESCOLHIDA[0]} \n Dica:Passe a historia em {LOCAL_ESCOLHIDO[0]} para encontrarem o {OBJETO_ESCOLHIDO[0]} ou você pode relacionar isto a um evento como: {EVENTO_ESCOLHIDO[0]}. Boa aventura ;)")

#misterio
elif enredo_escolhido == "misterio":
    NPC_ESCOLHIDO = random.choices(NPC, k=2)
    AMEACA_ESCOLHIDA = random.choices(AMEACA)
    LOCAL_ESCOLHIDO = random.choices(LOCAL)
    OBJETO_ESCOLHIDO = random.choices(OBJETO)
    EVENTO_ESCOLHIDO = random.choices(EVENTO)
    print (f"O enredo escolhido foi: {enredo_escolhido}\n Você deve usar os NPCs: {NPC_ESCOLHIDO[0]} e {NPC_ESCOLHIDO[1]}\n Ter como ameaça {AMEACA_ESCOLHIDA[0]} \n Dica:Passe a historia em {LOCAL_ESCOLHIDO[0]} para encontrarem o {OBJETO_ESCOLHIDO[0]} ou você pode relacionar isto a um evento como: {EVENTO_ESCOLHIDO[0]}. Boa aventura ;)")

#mensagem de erro
else:
    print ("Role novamente o dado")