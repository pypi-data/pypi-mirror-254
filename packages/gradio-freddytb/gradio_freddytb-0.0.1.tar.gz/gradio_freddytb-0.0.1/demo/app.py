
import gradio as gr
from gradio_freddytb import FreddyTb


example = FreddyTb().example_inputs()

demo = gr.Interface(
    lambda x:x,
    FreddyTb(),  # interactive version of your component
    FreddyTb(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
