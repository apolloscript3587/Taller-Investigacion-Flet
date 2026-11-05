import flet as ft

class ContadorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.contador = 0

        self.page.title = "Contador interactivo"
        self.page.window.width = 420
        self.page.window.height = 420
        self.page.padding = 24

        self.valor = ft.Text(
            value="0",
            size=56,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_700
        )

        self.mensaje = ft.Text(
            "Presiona un botón para comenzar."
        )

        self.boton_sumar = ft.Button(
            content="Incrementar",
            icon=ft.Icons.ADD,
            on_click=self.incrementar
        )

        self.boton_restar = ft.Button(
            content="Disminuir",
            icon=ft.Icons.REMOVE,
            on_click=self.disminuir
        )

        self.boton_reiniciar = ft.OutlinedButton(
            content="Reiniciar",
            icon=ft.Icons.REFRESH,
            on_click=self.reiniciar
        )

        self.page.add(
            ft.Column(
                controls=[
                    ft.Text(
                        "CONTADOR INTERACTIVO",
                        size=22,
                        weight=ft.FontWeight.BOLD
                    ),
                    self.valor,
                    ft.Row(
                        controls=[
                            self.boton_restar,
                            self.boton_sumar
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    self.boton_reiniciar,
                    self.mensaje
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=18
            )
        )

    def actualizar_interfaz(self, mensaje):
        self.valor.value = str(self.contador)
        self.mensaje.value = mensaje
        self.page.update()

    def incrementar(self, e):
        self.contador += 1
        self.actualizar_interfaz(
            "¡Se incrementó el contador!"
        )

    def disminuir(self, e):
        self.contador -= 1
        self.actualizar_interfaz(
            "El contador disminuyó."
        )

    def reiniciar(self, e):
        self.contador = 0
        self.actualizar_interfaz(
            "El contador volvió a cero."
        )

def main(page: ft.Page):
    ContadorApp(page)

if __name__ == "__main__":
    ft.run(main)
