import pluggy
import requests
import textwrap
from PIL import Image, ImageFont, ImageDraw
import pkg_resources
from io import BytesIO

from dinky.display_configuration import DisplayConfiguration
from dinky.layouts.layout_configuration import Zone

hookimpl = pluggy.HookimplMarker("dinky")

class DinkyNotesPlugin:
    primary_color = "#2a9d8f"

    def __init__(self, url: str):
        self.url = url

    def _get_notes(self):
        r = requests.get(
            url=self.url,
        )
        return r.text

    @hookimpl
    def dinky_draw(self, zone: Zone, fullscreen: DisplayConfiguration):
        # Notes
        notes = self._get_notes()

        # Fonts
        font_data = pkg_resources.resource_stream('dinky_notes', 'fonts/Roboto-Regular.ttf')
        font_bytes = BytesIO(font_data.read())
        font_header = ImageFont.truetype(font_bytes, 36)
        font_bytes.seek(0)
        font_regular = ImageFont.truetype(font_bytes, 14)

        # Panel
        im_panel = Image.new('RGB', (zone.width, zone.height), (255, 255, 255))
        draw_panel = ImageDraw.Draw(im_panel)
        draw_panel.rectangle((zone.padding, zone.padding, zone.width-zone.padding, zone.padding + 55), fill=self.primary_color)
        draw_panel.text((zone.padding + 5, zone.padding + 5), "Notes", font=font_header, fill="white")
        wrapper = textwrap.TextWrapper(width=int(0.15 * (zone.width - 2 * zone.padding)), drop_whitespace=False, replace_whitespace=False, subsequent_indent='    ')
        draw_panel.multiline_text((zone.padding + 5, zone.padding + 5 + 55), wrapper.fill(notes), font=font_regular, fill="black")

        # Fullscreen
        im_fullscreen = Image.new('RGB', (fullscreen.width, fullscreen.height), (255, 255, 255))
        draw_fullscreen = ImageDraw.Draw(im_fullscreen)
        draw_fullscreen.rectangle((zone.padding, zone.padding, fullscreen.width-zone.padding, zone.padding + 55), fill=self.primary_color)
        draw_fullscreen.text((zone.padding + 5, zone.padding + 5), "Notes", font=font_header, fill="white")
        wrapper = textwrap.TextWrapper(width=int(0.18 * (fullscreen.width - 2 * zone.padding)), drop_whitespace=False, replace_whitespace=False, subsequent_indent='    ')
        draw_fullscreen.multiline_text((zone.padding + 5, zone.padding + 5 + 55), wrapper.fill(notes), font=font_regular, fill="black")

        return im_panel, im_fullscreen