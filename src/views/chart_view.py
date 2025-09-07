import flet as ft
from flet.plotly_chart import PlotlyChart
from src.services.chart_generator_service import calculate_charts
from src.models.data import SharedData


def chart_view(page: ft.Page, shared_data: SharedData, *args):
    fig = calculate_charts(
        alquiler=shared_data.alquiler,
        values=shared_data.values
    )

    return ft.Column(
            controls=[PlotlyChart(fig, expand=True)],
            expand=True
            )
