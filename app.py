from flask import Flask, render_template

import contentful
from rich_text_renderer import RichTextRenderer
from rich_text_renderer.base_node_renderer import BaseNodeRenderer
from rich_text_renderer.null_renderer import NullRenderer
import os

# BaseNodeRenderer implements the `__init__` method required.
class locationBlockEntryRenderer(BaseNodeRenderer):

    def render(self, entry):
        return """<div class="col my-auto" align="center">
                        <h1>{0}</h1>
                        <p>{1}</p>
                        <p>{2}</p>
                        <p>{3}</p>
                    </div>""".format(
            entry.section_title,
            entry.location_string,
            entry.location.lat,
            entry.location.lon,
        )


class BaseBlockEntryRenderer(BaseNodeRenderer):
    __RENDERERS__ = []

    def render(self, node):
        entry = node["data"]["target"]
        renderer = None
        try:
            renderer = [
                r
                for r in self.__class__.__RENDERERS__
                if f"{entry.content_type.id}EntryRenderer" in r.__name__
            ][0]()
        except IndexError as e:
            print(e)
            return ""
        if renderer is not None:
            return renderer.render(entry)


SPACE_ID = os.environ.get("SPACE_ID")
DELIVERY_API_KEY = os.environ.get("DELIVERY_API_KEY")
API_URL = os.environ.get("API_URL")
MAP_KEY = os.environ.get("MAP_KEY")
DEBUG_STATUS = os.environ.get("DEBUG_STATUS")

client = contentful.Client(SPACE_ID, DELIVERY_API_KEY, API_URL)

BaseBlockEntryRenderer.__RENDERERS__ += [locationBlockEntryRenderer]

renderer = RichTextRenderer({"embedded-entry-block": BaseBlockEntryRenderer})


app = Flask(__name__)


@app.route("/")
def home_page():
    entry = client.entry("1l3EHYzPbgf9UUV0oEyTDs")

    return render_template(
        "home.html",
        renderer=renderer,
        title=entry.page_title,
        page_components=entry.page_component,
        client=client,
        MAP_KEY=MAP_KEY,
    )


if __name__ == "__main__":
    app.debug = DEBUG_STATUS
    app.run()
