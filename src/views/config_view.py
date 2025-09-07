import flet as ft
from src.models.data import SharedData


def config_view(page: ft.Page, shared_data: SharedData):
    alquiler = ft.TextField(label='Alquiler', input_filter=ft.NumbersOnlyInputFilter())

    personas_column = ft.Column(spacing=20)
    personas_inputs = []

    def agregar_persona(e=None):
        nombre_field = ft.TextField(label="Nombre", input_filter=ft.TextOnlyInputFilter(), expand=True)
        sueldo_field = ft.TextField(label="Sueldo", input_filter=ft.NumbersOnlyInputFilter(), expand=True)

        row = ft.Row([nombre_field, sueldo_field], expand=True)
        personas_inputs.append((nombre_field, sueldo_field))
        personas_column.controls.append(row)
        page.update()

    # generar gráfico y guardar en shared_data
    def on_generate(e):
        shared_data.alquiler = float(alquiler.value or 0)
        shared_data.values = {}

        for nombre_field, sueldo_field in personas_inputs:
            nombre = nombre_field.value.strip()
            sueldo = float(sueldo_field.value or 0)
            if nombre:
                shared_data.values[nombre] = sueldo

        if shared_data.values and alquiler.value:
            print("Navigating to:", page.route, "Views stack:", [v.route for v in page.views])
            page.go("/chart")
        else:
            page.open(ft.SnackBar(ft.Text("Debe ingresar al menos una persona y el alquiler.")))
            page.update()

    # 3 personas por defecto
    for _ in range(3):
        agregar_persona()

    boton_agregar = ft.ElevatedButton("Agregar persona", icon=ft.Icons.ADD, on_click=agregar_persona)
    boton_generar = ft.ElevatedButton("Generar Gráfico", icon=ft.Icons.IMAGE ,on_click=on_generate)

    return ft.Column([
        alquiler,
        boton_agregar,
        personas_column,
        boton_generar,
    ],
    scroll=ft.ScrollMode.AUTO,
    spacing=20
    )
