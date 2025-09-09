import flet as ft
from src.models.data import SharedData


def append_person(
        page: ft.Page,
        persons_inputs: list,
        persons_column: ft.Column,
        e=None
    ) -> None:
    nombre_field = ft.TextField(label="Nombre", input_filter=ft.TextOnlyInputFilter(), expand=True)
    sueldo_field = ft.TextField(label="Sueldo", input_filter=ft.NumbersOnlyInputFilter(), expand=True)

    row = ft.Row([nombre_field, sueldo_field], expand=True)
    persons_inputs.append((nombre_field, sueldo_field))
    persons_column.controls.append(row)
    page.update()


def on_generate(
        page: ft.Page,
        shared_data: SharedData,
        show_as: ft.Dropdown,
        alquiler: ft.TextField,
        persons_inputs: list,
        e
    ) -> None:
    shared_data.alquiler = float(alquiler.value or 0)
    shared_data.values = {}
    shared_data.show_as = show_as.value

    for nombre_field, sueldo_field in persons_inputs:
        nombre = nombre_field.value.strip()
        sueldo = float(sueldo_field.value or 0)
        if nombre:
            shared_data.values[nombre] = sueldo

    if shared_data.values and alquiler.value:
        page.go("/chart")
    else:
        page.open(ft.SnackBar(ft.Text("Debe ingresar al menos una persona y el alquiler.")))
        page.update()
