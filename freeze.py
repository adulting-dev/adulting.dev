from flask_frozen import Freezer
from app import app

from flask import Flask, render_template
from flaskext.markdown import Markdown
import contentful
from rich_text_renderer import RichTextRenderer
from rich_text_renderer.base_node_renderer import BaseNodeRenderer
from rich_text_renderer.null_renderer import NullRenderer
import os

from custom_renders import (
    locationBlockEntryRenderer,
    buttonEntryRenderer,
    BaseInlineRenderer,
    BaseBlockEntryRenderer,
)

SPACE_ID = os.environ.get("SPACE_ID")
DELIVERY_API_KEY = os.environ.get("DELIVERY_API_KEY")

client = contentful.Client(SPACE_ID, DELIVERY_API_KEY)

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
