import flet as ft
from flet.plotly_chart import PlotlyChart
from src.services.chart_generator_service import calculate_charts


def chart(page: ft.Page, values: dict, *args):
    page.title = "Cálculo del Alquiler"
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = True
    page.window_maximizable = True
    page.window_minimizable = True
    page.window.center()

    page.bgcolor = ft.Colors.GREY_300


def generate_plot(page: ft.Page, valores, alquiler, container: ft.Column, *args, **kwargs):
    fig = calculate_charts(alquiler=alquiler, values=valores)

    container.controls.clear()
    container.controls.append(PlotlyChart(fig, expand=True))
    page.update()