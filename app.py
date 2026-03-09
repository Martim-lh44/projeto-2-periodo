import flet as ft
from variaveis import nivel_1_3, nivel_2
    
def main(page: ft.Page):
    page.title = "Jogo da Forca"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    def clean_page():
        page.controls.clear()
        page.update()

    def voltar():
        page.views.pop()
        page.update()

    def teclado():
        letras = "QWERTYUIOPASDFGHJKLZXCVBNM"
        linha1 = ft.Row([ft.ElevatedButton(letra) for letra in letras[0:10]], alignment=ft.MainAxisAlignment.CENTER)
        linha2 = ft.Row([ft.ElevatedButton(letra) for letra in letras[10:19]], alignment=ft.MainAxisAlignment.CENTER)
        linha3 = ft.Row([ft.ElevatedButton(letra) for letra in letras[19:26]], alignment=ft.MainAxisAlignment.CENTER)
        return ft.Column(
            [linha1, linha2, linha3],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.END
            )

    def jogar0(): 
        clean_page() 
        page.add(
            teclado()
        )

    def jogar1():
        clean_page()
        nivel_1_3() 
        palavras_jogo = nivel_1_3()
        page.add(
            teclado(),
            ft.Text(letra if letra in [" ", "-"] else "_" for letra in palavras_jogo)
        )

    def jogar2(): 
        clean_page()
        nivel_2() 
        page.add(
            teclado()
        )
        

    def jogar3(): 
        clean_page()
        nivel_1_3() 
        page.add(
            teclado()
        )

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

    def amigavel():
        clean_page()
        classico= False
        palavra = ft.TextField(label="Escreve a palavra para o teu amigo adivinhar", keyboard_type=ft.KeyboardType.TEXT)
        tema = ft.TextField(label="Escreve o tema da palavra",keyboard_type=ft.KeyboardType.TEXT)
        page.add(
             ft.Text("Jogo da Forca", size=22, weight=ft.FontWeight.BOLD),
            ft.Text("Escolhe a palavra", size=15,),
            palavra,
            tema,
            ft.ElevatedButton("Começar", on_click=jogar0)
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
                                ft.ElevatedButton("Amigável", on_click=amigavel),
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
