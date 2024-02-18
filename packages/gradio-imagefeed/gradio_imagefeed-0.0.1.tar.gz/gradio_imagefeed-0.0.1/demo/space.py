
import gradio as gr
from app import demo as app
import os

_docs = {'ImageFeed': {'description': 'Creates an image component that can be used to upload images (as an input) or display images (as an output).', 'members': {'__init__': {'value': {'type': 'str | _Image.Image | np.ndarray | None', 'default': 'None', 'description': 'A PIL ImageFeed, numpy array, path or URL for the default value that ImageFeed component is going to take. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'height': {'type': 'int | str | None', 'default': 'None', 'description': 'The height of the displayed image, specified in pixels if a number is passed, or in CSS units if a string is passed.'}, 'width': {'type': 'int | str | None', 'default': 'None', 'description': 'The width of the displayed image, specified in pixels if a number is passed, or in CSS units if a string is passed.'}, 'image_mode': {'type': 'Literal[\n    "1",\n    "L",\n    "P",\n    "RGB",\n    "RGBA",\n    "CMYK",\n    "YCbCr",\n    "LAB",\n    "HSV",\n    "I",\n    "F",\n]', 'default': '"RGB"', 'description': '"RGB" if color, or "L" if black and white. See https://pillow.readthedocs.io/en/stable/handbook/concepts.html for other supported image modes and their meaning.'}, 'sources': {'type': 'list[Literal["upload", "webcam", "clipboard"]] | None', 'default': 'None', 'description': 'List of sources for the image. "upload" creates a box where user can drop an image file, "webcam" allows user to take snapshot from their webcam, "clipboard" allows users to paste an image from the clipboard. If None, defaults to ["upload", "webcam", "clipboard"] if streaming is False, otherwise defaults to ["webcam"].'}, 'type': {'type': 'Literal["numpy", "pil", "filepath"]', 'default': '"numpy"', 'description': 'The format the image is converted before being passed into the prediction function. "numpy" converts the image to a numpy array with shape (height, width, 3) and values from 0 to 255, "pil" converts the image to a PIL image object, "filepath" passes a str path to a temporary file containing the image. If the image is SVG, the `type` is ignored and the filepath of the SVG is returned.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'show_download_button': {'type': 'bool', 'default': 'True', 'description': 'If True, will display button to download image.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will allow users to upload and edit an image; if False, can only be used to display images. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'streaming': {'type': 'bool', 'default': 'False', 'description': "If True when used in a `live` interface, will automatically stream webcam feed. Only valid is source is 'webcam'."}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'mirror_webcam': {'type': 'bool', 'default': 'True', 'description': 'If True webcam will be mirrored. Default is True.'}, 'show_share_button': {'type': 'bool | None', 'default': 'None', 'description': 'If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.'}}, 'postprocess': {'value': {'type': 'np.ndarray | _Image.Image | str | Path | None', 'description': None}}, 'preprocess': {'return': {'type': 'np.ndarray | _Image.Image | str | None', 'description': None}, 'value': None}}, 'events': {}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'ImageFeed': []}}}
    
abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_imagefeed`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

A vertical feed of images which gets updated as a generater yields a new image.
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_imagefeed
```

## Usage

```python

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

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `ImageFeed`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["ImageFeed"]["members"]["__init__"], linkify=[])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function. 
- When used as an output, the component only impacts the return signature of the user function. 

The code snippet below is accurate in cases where the component is used as both an input and an output.



 ```python
def predict(
    value: np.ndarray | _Image.Image | str | None
) -> np.ndarray | _Image.Image | str | Path | None:
    return value
```
""", elem_classes=["md-custom", "ImageFeed-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          ImageFeed: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
        
        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
