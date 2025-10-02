import flet as ft
from src.models.data import SharedData
from src.services.view_services import append_person, on_generate


def config_view(page: ft.Page, shared_data: SharedData):
    alquiler = ft.TextField(label='Expense',
                            input_filter=ft.NumbersOnlyInputFilter(),
                            border_color=ft.Colors.WHITE)

    show_as = ft.Dropdown(
        label='Show as',
        options=[
            ft.DropdownOption(key='Dolar', text='$'),
            ft.DropdownOption(key='Euro', text='€'),
            ft.DropdownOption(key='Yen', text='¥'),
            ft.DropdownOption(key='Percentage', text='%'),
            ],
        value='Dolar',
        border_color=ft.Colors.WHITE
        )

    persons_column = ft.Column(spacing=20)
    persons_inputs = []

    # 3 persons default
    for _ in range(3):
        append_person(
            page=page,
            persons_inputs=persons_inputs,
            persons_column=persons_column
        )

    boton_agregar = ft.ElevatedButton("Add Person", icon=ft.Icons.ADD, on_click=lambda e: append_person(
        page, persons_inputs, persons_column, e
    ))
    boton_generar = ft.ElevatedButton("Generate Chart", icon=ft.Icons.IMAGE ,on_click=lambda e: on_generate(
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
