import gradio as gr
from gradio_gradioworkbook import GradioWorkbook

AICONFIG_FILE_PATH = "./example_aiconfig.json" #Can also be empty or None!
with gr.Blocks() as demo:
    GradioWorkbook(filepath=AICONFIG_FILE_PATH)

demo.queue().launch()
