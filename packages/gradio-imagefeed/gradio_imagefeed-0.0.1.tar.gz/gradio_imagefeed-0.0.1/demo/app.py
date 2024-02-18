
import gradio as gr
from gradio_imagefeed import ImageFeed
import time
from PIL import Image, ImageFilter
import os 

image = Image.open(os.path.join(os.path.dirname(__file__), "butterfly.png"))
blurred_images = [image.filter(ImageFilter.GaussianBlur(5-i)) for i in range(5)]

def fake_unblur(steps=5):
    for i in range(steps):
        yield blurred_images[i]
        time.sleep(1)
    yield image

with gr.Blocks() as demo: 
    with gr.Row():
        imagefeed = ImageFeed(label="Generated Images")
    button = gr.Button("Start Generating")
    button.click(fake_unblur, inputs=None, outputs=imagefeed)

if __name__ == "__main__":
    demo.launch()
