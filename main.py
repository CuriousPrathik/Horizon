import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text


class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE



class CalculatorApp(ft.Container):
        # add text

    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()
        self.reset()


        
        self.volume_of_water = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, width=100,)
        self.width = 500
        self.bgcolor = ft.colors.BLUE_GREY
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.volume_of_water,ActionButton(text="+",button_clicked=self.button_clicked)], alignment="end"),
                ft.Row(
                    controls=[
                        DigitButton(text="250",button_clicked=self.button_clicked),
                        DigitButton(text="500",button_clicked=self.button_clicked),
                        DigitButton(text="750",button_clicked=self.button_clicked),
                        DigitButton(text="1000",button_clicked=self.button_clicked),
                    ]
                ),
            ]
        )


    def button_clicked(self, e):
        data = e.control.data
        print(f"Button clicked with data = {data}")

        if data in ("250", "500", "750", "1000"):
            if self.volume_of_water.value == "0" or self.new_operand == True:
                self.volume_of_water.value = data
                self.new_operand = False
            else:
                self.volume_of_water.value = self.volume_of_water.value + data

        elif data in ("+"):
            self.volume_of_water.value = self.calculate(
                self.operand1, float(self.volume_of_water.value), self.operator
            )
            self.operator = data
            if self.volume_of_water.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.volume_of_water.value)
            self.new_operand = True

        self.update()


    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Horizon"
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.DARK


    # add text
    t = ft.Text(value="Current Hydration", color="grey")
    page.controls.append(t)
    page.update()
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


ft.app(target=main)