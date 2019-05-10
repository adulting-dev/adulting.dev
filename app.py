from flask import Flask, render_template

import contentful
from rich_text_renderer import RichTextRenderer
import os

SPACE_ID = os.environ.get("SPACE_ID")
DELIVERY_API_KEY = os.environ.get("DELIVERY_API_KEY")
API_URL = os.environ.get("API_URL")
MAP_KEY = os.environ.get("MAP_KEY")
DEBUG_STATUS = os.environ.get("DEBUG_STATUS")

client = contentful.Client(SPACE_ID, DELIVERY_API_KEY, API_URL)
renderer = RichTextRenderer()

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
        MAP_KEY=MAP_KEY
    )


if __name__ == "__main__":
    app.debug = DEBUG_STATUS
    app.run()
