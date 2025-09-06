import flet as ft
from flet.plotly_chart import PlotlyChart
from src.services.chart_generator_service import calculate_charts


def Config_view(page: ft.Page):
    page.title = "Cálculo del Alquiler"
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = True
    page.window_maximizable = True
    page.window_minimizable = True

    page.bgcolor = ft.Colors.GREY_300

    alquiler = ft.TextField(label='Sueldo', input_filter=ft.NumbersOnlyInputFilter())

    persona1_nombre = ft.TextField(label='Nombre', input_filter=ft.TextOnlyInputFilter())
    persona1_sueldo = ft.TextField(label='Sueldo', input_filter=ft.NumbersOnlyInputFilter())

    persona2_nombre = ft.TextField(label='Nombre', input_filter=ft.TextOnlyInputFilter())
    persona2_sueldo = ft.TextField(label='Sueldo', input_filter=ft.NumbersOnlyInputFilter())

    persona3_nombre = ft.TextField(label='Nombre', input_filter=ft.TextOnlyInputFilter())
    persona3_sueldo = ft.TextField(label='Sueldo', input_filter=ft.NumbersOnlyInputFilter())

    valores = {
        persona1_nombre.value: persona1_sueldo.value,
        persona2_nombre.value: persona2_sueldo.value,
        persona3_nombre.value: persona3_sueldo.value,
    }

    chart_container = ft.Column()

    boton = ft.ElevatedButton(
        'Generar Gráfico',
        on_click=lambda e: generate_plot(
                            page,
                            valores,
                            alquiler,
                            chart_container
                            )
                        )

    page.add(
        ft.Column([
            alquiler,
            ft.Row([
                persona1_nombre,
                persona1_sueldo
            ], expand=True),
            ft.Row([
                persona2_nombre,
                persona2_sueldo
            ], expand=True),
            ft.Row([
                persona3_nombre,
                persona3_sueldo
            ], expand=True),
            boton,
            chart_container
        ],
        expand=True
        )
    )
