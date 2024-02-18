from sufficient.frames import *


class App:
    name = "Redirect Buttons"
    description = "Demo of redirect button"
    image = "{uri}/static/home.svg"
    uri = "{uri}"
    start = "PageHome"


class PageHome:
    def view(self, action: Action, result: ActionResult):
        SVG = f'''<svg width="640" height="336" xmlns="http://www.w3.org/2000/svg"><textPageHome</text><style></svg>'''
        return SvgImageView.from_string(SVG)

    def btn_next(self, action: Action):
        return "PageNext"

    def goto_github(self, action: Action):
        return "https://github.com"


class PageNext:
    def view(self, action: Action, result: ActionResult):
        SVG = f'''<svg width="640" height="336" xmlns="http://www.w3.org/2000/svg"><text>PageNext</text><style></svg>'''
        return SvgImageView.from_string(SVG)

    def btn_prev(self, action: Action):
        return "PageHome"

    def btn_refresh(self, action: Action):
        return "PageNext"
