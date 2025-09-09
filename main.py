from src.views.main_view import main
import flet as ft
import asyncio


if __name__ == '__main__':
    asyncio.run(ft.app_async(target=main))