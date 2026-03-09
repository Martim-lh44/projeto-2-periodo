import random

# Dicionário
dicionario = {
    "ANIMAIS": ["leao","zebra","tigre","coala","panda","foca","lince","porco","cavalo",
                "cabra","galgo","burro","bufalo","urso","raposa","lobo","gato","cao",
                "pomba","corvo","aguia","falcao","pato","ganso","avestruz","peru","pavao",
                "golfinho","tubarao","orca","salmao","truta","polvo","lula","caranguejo",
                "lagosta","tartaruga","sapo","cobra","iguana","cavalo-marinho","formiga",
                "abelha","minhoca","caracol","coelho","canguru","hiena","lhama","crocodilo"],
    "PAISES": ["portugal","espanha","franca","italia","alemanha","holanda","belgica","suica",
               "austria","polonia","noruega","suecia","finlandia","dinamarca","irlanda",
               "reino unido","grecia","turquia","russia","ucrania","china","japao","coreia",
               "india","nepal","tailandia","vietname","malasia","indonesia","australia",
               "nova zelandia","egito","marrocos","tunisia","africa do sul","quenia",
               "nigeria","etiopia","canada","mexico","brasil","argentina"],
    "ALIMENTOS": ["massa","arroz","queijo","iogurte","croissant","peixe","carne","batata",
                  "feijao","tomate","cebola","cenoura","alface","sopa","pizza","hamburguer",
                  "tosta","sandes","chocolate","gelado","biscoito","omelete","lasanha",
                  "sushi","baunillha","morango","banana","abacate","manga","pera","kiwi",
                  "pessego","amendoim","ervilha","berinjela","abobora","chuchu","brocolo",
                  "couve","frango","espinafre","melancia","melao","tapioca"],
    "MARCAS": ["apple","samsung","lenovo","microsoft","google","amazon","tesla","mercedes",
               "volkswagen","toyota","honda","ferrari","reebok","gucci","prada","chanel",
               "nespresso","coca-cola","pepsi","red bull","nestle","danone","mcdonalds","spotify",
               "adidas","ikea","lacoste","rolex","canon","sony","asus","puma","fila","intel",
               "burger king","starbucks","peugeot","jaguar","philips","vodafone","nude project","pato"],
    "CIDADES": ["lisboa","porto","braga","coimbra","madrid","paris","roma","berlim","viena",
                "londres","dublin","estocolmo","varsovia","budapeste","atenas","istambul",
                "moscovo","new york","los angeles","chicago","toronto","vancouver",
                "cidade do mexico","sao paulo","rio de janeiro","brasilia","buenos aires",
                "toquio","pequim","xangai","banguecoque","nova deli","melbourne","sydney",
                "cairo","singapura","barcelona","valencia","sevilha","zurique"],
    "OBJETOS": ["mesa","cadeira","lampada","caneta","borracha","mochila","prato","colher",
                "telemovel","computador","teclado","monitor","tomada","carteira","porta","janela",
                "cortina","livro","caderno","camisola","sapatos","toalha","manta","almofada",
                "garrafa","relogio","carregador","quadro","radio","aquecedor","espelho",
                "cobertor","almofada","sofa","poltrona","armario","televisao","fogao",
                "frigorifico","micro-ondas","teclado"]
}

jogar_again = True
letras_permitidas = "abcdefghijklmnopqrstuvwxyz "  # sem acentos e sem cedilha
tema_revelado = True
quantidade_palavras = 1

# mini-jogo
def adivinha_numero():
    numero = random.randint(1, 10)
    print("Mini-jogo: Adivinha o número entre 1 e 10. Tens 1 tentativa!")
    palpite = input("Qual é o número? ")

    if palpite.isdigit():
        palpite = int(palpite)
    else:
        print("Isso não é um número! Perdeste a chance.")
        return 0

    if palpite == numero:
        print("Acertaste! Ganhas 1 vida.")
        return 1
    else:
        print(f"Erraste! O número era {numero}.")
        return 0

def nivel_1_3():
    tema, palavras = random.choice(list(dicionario.items()))
    palavras_jogo = random.sample(palavras, quantidade_palavras)
    jogo(tema, palavras_jogo)

def nivel_2():
    tema, palavras = random.choice(list(dicionario.items()))
    palavras_jogo = [random.choice(palavras)]
    jogo(tema, palavras_jogo)

def jogo(tema, palavras_jogo):
    perdeu_jogo = False
    for i, palavra in enumerate(palavras_jogo, start=1):
        letras_intro = []
        letras_intro1 = [" ", "-"]
        chances = 6
        ganhou = False
        nova_vida2 = False

        while True:
            # Mostrar tema
            if tema_revelado:
                print(f"Palavra {i}/{quantidade_palavras} - Tema: {tema}")
            else:
                print(f"Palavra {i}/{quantidade_palavras} - Tema oculto!")

            # Mostrar palavra
            palavra_mostrada = " ".join([letra if letra in letras_intro1 else "_" for letra in palavra])
            print(palavra_mostrada)

            # Letras já usadas
            print("Letras já introduzidas: " + (", ".join(letras_intro) if letras_intro else ""))

            # Mostrar vidas
            print(f"Tens {chances} vidas")

            # Input letra
            tentativa = input("Escolha uma letra: ")

            # Validações
            while True:
                if len(tentativa) != 1:
                    tentativa = input("Insere APENAS uma letra: ").lower()
                    continue
                if tentativa not in letras_permitidas:
                    tentativa = input("Carácter inválido! Insere outra letra: ").lower()
                    continue
                if tentativa in letras_intro:
                    tentativa = input("Já tentaste essa letra! Escolhe outra: ").lower()
                    continue
                break 

            letras_intro.append(tentativa)
            letras_intro1.append(tentativa)

            # Letra errada
            if tentativa not in palavra and chances > 0:
                chances -= 1

            # Mini-jogo se perder todas as vidas
            if not nova_vida2 and chances == 0:
                nova_vida2 = True
                print("Ficaste sem vidas! Vamos jogar um mini-jogo para tentar ganhar 1 vida.")
                print("Prima ENTER para começar a jogar...")
                input("")
                nova_vida = adivinha_numero()
                if nova_vida > 0:
                    chances += nova_vida
                    print(f"Agora tens {chances} vidas! Continua a jogar...")
                else:
                    print("Sem vidas adicionais. Palavra perdida.")

            # Verificar vitória
            if all(letra in letras_intro1 for letra in palavra):
                ganhou = True
                break

            # Verificar derrota
            if chances == 0 and nova_vida2:
                perdeu_jogo = True
                break

        if perdeu_jogo:
            break
