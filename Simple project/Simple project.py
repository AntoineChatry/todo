"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    items = ["Write pynecode app", "Deploy", "Have Fun"]
    new_item: str

    def add_item(self):
        self.items += [self.new_item]
        self.new_item = ""

    def finish_item(self, item):
        self.items = [i for i in self.items if i != item]


def render_item(item):
    return pc.list_item(
        pc.hstack(
            pc.button(pc.icon(tag="minus"),color_scheme="red",
                on_click=lambda: State.finish_item(item),
                height="1.25em",
                shadow="md",
                marging="5.25em",
                border_radius="0.25em",
            ),
            
            pc.text(item, font_size="1.25em"),
        )
    )


def todo_list():
    return pc.container(
        pc.vstack(
            pc.heading("Todos"),
            pc.input(
                on_blur=State.set_new_item,
                placeholder="Add a todo...",
                bg="white",
            ),
            pc.button("Add", on_click=State.add_item, bg="white"),
            pc.divider(),
            pc.ordered_list(
                pc.foreach(State.items, lambda item: render_item(item)),
            ),
            bg="#42a7f5",
            margin="5em",
            padding="1em",
            border_radius="1.25em",
            shadow="lg",
        )
    )


app = pc.App(state=State)
app.add_page(todo_list, route="/")
app.compile()
