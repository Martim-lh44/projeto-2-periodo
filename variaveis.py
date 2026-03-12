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

def palavras_1_3():
    tema, palavras = random.choice(list(dicionario.items()))
    palavras_jogo = random.sample(palavras, quantidade_palavras)
    return tema, palavras_jogo

def palavras_2():
    quantidade_palavras= 3
    tema, palavras = random.choice(list(dicionario.items()))
    palavras_jogo = random.sample(palavras, quantidade_palavras)
    return tema, palavras_jogo

tema_1_3, palavras_3_1 = palavras_1_3()

print("Tema:", tema_1_3)
print("Palavras:", palavras_3_1)

tema_2, palavras2 = palavras_2()

print("Tema:", tema_2)
print("Palavras:", palavras2)
