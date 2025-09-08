import flet as ft
from src.models.data import SharedData
from src.services.view_services import append_person, on_generate


def config_view(page: ft.Page, shared_data: SharedData):
    alquiler = ft.TextField(label='Alquiler', input_filter=ft.NumbersOnlyInputFilter())

    show_as = ft.Dropdown(
        label='Show as',
        options=[
            ft.DropdownOption(key='Peso', text='$'),
            ft.DropdownOption(key='Percentage', text='%')
            ],
        #expand=True
        )

    persons_column = ft.Column(spacing=20)
    persons_inputs = []

    # 3 personas por defecto
    for _ in range(3):
        append_person(
            page=page,
            persons_inputs=persons_inputs,
            persons_column=persons_column
        )

    boton_agregar = ft.ElevatedButton("Agregar persona", icon=ft.Icons.ADD, on_click=lambda e: append_person(
        page, persons_inputs, persons_column, e
    ))
    boton_generar = ft.ElevatedButton("Generar Gráfico", icon=ft.Icons.IMAGE ,on_click=lambda e: on_generate(
        page, shared_data, show_as, alquiler, persons_inputs, e
    ))

    return ft.Column([
        ft.Row([
            alquiler,
            boton_agregar,
            show_as
        ], expand=True),
        persons_column,
        boton_generar,
    ],
    scroll=ft.ScrollMode.AUTO,
    spacing=20
    )
