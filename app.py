import dearpygui.dearpygui as dpg
from PIL import Image
import segno
import io
import numpy as np

IMG_WIDTH = 500
IMG_HEIGHT = 500
DEFAULT_VALUE = "Hello World"


def generate_qrcode_to_data(text):
    qrcode = segno.make_qr(text)

    out = io.BytesIO()

    qrcode.save(out, scale=20, kind="png")
    out.seek(0)
    img = Image.open(out).resize((IMG_WIDTH, IMG_HEIGHT)).convert("RGBA")
    return np.frombuffer(img.tobytes(), dtype=np.uint8) / 255.0


dpg.create_context()


with dpg.texture_registry(show=False):
    dpg.add_dynamic_texture(
        width=IMG_WIDTH,
        height=IMG_HEIGHT,
        default_value=generate_qrcode_to_data(DEFAULT_VALUE),
        tag="image_id",
    )


def _update_qr_code():
    dpg.set_value("image_id", generate_qrcode_to_data(dpg.get_value("input_text")))


with dpg.window(tag="Window"):
    dpg.add_input_text(
        label="QR Code Input",
        tag="input_text",
        source="string_value",
        default_value=DEFAULT_VALUE,
        callback=_update_qr_code,
    )
    dpg.add_text("")
    dpg.add_image("image_id")


dpg.create_viewport(title="Window", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
