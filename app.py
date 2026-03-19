import flet as ft 
import random
from dict import dicionario  # Assumindo que já tens o dict.py importado

def main(page: ft.Page):
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
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    indice_palavra = {"valor": 0}
    palavras_jogo = []
    palavra_atual = {"palavra": ""}
    letras_usadas = []
    texto_palavra = ft.Text(size=32, weight=ft.FontWeight.BOLD, color="#E5E7EB")

    historico = []
    historico.append(lambda: None)

    vidas= {"valor": 6}
    texto_vidas= ft.Text(color="#F97373", size=16)

    letras_erradas = []
    texto_erradas = ft.Text(color="#F97373", size=14)

    jogo_terminado= {"valor": False}
    
    # NOVAS VARIÁVEIS DO MINIJOGO
    numero_secreto = {"valor": 0}
    minijogo_ativo = {"valor": False}

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
        |     \|/
        |       |
        |
        |
        _|___
        """,
        """
         _______
        |/      |
        |      (_)
        |     \|/
        |       |
        |      /
        |
        _|___
        """,
        """
         _______
        |/      |
        |      (_)
        |     \|/
        |       |
        |     / \     
        |
        _|___
        """
    ]
    
    texto_forca= ft.Text(value=forca[0], font_family="monospace")

    # ASCII ARTS (mantidos iguais)
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
        color="#FACC15"
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
        color="#F97373"
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
        color="#4ADE80"
    )

    # *** NOVO MINIJOGO ***
    def minijogo_numero():
        numero_secreto["valor"] = random.randint(0, 9)
        minijogo_ativo["valor"] = True
        clean_page()
        
        numero_input = ft.TextField(
            label="Digite um número (0-9)",
            width=250,
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=1
        )
        
        def tentar_numero(e):
            try:
                chute = int(numero_input.value)
                if 0 <= chute <= 9:
                    if chute == numero_secreto["valor"]:
                        # GANHOU 1 VIDA!
                        minijogo_ativo["valor"] = False
                        vidas["valor"] = 1
                        page.dialog.open = False
                        abrir_pagina(nivel_atual)
                    else:
                        derrota_final()
                else:
                    numero_input.error_text = "Só números de 0 a 9!"
                    page.update()
            except:
                numero_input.error_text = "Número inválido!"
                page.update()
        
        page.add(
            ft.Container(
                bgcolor="#020617",
                border_radius=20,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "🎲 ÚLTIMA CHANCE! 🎲",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color="#FACC15"
                        ),
                        ft.Text(
                            "Adivinha o número de 0 a 9 para ganhar 1 vida!",
                            size=16,
                            color="#E5E7EB"
                        ),
                        ft.Container(height=20),
                        ft.Text(
                            "Número secreto: ???",
                            size=20,
                            color="#F97373"
                        ),
                        ft.Container(height=10),
                        numero_input,
                        ft.Container(height=10),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "TENTAR",
                                    icon=ft.Icons.CHECK,
                                    bgcolor="#22C55E",
                                    color="black",
                                    width=120,
                                    on_click=tentar_numero
                                ),
                                ft.ElevatedButton(
                                    "DESISTIR",
                                    icon=ft.Icons.CLOSE,
                                    bgcolor="#F97373", 
                                    color="black",
                                    width=120,
                                    on_click=derrota_final
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15
                        ),
                        ft.Container(height=20),
                        ft.ElevatedButton(
                            "Voltar ao Jogo",
                            icon=ft.Icons.ARROW_BACK,
                            bgcolor="#1E293B",
                            color="#E5E7EB",
                            on_click=derrota_final
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15
                )
            )
        )
        page.update()

    def derrota_final():
        minijogo_ativo["valor"] = False
        jogo_terminado["valor"] = True
        clean_page()
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        capa_derrota,
                        ft.Text(
                            f"A palavra era: {palavra_atual['palavra']}",
                            size=20,
                            color="#E5E7EB",
                        ),
                        ft.Container(height=30),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Tentar Outra Vez",
                                    icon=ft.Icons.REPLAY,
                                    bgcolor="#F97373",
                                    color="black",
                                    on_click=lambda e: reiniciar_nivel(nivel_atual),
                                ),
                                ft.ElevatedButton(
                                    "Menu",
                                    icon=ft.Icons.HOME,
                                    bgcolor="#38BDF8",
                                    color="black",
                                    on_click=lambda e: (
                                        gerar_novas_palavras_1_3(),
                                        gerar_novas_palavras_2(),
                                        abrir_pagina(modo_jogo),
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=20,
                border_radius=16,
                bgcolor="#020617",
            )
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
        if jogo_terminado["valor"] or minijogo_ativo["valor"]:
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

        # VITÓRIA - RESET VIDAS PARA PRÓXIMA PALAVRA (NÍVEL 3)
        if ganhou and not jogo_terminado["valor"]:
            indice_palavra["valor"] += 1

            if indice_palavra["valor"] < len(palavras_jogo):
                # RESET COMPLETO PARA NÍVEL 3
                vidas["valor"] = 6
                texto_vidas.value = f"Vidas: 6"
                texto_forca.value = forca[0]
                
                letras_usadas.clear()
                letras_erradas.clear()
                for botao in botoes_teclado.values():
                    botao.disabled = False
                palavra_atual["palavra"] = palavras_jogo[indice_palavra["valor"]]
                texto_erradas.value = ""
                atualizar_palavra()
            else:
                jogo_terminado["valor"] = True
                clean_page()
                page.add(
                    ft.Container(
                        content=ft.Column(
                            [
                                capa_vitoria,
                                ft.Text(
                                    "Parabéns! Adivinhaste todas as palavras!",
                                    size=20,
                                    color="#E5E7EB",
                                ),
                                ft.Container(height=30),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            "Jogar Outra Vez",
                                            icon=ft.Icons.REPLAY,
                                            bgcolor="#22C55E",
                                            color="black",
                                            on_click=lambda e: reiniciar_nivel(nivel_atual),
                                        ),
                                        ft.ElevatedButton(
                                            "Menu",
                                            icon=ft.Icons.HOME,
                                            bgcolor="#38BDF8",
                                            color="black",
                                            on_click=lambda e: (
                                                gerar_novas_palavras_1_3(),
                                                gerar_novas_palavras_2(),
                                                abrir_pagina(modo_jogo),
                                            ),
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=20,
                        border_radius=16,
                        bgcolor="#020617",
                    )
                )

        # DERROTA - MINIJOGO!
        if vidas["valor"] == 0 and not minijogo_ativo["valor"]:
            minijogo_numero()
            return

        page.update()

    # RESTO DO CÓDIGO (teclado, niveis, etc.) MANTIDO IGUAL
    def teclado():
        letras = "QWERTYUIOPASDFGHJKLZXCVBNM"
        botoes = []

        for letra in letras:
            botao = ft.ElevatedButton(
                letra,
                width=46,
                height=42,
                style=ft.ButtonStyle(
                    bgcolor={"": "#0F172A"},
                    color={"": "#E5E7EB"},
                ),
                on_click=lambda e, l=letra.lower(): clicar_letra(l),
            )
            botoes_teclado[letra.lower()] = botao
            botoes.append(botao)

        linha1 = ft.Row(botoes[0:10], alignment=ft.MainAxisAlignment.CENTER)
        linha2 = ft.Row(botoes[10:19], alignment=ft.MainAxisAlignment.CENTER)
        linha3 = ft.Row(botoes[19:26], alignment=ft.MainAxisAlignment.CENTER)

        return ft.Column(
            [linha1, linha2, linha3],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
        )

    def reiniciar_nivel(func_nivel):
        letras_usadas.clear()
        letras_erradas.clear()
        for botao in botoes_teclado.values():
            botao.disabled = False           
        botoes_teclado.clear()
        vidas["valor"] = 6
        jogo_terminado["valor"] = False
        minijogo_ativo["valor"] = False
        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = ""
        texto_forca.value = forca[0]
        indice_palavra["valor"] = 0
        
        if func_nivel == jogar1 or func_nivel == jogar2:
            gerar_novas_palavras_1_3()
        elif func_nivel == jogar3:
            gerar_novas_palavras_2()
        
        if func_nivel != camigos:
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
        vidas["valor"] = 6
        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = ""
        texto_forca.value = forca[0]
        layout_jogo(tema_1_3, voltar_destino=niveis)

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
        vidas["valor"] = 6
        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = ""
        texto_forca.value = forca[0]
        layout_jogo("Indisponível", voltar_destino=niveis)

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
        vidas["valor"] = 6  # 6 VIDAS POR PALAVRA
        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = ""
        texto_forca.value = forca[0]
        layout_jogo(tema_2, voltar_destino=niveis)

    def layout_jogo(tema, voltar_destino):
        page.add(
            ft.Container(
                bgcolor="#020617",
                border_radius=20,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            f"Tema: {tema}",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="#A5B4FC",
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                    content=texto_forca,
                                    padding=10,
                                    border_radius=12,
                                    bgcolor="#020617",
                                ),
                                ft.Column(
                                    [
                                        texto_palavra,
                                        texto_vidas,
                                        texto_erradas,
                                    ],
                                    spacing=5,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                        ft.Container(height=10),
                        teclado(),
                        ft.Container(height=10),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Voltar",
                                    icon=ft.Icons.ARROW_BACK,
                                    bgcolor="#1E293B",
                                    color="#E5E7EB",
                                    on_click=lambda e: abrir_pagina(voltar_destino),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )
        atualizar_palavra()

    # RESTO DAS FUNÇÕES (niveis, modo_jogo, camigos, capa_abertura) MANTIDAS EXATAMENTE IGUAIS
    def niveis():
        clean_page()
        page.add(
            ft.Container(
                bgcolor="#020617",
                border_radius=20,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "Níveis Clássicos",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color="#E5E7EB",
                        ),
                        ft.Text(
                            "Escolhe a dificuldade:",
                            size=15,
                            color="#9CA3AF",
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Nível 1",
                                    icon=ft.Icons.LOOKS_ONE,
                                    bgcolor="#22C55E",
                                    color="black",
                                    on_click=lambda e: abrir_pagina(jogar1),
                                ),
                                ft.ElevatedButton(
                                    "Nível 2",
                                    icon=ft.Icons.LOOKS_TWO,
                                    bgcolor="#FACC15",
                                    color="black",
                                    on_click=lambda e: abrir_pagina(jogar2),
                                ),
                                ft.ElevatedButton(
                                    "Nível 3",
                                    icon=ft.Icons.LOOKS_3,
                                    bgcolor="#F97373",
                                    color="black",
                                    on_click=lambda e: abrir_pagina(jogar3),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                        ft.Container(height=10),
                        ft.ElevatedButton(
                            "Voltar",
                            icon=ft.Icons.ARROW_BACK,
                            bgcolor="#1E293B",
                            color="#E5E7EB",
                            on_click=lambda e: abrir_pagina(modo_jogo),
                        ),
                    ],
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )

    def modo_jogo():
        letras_usadas.clear()
        letras_erradas.clear()
        botoes_teclado.clear()
        vidas["valor"] = 6
        jogo_terminado["valor"] = False
        minijogo_ativo["valor"] = False
        indice_palavra["valor"] = 0
        palavra_atual["palavra"] = ""
        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = ""
        texto_forca.value = forca[0]
        atualizar_palavra()
        clean_page()
        page.add(
            ft.Container(
                bgcolor="#020617",
                border_radius=20,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "Jogo da Forca",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color="#E5E7EB",
                        ),
                        ft.Text(
                            "Escolhe o modo de jogo:",
                            size=15,
                            color="#9CA3AF",
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Clássicos",
                                    icon=ft.Icons.GAMES,
                                    bgcolor="#22C55E",
                                    color="black",
                                    on_click=lambda e: abrir_pagina(niveis),
                                ),
                                ft.ElevatedButton(
                                    "Com Amigos",
                                    icon=ft.Icons.PEOPLE,
                                    bgcolor="#38BDF8",
                                    color="black",
                                    on_click=lambda e: abrir_pagina(camigos),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                    ],
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )

    def camigos():
        nonlocal nivel_atual
        nivel_atual = camigos
        clean_page()
        palavra = ft.TextField(
            label="Palavra para o teu amigo",
            width=350,
            bgcolor="#020617",
        )
        tema = ft.TextField(
            label="Tema da palavra",
            width=350,
            bgcolor="#020617",
        )

        def comecar():
            letras_usadas.clear()
            letras_erradas.clear()
            vidas["valor"] = 6
            minijogo_ativo["valor"] = False
            texto_vidas.value = f"Vidas: {vidas['valor']}"
            texto_erradas.value = ""
            texto_forca.value = forca[0]
            botoes_teclado.clear()
            palavra_atual["palavra"] = palavra.value.lower()
            clean_page()
            page.add(
                ft.Container(
                    bgcolor="#020617",
                    border_radius=20,
                    padding=20,
                    content=ft.Column(
                        [
                            ft.Text(
                                f"Tema: {tema.value}",
                                size=20,
                                color="#A5B4FC",
                                weight=ft.FontWeight.BOLD,
                            ),
                            texto_forca,
                            texto_palavra,
                            texto_vidas,
                            texto_erradas,
                            teclado(),
                            ft.Container(height=10),
                            ft.ElevatedButton(
                                "Voltar",
                                icon=ft.Icons.ARROW_BACK,
                                bgcolor="#1E293B",
                                color="#E5E7EB",
                                on_click=voltar,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                )
            )
            atualizar_palavra()

        page.add(
            ft.Container(
                bgcolor="#020617",
                border_radius=20,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "Jogar com Amigos",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color="#E5E7EB",
                        ),
                        ft.Text(
                            "Escreve a palavra e o tema para o teu amigo adivinhar.",
                            size=14,
                            color="#9CA3AF",
                        ),
                        ft.Container(height=10),
                        palavra,
                        tema,
                        ft.Container(height=10),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Começar",
                                    icon=ft.Icons.PLAY_ARROW,
                                    bgcolor="#22C55E",
                                    color="black",
                                    on_click=comecar,
                                ),
                                ft.ElevatedButton(
                                    "Voltar",
                                    icon=ft.Icons.ARROW_BACK,
                                    bgcolor="#1E293B",
                                    color="#E5E7EB",
                                    on_click=lambda e: abrir_pagina(modo_jogo),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )

    def capa_abertura():
        clean_page()
        page.add(
            ft.Container(
                bgcolor="#020617",
                border_radius=24,
                padding=24,
                content=ft.Column(
                    [
                        titulo_forca,
                        ft.Text(
                            "Tenta adivinhar a palavra antes de seres enforcado!",
                            size=16,
                            color="#9CA3AF",
                        ),
                        ft.Container(height=20),
                        ft.ElevatedButton(
                            "COMEÇAR",
                            icon=ft.Icons.PLAY_ARROW,
                            width=220,
                            height=50,
                            bgcolor="#22C55E",
                            color="black",
                            style=ft.ButtonStyle(
                                shape={
                                    "": ft.RoundedRectangleBorder(radius=12),
                                },
                            ),
                            on_click=lambda e: abrir_pagina(modo_jogo),
                        ),
                    ],
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,
                ),
            )
        )

    capa_abertura()

ft.run(main)
