import os
import tkinter as tk
from tkinter import filedialog

# Configuration
RESOLUTION = "600x500"
PAD = 20

# DATA
FILE_NAME = ""

# Utility Functions
def open_file_explorer(label):
    global FILE_NAME
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if file_path:
        FILE_NAME = os.path.basename(file_path)
        label.config(text=f"Archivo seleccionado: {FILE_NAME}")

def add_record(error_label):
    if len(FILE_NAME) == 0:
        error_label.config(text="Error: ningún archivo seleccionado.")
    else:
        error_label.config(text="")
        #agregar funcionalidad para agregar registro

# Main Application Logic
def main():
    root = tk.Tk()
    root.title("Aresil - Control")
    root.geometry(f"{RESOLUTION}-1920+0") # Move window to the second screen

    title_frame = tk.Frame(root, width=560, height=35, relief="solid")
    title_frame.pack(padx=PAD,pady=(PAD,0), fill='both')

    title_label = tk.Label(title_frame, text="Control", font=("Helvetica", 26))
    title_label.pack()

    
    file_frame = tk.Frame(root, width=560, height=150)
    file_frame.pack(padx=PAD, pady=0, fill='both')

    button_label = tk.Label(file_frame, text="Seleccione un archivo:")
    button_label.pack(pady=(PAD,0))

    button = tk.Button(file_frame, text="Seleccionar archivo", command=lambda: open_file_explorer(button_label))
    button.pack(pady=(5,PAD))


    bottom_frame = tk.Frame(root, width=560, height=75)
    bottom_frame.pack(anchor='s', padx=PAD, pady=(0,PAD), fill='both')


    button_execute = tk.Button(bottom_frame, text="Agregar registro", command=lambda: add_record(error_label))
    button_execute.pack(pady=PAD)

    error_label = tk.Label(bottom_frame, text="", fg="red")
    error_label.pack()

    button_settings = tk.Button(bottom_frame, text="C")
    button_settings.pack(anchor='w')


    settings_frame = tk.Frame(root, width=560, height=75)
    settings_frame.pack(anchor='s', padx=PAD, pady=(0,PAD), fill='both')

    text_widget_control_file = tk.Text(settings_frame, height=1, width=50)
    text_widget_control_file.pack(side='left', fill='x')

    button_select_control_file = tk.Button(settings_frame, text="Seleccionar archivo destino")
    button_select_control_file.pack(side='right')

    

    root.mainloop()

if __name__ == "__main__":
    main()