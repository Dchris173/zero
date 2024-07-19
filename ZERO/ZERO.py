"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

class State(rx.State):
    

    ...
def index() -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.vstack(
                rx.text('Welcome :)'),
                rx.input(placeholder='Usuario'),
                rx.input(placeholder='Conttaseña', type='password'),
                rx.button('Ingresar')
            )
        )
    )

app = rx.App()
app.add_page(index)