import contentful
from rich_text_renderer import RichTextRenderer
from rich_text_renderer.base_node_renderer import BaseNodeRenderer
from rich_text_renderer.null_renderer import NullRenderer
import os

MAP_KEY = os.environ.get("MAP_KEY")


class locationBlockEntryRenderer(BaseNodeRenderer):
    def render(self, entry):
        return """<div class="col my-auto" align="center">
                    <h1>{0}</h1>
                    <p>{1}</p>
                    <a class="btn btn-lg btn-outline-secondaru" href="https://www.google.com/maps?q={2}" target="_blank" role="button">View on Google Maps</a>
                </div>
                <div class="col" align="center">
                    <div id="map">
                        <iframe
                          width="100%"
                          height="640"
                          frameborder="0" style="border:0"
                          src="https://www.google.com/maps/embed/v1/place?key={2}
                            &q={1}" allowfullscreen>
                        </iframe>
                    </div>
                </div>""".format(
            entry.section_title, entry.location_string, MAP_KEY
        )


# class locationBlockInlineRenderer(BaseNodeRenderer):
#     def render(self, node):
# entry = node["data"]["target"]
# return "<{0} href='#{1}'>{1}</{0}>".format(self._render_tag, entry.section_title)


class buttonEntryRenderer(BaseNodeRenderer):
    def render(self, entry):
        return """<div class="col">
                        <a class="btn btn-lg btn-outline-warning" href="{1}" role="button">{0}</a>
                    </div>""".format(
            entry.section_title, entry.section_link
        )


class BaseInlineRenderer(BaseNodeRenderer):
    def render(self, node):
        entry = node["data"]["target"]
        return "<{0} href='#{1}'>{1}</{0}>".format(
            self._render_tag, entry.section_title
        )

    @property
    def _render_tag(self):
        return "a"


class BaseBlockEntryRenderer(BaseNodeRenderer):
    __RENDERERS__ = []

    def render(self, node):
        entry = node["data"]["target"]
        if type(entry) == contentful.resource.Link:
            entry = entry.resolve(client)
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
