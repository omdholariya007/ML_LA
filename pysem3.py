# eng_to_guj_gui.py
# English → Gujarati Translator (Works on Python 3.13)
# Requires: pip install deep-translator

import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_action():
    txt = txt_input.get("1.0", "end").strip()
    if not txt:
        messagebox.showwarning("Input Needed", "Please type English text to translate.")
        return
    try:
         translated = GoogleTranslator(source='en', target='gu').translate(txt)
         txt_output.delete("1.0", "end")
         txt_output.insert("1.0", translated)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed:\n{e}")

root = tk.Tk()
root.title("English → Gujarati Translator")

frm = ttk.Frame(root, padding=12)
frm.grid(sticky="nsew")

ttk.Label(frm, text="Enter English text:").grid(row=0, column=0, sticky="w")
txt_input = tk.Text(frm, width=60, height=8)
txt_input.grid(row=1, column=0, padx=4, pady=4)

btn = ttk.Button(frm, text="Translate → Gujarati", command=translate_action)
btn.grid(row=2, column=0, sticky="e", pady=6)

ttk.Label(frm, text="Gujarati output:").grid(row=3, column=0, sticky="w")
txt_output = tk.Text(frm, width=60, height=8)
txt_output.grid(row=4, column=0, padx=4, pady=4)

root.columnconfigure(0, weight=1)
root.mainloop()
