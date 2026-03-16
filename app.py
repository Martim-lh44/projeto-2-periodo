import flet as ft
from vt2 import tema_1_3, palavras_3_1, palavras2, tema_2

    
def main(page: ft.Page):
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

    def clean_page():
        page.controls.clear()
        page.update()
    
    def abrir_pagina(funcao):
        historico.append(funcao)
        funcao()

    def voltar(e):
        if len(historico) > 1:
            historico.pop()  # remove a atual
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
                page.add(ft.Text("GANHASTE O JOGO!", size=25, color="green"))
                jogo_terminado["valor"] = True
        if vidas["valor"] == 0:
            page.add(ft.Text(f"PERDESTE! Palavra: {palavra_atual['palavra']}", size=25, color="red"))
            jogo_terminado["valor"] = True
        page.update()

    def teclado():
        letras = "QWERTYUIOPASDFGHJKLZXCVBNM"
        botoes = []
        for letra in letras:
                botao= ft.ElevatedButton(
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

    def reset_jogo():
        letras_usadas.clear()
        letras_erradas.clear()
        botoes_teclado.clear()
        vidas["valor"] = 6
        jogo_terminado["valor"] = False
        texto_vidas.value = f"Vidas: {vidas['valor']}"
        texto_erradas.value = ""
        texto_forca.value = forca[0]

    def jogar1():
        clean_page()
        reset_jogo()
        palavra_atual["palavra"] = palavras_3_1[0]
        print("Tema:", tema_1_3)
        print("Palavra:", palavra_atual["palavra"])
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
        clean_page()
        reset_jogo()
        palavra_atual["palavra"] = palavras_3_1[0]
        print("Palavra:", palavra_atual["palavra"])
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
        clean_page()
        reset_jogo()
        palavras_jogo.clear()
        palavras_jogo.extend(palavras2)
        indice_palavra["valor"] = 0
        palavra_atual["palavra"] = palavras_jogo[indice_palavra["valor"]]
        print("Tema:", tema_2)
        print("Palavra:", palavra_atual["palavra"])
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
                        ft.Text("Escolha o nível", size=15,),
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

    def camigos():
        clean_page()
        palavra = ft.TextField(label="Escreve a palavra para o teu amigo adivinhar")
        tema = ft.TextField(label="Escreve o tema da palavra")
        def comecar(e):
            reset_jogo()
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

    def modo_jogo():
        clean_page()
        page.add(
            ft.Column(
                    [
                        ft.Text("Jogo da Forca", size=22, weight=ft.FontWeight.BOLD),
                        ft.Text("Escolha o modo de jogo", size=15,),
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

    page.add(
        ft.Column(
                [
                    ft.Text("Jogo da Forca", size=22, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.ElevatedButton("Começar", on_click=lambda e: abrir_pagina(modo_jogo))
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
ft.run(main)
