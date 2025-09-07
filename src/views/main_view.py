import flet as ft
from src.views.config_view import config_view
from src.views.chart_view import chart_view
from src.models.data import SharedData


def main(page: ft.Page):
    page.title = "Cálculo del Alquiler"
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = True
    page.window_maximizable = True
    page.window_minimizable = True
    page.window.center()

    page.bgcolor = ft.Colors.GREY_300

    shared_data = SharedData()

    def route_change(e: ft.RouteChangeEvent):
        if page.views and page.views[-1].route == page.route:
            return
        
        page.views.clear()

        # vista formilario
        page.views.append(
            ft.View(
                "/",
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.AppBar(title=ft.Text("Configuración")),
                    config_view(page, shared_data),
                ],
                can_pop=False
            )
        )

        # vista del gráfico
        if page.route == "/chart":
            page.views.append(
                ft.View(
                    "/chart",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Gráfico"),
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/"))
                        ),
                        chart_view(page, shared_data),
                    ]
                )
            )

        page.update()

    def view_pop(view):
        if page.views:
            page.views.pop()
            if page.views:
                top_view = page.views[-1]
                page.go(top_view.route) 

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
