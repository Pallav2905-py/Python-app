# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "/about"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def home():
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone -123!", font_size="2em"),
            pc.link("Pallav", border="0.1em solid", border_radius="0.5em", padding="5em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
                    pc.link(
                "Hello",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
        padding_top="10%",
    )


def about():
    return pc.center(
        pc.vstack(  
        pc.text("About this Website"),
        padding_top="10em",
        )
    )
    
def contactus():
    return pc.center(
        pc.vstack(
    pc.tablet_and_desktop(
        pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone -123!", font_size="2em"),
            pc.link("Pallav", border="0.1em solid", border_radius="0.5em", padding="5em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
                    pc.link(
                "Hello",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
        padding_top="10%",
    )
    ),
    pc.tablet_only(
        pc.text("Tablet View"),
    ),
    pc.mobile_only(
        pc.text("Mobile View"),
    ),
    # pc.mobile_and_tablet(
    #     pc.text("Visible on Mobile and Tablet"),
    # ),
    # pc.tablet_and_desktop(
    #     pc.text("Visible on Desktop and Tablet"),
    # ),
)
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(home, route="/")
app.add_page(about, route="/about")
app.add_page(contactus, route="/contact")

app.compile()
