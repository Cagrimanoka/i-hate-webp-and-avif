"""converts a webp/avif image in the clipboard to a png"""

from io import BytesIO
import win32clipboard
import pillow_avif
from PIL import ImageGrab, Image

#input("press enter for conversion")

try:
    im = ImageGrab.grabclipboard()

    if isinstance(im, list):
        im = Image.open(im[0])
    # https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html#PIL.ImageGrab.grabclipboard

    with BytesIO() as output:
        im.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

    #input("ez")
except AttributeError:
    input("not ez: no image in clipboard")
