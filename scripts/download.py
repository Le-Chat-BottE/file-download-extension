import gradio as gr
import os
import shutil
from modules import script_callbacks

def zip_folder(folder_path):
    folder_flag = os.path.exists(folder_path)
    if folder_flag is True:
        shutil.make_archive('pics', 'zip', folder_path)
        return 'Success'
    else:
        return 'Fail'

def zip_file(zip_path):
    file_flag = os.path.exists(zip_path)
    if zip_path is True:
        return zip_path
    else:
        return

def on_ui_tabs():
    with gr.Blocks() as download:
        with gr.Tab('zip'):
            folder_path = gr.Textbox(label="Folder")
            output = gr.Textbox(label='Result')
            zip_btn = gr.Button("Zip")
            zip_flag = False
            zip_btn.click(fn=zip_folder, inputs=folder_path, outputs=output)

        with gr.Tab('Download'):
            file_path = gr.Textbox(label="File")
            output = gr.File(label='Zip')
            download_btn = gr.Button("Check")
            download_btn.click(fn=zip_file, inputs=file_path, outputs=output)

    return (download, "Zip and Download", "download"),


script_callbacks.on_ui_tabs(on_ui_tabs)
