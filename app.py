import flet as ft
from vt2 import tema_1_3, palavras_3_1, tema_2, palavras2

    
def main(page: ft.Page):
    page.title = "Jogo da Forca"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    indice_palavra = {"valor": 0}
    palavras_jogo = []
    palavra_atual = {"palavra": ""}
    letras_usadas = []
    texto_palavra = ft.Text(size=30, weight=ft.FontWeight.BOLD)
    palavras_jogo = []
    indice_palavra = {"valor": 0}
    jogar_again = True
    
    def clean_page():
        page.controls.clear()
        page.update()

    def voltar():
        page.views.pop()
        page.update()

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
        if letra not in letras_usadas:
            letras_usadas.append(letra)
        atualizar_palavra()
        # verificar vitória
        ganhou = True
        for l in palavra_atual["palavra"]:
            if l not in letras_usadas and l not in [" ", "-"]:
                ganhou = False
        if ganhou:
            indice_palavra["valor"] += 1
            if indice_palavra["valor"] < len(palavras_jogo):
                letras_usadas.clear()
                palavra_atual["palavra"] = palavras_jogo[indice_palavra["valor"]]
                page.add(ft.Text("Próxima palavra!", size=20))
                atualizar_palavra()
            else:
                page.add(ft.Text("GANHASTE O JOGO!", size=25, color="green"))

    def teclado():
        letras = "QWERTYUIOPASDFGHJKLZXCVBNM"
        botoes = []
        for letra in letras:
            botoes.append(
                ft.ElevatedButton(
                    letra,
                    on_click=lambda e, l=letra.lower(): clicar_letra(l)
                )
            )

        linha1 = ft.Row(botoes[0:10], alignment=ft.MainAxisAlignment.CENTER)
        linha2 = ft.Row(botoes[10:19], alignment=ft.MainAxisAlignment.CENTER)
        linha3 = ft.Row(botoes[19:26], alignment=ft.MainAxisAlignment.CENTER)

        return ft.Column(
            [linha1, linha2, linha3],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def jogar0(): 
        clean_page() 
        page.add(
            teclado()
        )

    def jogar1():
        clean_page()
        letras_usadas.clear()
        palavra_atual["palavra"] = palavras_3_1[0]
        print("Tema:", tema_1_3)
        print("Palavra:", palavra_atual["palavra"])
        page.add(
            ft.Text(f"Tema: {tema_1_3}", size=20),
            texto_palavra,
            teclado()
        )
        atualizar_palavra()

    def jogar2(): 
        clean_page()
        letras_usadas.clear()
        palavra_atual["palavra"] = palavras_3_1[0]
        print("Palavra:", palavra_atual["palavra"])
        page.add(
            ft.Text(f"Tema: Indisponível", size=20),
            texto_palavra,
            teclado()
        )
        atualizar_palavra()
        

    def jogar3(): 
        clean_page()
        letras_usadas.clear()
        palavras_jogo.clear()
        palavras_jogo.extend(palavras2)
        indice_palavra["valor"] = 0
        palavra_atual["palavra"] = palavras_jogo[indice_palavra["valor"]]
        print("Tema:", tema_1_3)
        print("Palavra:", palavra_atual["palavra"])
        page.add(
            ft.Text(f"Tema: {tema_1_3}", size=20),
            texto_palavra,
            teclado()
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
                                ft.ElevatedButton("Nível 1", on_click=jogar1),
                                ft.ElevatedButton("Nível 2", on_click=jogar2),
                                ft.ElevatedButton("Nível 3", on_click=jogar3)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
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
            letras_usadas.clear()
            palavra_atual["palavra"] = palavra.value.lower()
            clean_page()
            page.add(
                ft.Text(f"Tema: {tema.value}", size=20),
                texto_palavra,
                teclado()
            )
            atualizar_palavra()
        page.add(
            ft.Text("Jogo da Forca", size=22, weight=ft.FontWeight.BOLD),
            ft.Text("Escolhe a palavra", size=15),
            palavra,
            tema,
            ft.ElevatedButton("Começar", on_click=comecar)
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
                                ft.ElevatedButton("Clássicos", on_click=niveis),
                                ft.ElevatedButton("Com Amigos", on_click=camigos),
                                ft.ElevatedButton("Voltar", on_click=voltar)
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
                            ft.ElevatedButton("Começar", on_click=modo_jogo)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
ft.run(main)
