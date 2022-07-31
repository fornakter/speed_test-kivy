from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from only_test import speed_test

class MainWidget(BoxLayout):
    status_label = StringProperty("Status: waiting")

    def on_button_click(self):
        self.status_label = "Status: klick"
        try:
            speed_test()
        except Exception as e:
            print(e)


class MainMenu(App):
    pass


if __name__ == '__main__':
    MainMenu().run()
