import tkinter as tk
from tkinter import ttk, Menu, messagebox
from python_interface.handlers_visual.panels.selection import open_new_window
from python_interface.handlers_visual.panels.interval_estimation_panel import open_likelihood_window
from python_interface.handlers_visual.panels.confidence_interval_panel import open_confidence_interval_window

def create_menu(root):
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Helvetica', 14), padding=10, background='#4CAF50', foreground='white')
    style.map('TButton', background=[('active', '#45a049')])
    style.configure('TLabel', font=('Helvetica', 14), padding=10, foreground='black')
    style.configure('TFrame', background='white')

    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Меню", menu=file_menu)

    file_menu.add_command(
        label="Предметная область", command=lambda: create_buttons_window(root)
    )

def create_buttons_window(root):
    buttons_window = tk.Toplevel(root)
    buttons_window.title("Предметная область")
    buttons_window.attributes('-fullscreen', True)
    buttons_window.configure(background='white')

    button_frame = ttk.Frame(buttons_window, style='TFrame')
    button_frame.pack(pady=50)

    style = ttk.Style()
    style.configure("TButton", background="DodgerBlue3")

    button1 = ttk.Button(
        button_frame, text="Выборка", command=lambda: open_new_window(root), style='TButton'
    )
    button1.pack(pady=10, fill='x', padx=20)

    button2 = ttk.Button(
        button_frame, text="Расчет правдоподобия", command=lambda: open_likelihood_window(root), style='TButton'
    )
    button2.pack(pady=10, fill='x', padx=20)

    button3 = ttk.Button(
        button_frame, text="Расчет доверительных интервалов", command=lambda: open_confidence_interval_window(root), style='TButton'
    )
    button3.pack(pady=10, fill='x', padx=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Математическая статистика")
    root.attributes('-fullscreen', True)
    root.configure(background='white')

    create_menu(root)

    root.mainloop()