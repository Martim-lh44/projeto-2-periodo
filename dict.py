import pickle

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
                      "sushi","baunilha","morango","banana","abacate","manga","pera","kiwi",
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

with open("dicionario.bin", "wb") as arquivo:
    pickle.dump(dicionario, arquivo)
