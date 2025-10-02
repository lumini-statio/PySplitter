import flet as ft
from flet.plotly_chart import PlotlyChart
from src.services.chart_generator_service import calculate_charts
from src.models.data import SharedData
import asyncio


async def chart_view(page: ft.Page, shared_data: SharedData, *args):
    await asyncio.sleep(0.1)
    
    chart_container = ft.Container(
        content=ft.Column(
            [
                ft.ProgressRing(width=50, height=50),
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

    page.update()

    async def generate_chart():
        await asyncio.sleep(0.5)
        try:
            fig = calculate_charts(
                alquiler=shared_data.alquiler,
                values=shared_data.values,
                show_as=shared_data.show_as
            )
            
            plotly_chart = PlotlyChart(fig, expand=True, isolated=True)
            
            chart_container.content = plotly_chart
            chart_container.update()
            
        except Exception as e:
            chart_container.content = ft.Text(f"Error: {str(e)}", color="red")
            chart_container.update()
    
    asyncio.create_task(generate_chart())
    
    return column