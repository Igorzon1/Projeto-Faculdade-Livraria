import flet as ft

class label_text(ft.Text):
    def __init__(self,text):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_100
        self.color = ft.colors.BLUE_100
        self.text = text