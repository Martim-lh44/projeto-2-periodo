import flet as ft 
import random

def main(page: ft.Page):
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

    quantidade_palavras = 1

    def palavras_1_3():
        tema, palavras = random.choice(list(dicionario.items()))
        palavras_jogo = random.sample(palavras, quantidade_palavras)
        return tema, palavras_jogo

    def palavras_2():
        quantidade_palavras_local = 3
        tema, palavras = random.choice(list(dicionario.items()))
        palavras_jogo = random.sample(palavras, quantidade_palavras_local)
        return tema, palavras_jogo

    tema_1_3, palavras_3_1 = palavras_1_3()
    tema_2, palavras2 = palavras_2()

    def gerar_novas_palavras_1_3():
        nonlocal tema_1_3, palavras_3_1
        tema_1_3, palavras_3_1 = palavras_1_3()

    def gerar_novas_palavras_2():
        nonlocal tema_2, palavras2
        tema_2, palavras2 = palavras_2()

    page.title = "Jogo da Forca"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    indice_palavra = {"valor": 0}
    palavras_jogo = []
    palavra_atual = {"palavra": ""}
    letras_usadas = []
    texto_palavra = ft.Text(size=30, weight=ft.FontWeight.BOLD)

    historico = []
    historico.append(lambda: None)

    vidas= {"valor": 6}
    texto_vidas= ft.Text()

    letras_erradas = []
    texto_erradas = ft.Text()

    jogo_terminado= {"valor": False}

    botoes_teclado = {}

    forca = [
        """
          _______
         |/      |
         |
         |
         |
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |
         |
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |       |
         |       |
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \|
         |       |
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      /
         |
        _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      / \     
         |
        _|___
        """
    ]
    
    texto_forca= ft.Text(value=forca[0], font_family="monospace")

    titulo_forca = ft.Text(
"""
 _____   _____   ____    _____   _____    _____         _____
|  ___| /  _  \ |  _ \  |  ___| |  _  |  |___  |       |  _  |
| |_    | | | | | |_| | | |     | | | |   ___| |       | | | |
|  _|   | | | | |   _/  | |     | |_| |  /  ___|  ___  | | | |
| |     | |_| | |   \   | |__   |  _  |  | |___  |   | | |_| |
|_|     \_____/ |_|\_\  |_____| |_| |_|  |_____| |___| |_____|
""",
        font_family="Courier New",
        size=18,
        weight=ft.FontWeight.BOLD,
    )

    capa_derrota = ft.Text(
"""
 ______    ____    __  __    ______     ______    _    _   ______   _____                  
|  ____|  / __ \  |  \/  |  |  ____|   |  __  |  | |  | | |  ____| |  __ \    ⌐╦╦═─ (x_x)  
| |      | |  | | |      |  | |_       | |  | |  | |  | | | |_     | |__| |           |    
| |  __  | |__| | | |\/| |  |   |      | |  | |  | |  | | |   |    |     /           /|\   
| |  | | |  __  | | |  | |  |  _|      | |  | |  | |  | | |  _|    |  _ \           / | \  
| |__| | | |  | | | |  | |  | |____    | |__| |   \ \/ /  | |____  | | \ \           / \   
|______| |_|  |_| |_|  |_|  |______|   |______|    \__/   |______| |_|  \_\         /   \  
""",
        font_family="Courier New",
        size=18,
        weight=ft.FontWeight.BOLD,
    )

    capa_vitoria = ft.Text(
"""
__    __  ______   _    _      _    _   ______   _    _    * *    * *  
\ \  / / |  __  | | |  | |    | |  | | |      | | \  | |    * (^o^) *  
 \ \/ /  | |  | | | |  | |    | |  | | |_    _| |  \ | |       /|\     
  \  /   | |  | | | |  | |    | |/\| |   |  |   |   \| |      / | \    
   ||    | |  | | | |  | |    |      |  _|  |_  | |\   |        |      
   ||    | |__| | | |__| |    |  /\  | |      | | | \  |       / \     
   ||    |______| |______|    |_/  \_| |______| |_|  \_|      /   \   
""",
        font_family="Courier New",
        size=18,
        weight=ft.FontWeight.BOLD,
    )

    def clean_page():
        page.controls.clear()
        page.update()
    
    def abrir_pagina(funcao):
        historico.append(funcao)
        funcao()

    def voltar():
        if len(historico) > 1:
            historico.pop()
            historico[-1]()  

    def atualizar_palavra():
        resultado = ""
        for letra in palavra_atual["palavra"]:
            if letra in letras_usadas or letra in [" ", "-"]:
                resultado += letra + " "
            else:
                resultado += "_ "
        texto_palavra.value = resultado
        page.update()

    def clicar_letra(letra):
        if jogo_terminado["valor"]:
            return

        botoes_teclado[letra].disabled = True

        if letra not in letras_usadas:
            letras_usadas.append(letra)

        if letra not in palavra_atual["palavra"]:
            letras_erradas.append(letra)
            vidas["valor"] -= 1

        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = "Erradas: " + ", ".join(letras_erradas)
        texto_forca.value = forca[6 - vidas["valor"]]

        atualizar_palavra()

        ganhou = True
        for l in palavra_atual["palavra"]:
            if l not in letras_usadas and l not in [" ", "-"]:
                ganhou = False

        if ganhou and not jogo_terminado["valor"]:
            indice_palavra["valor"] += 1

            if indice_palavra["valor"] < len(palavras_jogo):
                letras_usadas.clear()
                letras_erradas.clear()
                for botao in botoes_teclado.values():
                    botao.disabled = False
                palavra_atual["palavra"] = palavras_jogo[indice_palavra["valor"]]
                page.add(ft.Text("Próxima palavra!", size=20))
                atualizar_palavra()
            else:
                jogo_terminado["valor"] = True
                clean_page()
                page.add(
                    ft.Column(
                        [
                            capa_vitoria,
                            ft.Text("Parabéns! Adivinhaste todas as palavras!", size=20),
                            ft.Container(height=40),
                            ft.Row(
                                [
                                    ft.ElevatedButton(
                                        "Jogar Outra Vez",
                                        on_click=lambda e: reiniciar_nivel(nivel_atual)
                                    ),
                                    ft.ElevatedButton(
                                        "Menu",
                                        on_click=lambda e: (
                                            gerar_novas_palavras_1_3(),
                                            gerar_novas_palavras_2(),
                                            abrir_pagina(modo_jogo)
                                        )
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True
                    )
                )

        if vidas["valor"] == 0:
            jogo_terminado["valor"] = True
            clean_page()
            page.add(
                ft.Column(
                    [
                        capa_derrota,
                        ft.Text(f"A palavra era: {palavra_atual['palavra']}", size=20),
                        ft.Container(height=40),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Tentar Outra Vez",
                                    on_click=lambda e: reiniciar_nivel(nivel_atual)
                                ),
                                ft.ElevatedButton(
                                    "Menu",
                                    on_click=lambda e: (
                                        gerar_novas_palavras_1_3(),
                                        gerar_novas_palavras_2(),
                                        abrir_pagina(modo_jogo)
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            )

        page.update()

    def teclado():
        letras = "QWERTYUIOPASDFGHJKLZXCVBNM"
        botoes = []

        for letra in letras:
            botao = ft.ElevatedButton(
                letra,
                on_click=lambda e, l=letra.lower(): clicar_letra(l)
            )
            botoes_teclado[letra.lower()] = botao
            botoes.append(botao)

        linha1 = ft.Row(botoes[0:10], alignment=ft.MainAxisAlignment.CENTER)
        linha2 = ft.Row(botoes[10:19], alignment=ft.MainAxisAlignment.CENTER)
        linha3 = ft.Row(botoes[19:26], alignment=ft.MainAxisAlignment.CENTER)

        return ft.Column(
            [linha1, linha2, linha3],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def reiniciar_nivel(func_nivel):
        letras_usadas.clear()
        letras_erradas.clear()
        for botao in botoes_teclado.values():
            botao.disabled = False           
        botoes_teclado.clear()
        vidas["valor"] = 6
        jogo_terminado["valor"] = False
        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = ""
        texto_forca.value = forca[0]
        indice_palavra["valor"] = 0
        
        if func_nivel == jogar1 or func_nivel == jogar2:
            gerar_novas_palavras_1_3()
        elif func_nivel == jogar3:
            gerar_novas_palavras_2()
        
        if func_nivel != camigos:  # só atualiza palavra se não for Camigos
            if palavras_jogo:
                palavra_atual["palavra"] = palavras_jogo[indice_palavra["valor"]]
        
        abrir_pagina(func_nivel)

    nivel_atual = None

    def jogar1():
        nonlocal nivel_atual
        nivel_atual = jogar1
        clean_page()
        letras_usadas.clear()
        letras_erradas.clear()
        botoes_teclado.clear()
        indice_palavra["valor"] = 0
        palavras_jogo.clear()
        palavras_jogo.extend(palavras_3_1)
        palavra_atual["palavra"] = palavras_jogo[0]

        page.add(
            ft.Text(f"Tema: {tema_1_3}", size=20),
            texto_forca,
            texto_palavra,
            texto_vidas,
            texto_erradas,
            teclado(),
            ft.ElevatedButton("Voltar", on_click=lambda e: abrir_pagina(niveis))
        )

        atualizar_palavra()

    def jogar2():
        nonlocal nivel_atual
        nivel_atual = jogar2
        clean_page()
        letras_usadas.clear()
        letras_erradas.clear()
        botoes_teclado.clear()
        indice_palavra["valor"] = 0
        palavras_jogo.clear()
        palavras_jogo.extend(palavras_3_1)
        palavra_atual["palavra"] = palavras_jogo[0]

        page.add(
            ft.Text(f"Tema: Indisponível", size=20),
            texto_forca,
            texto_palavra,
            texto_vidas,
            texto_erradas,
            teclado(),
            ft.ElevatedButton("Voltar", on_click=lambda e: abrir_pagina(niveis))
        )

        atualizar_palavra()

    def jogar3():
        nonlocal nivel_atual
        nivel_atual = jogar3
        clean_page()
        letras_usadas.clear()
        letras_erradas.clear()
        botoes_teclado.clear()
        palavras_jogo.clear()
        palavras_jogo.extend(palavras2)
        indice_palavra["valor"] = 0
        palavra_atual["palavra"] = palavras_jogo[indice_palavra["valor"]]

        page.add(
            ft.Text(f"Tema: {tema_2}", size=20),
            texto_forca,
            texto_palavra,
            texto_vidas,
            texto_erradas,
            teclado(),
            ft.ElevatedButton("Voltar", on_click=lambda e: abrir_pagina(niveis))
        )

        atualizar_palavra()

    def niveis():
        clean_page()
        page.add(
            ft.Column(
                [
                    ft.Text("Jogo da Forca", size=22, weight=ft.FontWeight.BOLD),
                    ft.Text("Escolha o nível", size=15),
                    ft.Row(
                        [
                            ft.ElevatedButton("Nível 1", on_click=lambda e: abrir_pagina(jogar1)),
                            ft.ElevatedButton("Nível 2", on_click=lambda e: abrir_pagina(jogar2)),
                            ft.ElevatedButton("Nível 3", on_click=lambda e: abrir_pagina(jogar3))
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ElevatedButton("Voltar", on_click=lambda e: abrir_pagina(modo_jogo))
                ],
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    def modo_jogo():
        letras_usadas.clear()
        letras_erradas.clear()
        botoes_teclado.clear()
        vidas["valor"] = 6
        jogo_terminado["valor"] = False
        indice_palavra["valor"] = 0
        palavra_atual["palavra"] = ""
        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = ""
        texto_forca.value = forca[0]
        atualizar_palavra()
        clean_page()
        page.add(
            ft.Column(
                [
                    ft.Text("Jogo da Forca", size=22, weight=ft.FontWeight.BOLD),
                    ft.Text("Escolha o modo de jogo", size=15),
                    ft.Row(
                        [
                            ft.ElevatedButton("Clássicos", on_click=lambda e: abrir_pagina(niveis)),
                            ft.ElevatedButton("Com Amigos", on_click=lambda e: abrir_pagina(camigos))
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    def camigos():
        nonlocal nivel_atual
        nivel_atual = camigos
        clean_page()
        palavra = ft.TextField(label="Escreve a palavra para o teu amigo adivinhar")
        tema = ft.TextField(label="Escreve o tema da palavra")

        def comecar(e):
            letras_usadas.clear()
            letras_erradas.clear()
            botoes_teclado.clear()
            palavra_atual["palavra"] = palavra.value.lower()
            clean_page()
            page.add(
                ft.Text(f"Tema: {tema.value}", size=20),
                texto_forca,
                texto_palavra,
                texto_vidas,
                texto_erradas,
                teclado(),
                ft.ElevatedButton("Voltar", on_click=voltar)
            )
            atualizar_palavra()

        page.add(
            ft.Text("Jogo da Forca", size=22, weight=ft.FontWeight.BOLD),
            ft.Text("Escolhe a palavra", size=15),
            palavra,
            tema,
            ft.ElevatedButton("Começar", on_click=comecar),
            ft.ElevatedButton("Voltar", on_click=lambda e: abrir_pagina(modo_jogo))
        )

    def capa_abertura():
        clean_page()
        page.add(
            ft.Column(
                [
                    titulo_forca,
                    ft.Text("Tenta adivinhar a palavra antes de seres enforcado!", size=16),
                    ft.Container(height=40),
                    ft.ElevatedButton(
                        "COMEÇAR",
                        width=200,
                        on_click=lambda e: abrir_pagina(modo_jogo)
                    )
                ],
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    capa_abertura()

ft.run(main)
