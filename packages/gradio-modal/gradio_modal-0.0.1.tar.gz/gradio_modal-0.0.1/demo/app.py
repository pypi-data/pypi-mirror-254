
import gradio as gr
from gradio_modal import Modal


with gr.Blocks() as demo:
    gr.Markdown("### Main Page")
    gr.Textbox("lorem ipsum " * 1000, lines=10)

    with Modal(visible=True) as modal:
        gr.Markdown("# License Agreement")
        gr.Textbox(value="This is the license agreement. Please read it carefully. " * 5, lines=12)
        close_btn = gr.Button("Close Modal")
        close_btn.click(lambda: Modal(visible=False), None, modal)

    show_btn = gr.Button("Show Modal")
    show_btn.click(lambda: Modal(visible=True), None, modal)


if __name__ == "__main__":
    demo.launch()
