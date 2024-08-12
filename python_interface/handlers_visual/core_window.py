import tkinter as tk
from tkinter import Menu
from panels.selection import open_new_window

def create_menu(root):
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Меню", menu=file_menu)

    file_menu.add_command(label="Предметная область", command=lambda: create_buttons_window(root))

def create_buttons_window(root):
    buttons_window = tk.Toplevel(root)
    buttons_window.title("Предметная область")
    buttons_window.geometry("400x400")
    
    close_button = tk.Button(buttons_window, text = ('<-'), command = buttons_window.destroy)
    close_button.place(x = 350, y = 0)

    button1 = tk.Button(buttons_window, text="Выборка", command=lambda: open_new_window(root))
    button1.pack(pady=5)

    button2 = tk.Button(buttons_window, text="Button 2", command=lambda: on_button_click("Button 2"))
    button2.pack(pady=5)

    button3 = tk.Button(buttons_window, text="Button 3", command=lambda: on_button_click("Button 3"))
    button3.pack(pady=5)

def on_button_click(button_name):
    print(f"Button '{button_name}' clicked")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu Example")

    create_menu(root)

    root.mainloop()