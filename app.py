# To run
# $ export FLASK_APP=app.py
# $ python -m flask run

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import contentful
from rich_text_renderer import RichTextRenderer

SPACE_ID = 'vkfdy957l5sa'
DELIVERY_API_KEY = '404be0eecf4bf13c1cb9db6e9ebbf747a421fbf1531d76b7cd340747802b60bd'

client = contentful.Client(
    SPACE_ID,
    DELIVERY_API_KEY)

renderer = RichTextRenderer()

app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def home_page():
    entry = client.entry('1l3EHYzPbgf9UUV0oEyTDs')

    return render_template('base.html',renderer=renderer,title=entry.page_title,page_components=entry.page_component)

if __name__ == "__main__":
    app.debug = True
    app.run()
