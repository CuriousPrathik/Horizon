import flet as ft

def main(page: ft.page):
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.DARK


    # add text
    t = ft.Text(value="Today", color="grey")
    page.controls.append(t)
    page.update()

    
    class CalcButton(ft.ElevatedButton):
        def __init__(self, text, expand=1):
            super().__init__()
            self.text = text
            self.expand = expand
    
    class DigitButton(CalcButton):
        def __init__(self, text, expand=1):
            CalcButton.__init__(self, text, expand)
            self.bgcolor = ft.colors.WHITE70
            self.color = ft.colors.BLACK

    class ActionButton(CalcButton):
        def __init__(self, text):
            CalcButton.__init__(self, text)
            self.bgcolor = ft.colors.ORANGE
            self.color = ft.colors.WHITE



    volume_of_water = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, width=100,)

    page.add(
        ft.Container(
            width=500,
            bgcolor=ft.colors.BLUE_GREY,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=
                    [
                        ft.Row(controls=[volume_of_water,ActionButton(text="+")]),
                        ft.Row(
                            controls=[
                                DigitButton(text="250 ml"),
                                DigitButton(text="500 ml"),
                                DigitButton(text="750 ml"),
                                DigitButton(text="1000 ml"),
                            ]
                        ),
                    ]
            )
        )
    )


    class CalcButton(ft.ElevatedButton):
        def __init__(self, text, expand=1):
            super().__init__()
            self.text = text
            self.expand = expand
    
    class DigitButton(CalcButton):
        def __init__(self, text, expand=1):
            CalcButton.__init__(self, text, expand)
            self.bgcolor = ft.colors.WHITE70
            self.color = ft.colors.BLACK

    class ActionButton(CalcButton):
        def __init__(self, text):
            CalcButton.__init__(self, text)
            self.bgcolor = ft.colors.ORANGE
            self.color = ft.colors.WHITE
            
class CalculatorApp(ft.Container):
    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()

        self.volume_of_water = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, width=100,)
        self.width = 500
        self.bgcolor = ft.colors.BLUE_GREY
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.volume_of_water,ActionButton(text="+")], alignment="end"),
                ft.Row(
                    controls=[
                            DigitButton(text="250 ml"),
                            DigitButton(text="500 ml"),
                            DigitButton(text="750 ml"),
                            DigitButton(text="1000 ml"),

                    ]
                ),
            ]
        )

def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


ft.app(target=main)