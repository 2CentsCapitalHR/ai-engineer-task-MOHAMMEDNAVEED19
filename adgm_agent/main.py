from ui.gradio_app import create_gradio_interface
from config import *


def launch_application():
    demo = create_gradio_interface()
    demo.launch()


if __name__ == "__main__":
    launch_application()
