import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")
    
    def new_label(self, text, posy, posx, width, height, bg, fg):
        label = tk.Label(self.window, text=text, bg=bg, fg=fg)
        label.place(x=posx, y=posy, width=width, height=height)
        return label
    
    def new_button(self, text, posy, posx, width, height, bg, fg, command=None):
        button = tk.Button(self.window, text=text, bg=bg, fg=fg, command=command)
        button.place(x=posx, y=posy, width=width, height=height)
        return button
    
    def new_entry(self, posy, posx, width, fg, placeholder=""):
        entry = tk.Entry(self.window, fg=fg)
        entry.place(x=posx, y=posy, width=width)
        entry.insert(0, placeholder)  # Insere um texto inicial no campo, se fornecido
        return entry
    
    def new_frame(self, posy, posx, width, height, bg):
        frame = tk.Frame(self.window, bg=bg)
        frame.place(x=posx, y=posy, width=width, height=height)
        return frame
    
    def new_checkbutton(self, text, posy, posx, variable, onvalue, offvalue, bg):
        checkbutton = tk.Checkbutton(self.window, text=text, variable=variable, onvalue=onvalue, offvalue=offvalue, bg=bg)
        checkbutton.place(x=posx, y=posy)
        return checkbutton
    
    def new_radiobutton(self, text, posy, posx, variable, value, bg):
        radiobutton = tk.Radiobutton(self.window, text=text, variable=variable, value=value, bg=bg)
        radiobutton.place(x=posx, y=posy)
        return radiobutton
    
    def new_text(self, posy, posx, width, height, fg, bg):
        text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, fg=fg, bg=bg)
        text.place(x=posx, y=posy, width=width, height=height)
        return text
    
    def new_listbox(self, posy, posx, width, height, fg, bg):
        listbox = tk.Listbox(self.window, fg=fg, bg=bg)
        listbox.place(x=posx, y=posy, width=width, height=height)
        return listbox
    
    def new_combobox(self, posy, posx, width, values):
        combobox = ttk.Combobox(self.window, values=values)
        combobox.place(x=posx, y=posy, width=width)
        return combobox
    
    def new_scale(self, posy, posx, width, fg, orient="horizontal"):
        scale = tk.Scale(self.window, from_=0, to=100, orient=orient, fg=fg)
        scale.place(x=posx, y=posy, width=width)
        return scale
    
    def new_spinbox(self, posy, posx, width, fg, from_, to):
        spinbox = tk.Spinbox(self.window, from_=from_, to=to, fg=fg)
        spinbox.place(x=posx, y=posy, width=width)
        return spinbox
    
    def new_progressbar(self, posy, posx, width, mode="indeterminate"):
        progressbar = ttk.Progressbar(self.window, length=width, mode=mode)
        progressbar.place(x=posx, y=posy)
        return progressbar
    
    def new_canvas(self, posy, posx, width, height, bg):
        canvas = tk.Canvas(self.window, bg=bg)
        canvas.place(x=posx, y=posy, width=width, height=height)
        return canvas
    
    def new_menu_separator(self, menu):
        menu.add_separator()
    
    def new_messagebox(self, title, message):
        messagebox.showinfo(title, message)
    
    def new_label_frame(self, posy, posx, width, height, text, bg):
        label_frame = ttk.LabelFrame(self.window, text=text, padding=(10, 10), relief="sunken", borderwidth=2)
        label_frame.place(x=posx, y=posy, width=width, height=height)
        return label_frame
    
    def new_image(self, path):
        img = tk.PhotoImage(file=path)
        return img
    
    def new_treeview(self, posy, posx, width, height, columns):
        treeview = ttk.Treeview(self.window, columns=columns, show="headings")
        treeview.place(x=posx, y=posy, width=width, height=height)
        for col in columns:
            treeview.heading(col, text=col)
        return treeview
    
    def new_notebook(self, posy, posx, width, height):
        notebook = ttk.Notebook(self.window)
        notebook.place(x=posx, y=posy, width=width, height=height)
        return notebook
    
    def new_tab(self, notebook, text):
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=text)
        return tab
    
    def new_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Selecione um arquivo", filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")])
        return file_path
    
    def new_directory_dialog(self):
        dir_path = filedialog.askdirectory(title="Selecione um diretório")
        return dir_path
    
    def new_alert(self, title, message):
        messagebox.showinfo(title, message)
    
    def new_input(self, title, prompt):
        user_input = simpledialog.askstring(title, prompt)
        return user_input