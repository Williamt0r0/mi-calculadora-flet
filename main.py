import flet as ft
from flet import Colors, alignment

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Calculadora Flet"
    page.window_width = 350
    page.window_height = 500
    page.bgcolor = Colors.BLACK
    page.padding = 20

    # Pantalla donde se muestran los números
    display = ft.Text(value="0", color=Colors.WHITE, size=45)

    # Función que maneja todos los clics
    def button_clicked(e):
        boton = e.control.text
        
        if boton == "AC":
            display.value = "0"
        elif boton == "=":
            try:
                # eval() realiza la operación matemática
                # Reemplazamos 'x' por '*' para que Python entienda la multiplicación
                formula = display.value.replace("x", "*").replace("÷", "/")
                display.value = str(round(eval(formula), 4))
            except:
                display.value = "Error"
        else:
            if display.value == "0" or display.value == "Error":
                display.value = boton
            else:
                display.value += boton
        
        page.update()

    # Función para crear botones rápido y con el mismo estilo
    def btn(texto, color_fondo=Colors.GREY_900, color_texto=Colors.WHITE):
        return ft.ElevatedButton(
            text=texto,
            bgcolor=color_fondo,
            color=color_texto,
            on_click=button_clicked,
            expand=True,  # Hace que el botón ocupe el espacio disponible
            height=70,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
        )

    # Añadimos los elementos a la página
    page.add(
        # Contenedor para el resultado
        ft.Container(
            content=display,
            alignment=alignment.center_right,
            padding=10,
            height=100
        ),
        # Filas de botones
        ft.Column([
            ft.Row([btn("AC", Colors.RED_700), btn("÷", Colors.ORANGE)]),
            ft.Row([btn("7"), btn("8"), btn("9"), btn("x", Colors.ORANGE)]),
            ft.Row([btn("4"), btn("5"), btn("6"), btn("-", Colors.ORANGE)]),
            ft.Row([btn("1"), btn("2"), btn("3"), btn("+", Colors.ORANGE)]),
            ft.Row([btn("0"), btn("."), btn("=" , Colors.GREEN_800)]),
        ], spacing=10)
    )

ft.app(target=main)
