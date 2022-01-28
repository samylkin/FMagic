from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class FMagicApp(MDApp):
    def build(self):
        return MDLabel(text="The FMagic has you", halign="center")


FMagicApp().run()
