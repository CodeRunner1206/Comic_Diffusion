import os
import gradio as gr

API_KEY=os.environ.get('HUGGING_FACE_HUB_TOKEN', None)

article = """---
This space was created using [SD Space Creator](https://huggingface.co/spaces/anzorq/sd-space-creator)."""

gr.Interface.load(
    name="models/ogkalu/Comic-Diffusion",
    title="""Comic Diffusion""",
    description="""Demo for <a href="https://huggingface.co/ogkalu/Comic-Diffusion">Comic Diffusion</a> Stable Diffusion model.""",
    article=article,
    api_key=API_KEY,
    ).queue(concurrency_count=20).launch()
