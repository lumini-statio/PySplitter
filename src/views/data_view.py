import flet as ft
from src.models.data import SharedData
from src.services.view_services import calculate_data


async def chart_view(page: ft.Page, shared_data: SharedData, *args):
    data_rows = []

    sign = shared_data.show_as

    if 'Dolar' in sign:
        sign = '$'
    elif 'Euro' in sign:
        sign = '€'

    all_items = calculate_data(shared_data)

    for name, salary, due_money, percentage_due in all_items:
        data_rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(name)),
                ft.DataCell(ft.Text(f"{sign}{salary}")),
                ft.DataCell(ft.Text(f"{sign}{due_money}")),
                ft.DataCell(ft.Text(f"%{percentage_due}")),
            ])
        )
    
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Name", expand=True)),
            ft.DataColumn(ft.Text("Salary", expand=True)),
            ft.DataColumn(ft.Text("Due Money", expand=True)),
            ft.DataColumn(ft.Text("Due Percentage", expand=True)),
        ],
        rows=data_rows,
        expand=True,
        horizontal_margin=20,
        column_spacing=20,
    )

    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ListTile(
                        title=ft.Text("Distribution Table", weight=ft.FontWeight.BOLD),
                    ),
                    ft.Divider(),
                    ft.Container(
                        content=ft.ListView(
                            controls=[data_table],
                            expand=True,
                        ),
                        padding=20,
                        expand=True,
                    ),
                ],
                expand=True,
            ),
            margin=20,
            expand=True,
        ),
        expand=True,
    )