import flet as ft
from flet.plotly_chart import PlotlyChart
from src.services.chart_generator_service import calculate_charts
from src.models.data import SharedData


async def chart_view(page: ft.Page, shared_data: SharedData, *args):
    chart_container = ft.Container(
        content=ft.Column(
            [
                ft.ProgressRing(width=50, height=50), # initialize it whit a progress ring
                ft.Text("Generando gráfico...", size=16)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        expand=True
    )
    
    column = ft.Column(
        controls=[chart_container],
        expand=True
    )

    async def generate_chart():
        try:
            fig = calculate_charts(
                alquiler=shared_data.alquiler,
                values=shared_data.values,
                show_as=shared_data.show_as
            )
            
            plotly_chart = ft.Column([
                PlotlyChart(fig, expand=True, isolated=True)
            ])
            
            chart_container.content = plotly_chart
            chart_container.update()
            
        except Exception as e:
            chart_container.content = ft.Text(f"Error al generar el gráfico: {str(e)}", color="red")
            chart_container.update()
    
    page.run_task(generate_chart)
    
    return column