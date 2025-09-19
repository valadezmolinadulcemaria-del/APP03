import flet as ft
import math


def main(page: ft.Page):
    page.title= "calculadora siemple"
    page.bgcolor=ft.Colors.RED_100
    
   #titulo
   titulo=ft.Text(
       "🥬 caculadora basica vv",
        size=28,
        color=ft.Colors.RED_700
        text_align="center",
        weight=="bold"
   )
   
   #entradas
    num1 = ft.TextField(
        label="Número 1",
        width=200,
        text_style=ft.TextStyle(color=ft.Colors. YELLOW_100)
    )
    num2 = ft. TextField(
        label="Número 2",
        width=200,
    text_style=ft.TextStyle(color=ft.Colors.YELLOW_100)
    )
    
    resultado = ft.Text(
        value="Resultado: ",
        size=20,
        color=ft.Colors.YELLOW_100,
        text_align="center"
    )

   
    page.add()


ft.app(main)
