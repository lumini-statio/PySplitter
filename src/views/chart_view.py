import flet as ft
import plotly.graph_objs as go
from flet.plotly_chart import PlotlyChart
from src.services.chart_generator_service import calculate_charts
from src.models.data import SharedData


def chart_view(page: ft.Page, shared_data: SharedData, *args):
    fig: go.Figure = calculate_charts(
        alquiler=shared_data.alquiler,
        values=shared_data.values,
        show_as=shared_data.show_as
    )

    return ft.Column(
            controls=[PlotlyChart(fig, expand=True, isolated=True)],
            expand=True
            )
