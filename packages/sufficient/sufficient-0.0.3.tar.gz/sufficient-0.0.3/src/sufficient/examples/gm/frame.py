from sufficient.frames import *


class App:
    name = "Sufficient-py"
    description = "A framework for creating Frame apps in an intuitive and declarative manner"
    image = "{uri}/static/home.png"
    uri = "{uri}"
    start = "PageHome"


class PageHome:
    def view(self, action: Action, result: ActionResult):
        return BinaryImageView.from_file("home.png")

    def btn_features(self, action: Action):
        c = FarcasterClient()
        actor_user = c.neynar_get_user(action.actor)
        return "PageDemo", ActionResult(data=actor_user)

    def btn_concepts(self, action: Action):
        return "PageConcepts"


class PageDemo:
    def view(self, action: Action, result: ActionResult):
        if action.page == "PageDemo":
            if action.action == 1:
                return SvgImageView.from_template("reactions.svg", result)
            elif action.action == 2:
                return SvgImageView.from_template("token_infos.svg", result)
            elif action.action == 3:
                return SvgImageView.from_template("render_methods.svg", result)
        else:
            return SvgImageView.from_template("greeting.svg", result)

    def btn_get_reactions(self, action: Action):
        c = FarcasterClient()
        cast_actions = c.neynar_get_cast_actions(action.cast, action.actor)
        return "PageDemo", ActionResult(data=cast_actions)

    def btn_get_tokens(self, action: Action):
        return "PageDemo"

    def btn_render_methods(self, action: Action):
        return "PageDemo"

    def btn_declarative(self, action: Action):
        return "PageConcepts"


class PageConcepts:
    def view(self, action: Action, result: ActionResult):
        if action.page == "PageConcepts":
            if action.action == 1:
                return BinaryImageView.from_file("page.png")
            elif action.action == 2:
                return BinaryImageView.from_file("view.png")
            elif action.action == 3:
                return BinaryImageView.from_file("action.png")
        else:
            return SvgImageView.from_template("concepts.svg", result)

    def btn_page(self, action: Action):
        return "PageConcepts"

    def btn_view(self, action: Action):
        return "PageConcepts"

    def btn_action(self, action: Action):
        return "PageConcepts"

    def btn_contribute(self, action: Action):
        return "PageContribute"


class PageContribute:
    def view(self, action: Action, result: ActionResult):
        return BinaryImageView.from_file("contribute.png")

    def btn_back_home(self, action: Action):
        return "PageHome"


# CSS = """
#   .center {
#     width: 100%;
#     padding: 16px;
#     margin: auto;
#     text-align: center;
#   }
#   .medium {
#     width: 70%;
#     text-align: left;
#     margin: auto;
#   }
#   .small {
#     width: 50%;
#     background-color: lightgrey;
#     text-align: left;
#     margin: auto;
#   }
# """
