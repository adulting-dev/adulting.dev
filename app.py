from flask import Flask, render_template
from flaskext.markdown import Markdown
import contentful
from rich_text_renderer import RichTextRenderer
from rich_text_renderer.base_node_renderer import BaseNodeRenderer
from rich_text_renderer.null_renderer import NullRenderer
import os

from dotenv import load_dotenv
load_dotenv()


from custom_renders import (
    locationBlockEntryRenderer,
    buttonEntryRenderer,
    BaseInlineRenderer,
    BaseBlockEntryRenderer,
)

SPACE_ID = os.environ.get("SPACE_ID")
DELIVERY_API_KEY = os.environ.get("DELIVERY_API_KEY")
API_URL = os.environ.get("API_URL")
MAP_KEY = os.environ.get("MAP_KEY")
DEBUG_STATUS = os.environ.get("DEBUG_STATUS")
ENV = os.environ.get("ENV")

client = contentful.Client(SPACE_ID, DELIVERY_API_KEY, API_URL, environment=ENV)

BaseBlockEntryRenderer.__RENDERERS__ += [
    locationBlockEntryRenderer,
    buttonEntryRenderer,
]

renderer = RichTextRenderer(
    {
        "embedded-entry-block": BaseBlockEntryRenderer,
        "embedded-entry-inline": BaseInlineRenderer,
    }
)

app = Flask(__name__)
Markdown(app)

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
