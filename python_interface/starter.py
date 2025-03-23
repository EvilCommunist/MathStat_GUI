# dummy file for build
from handlers_visual.core_window import *

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Математическая статистика")
    root.configure(background='white')

    root.protocol("WM_DELETE_WINDOW", root.quit)

    create_main_buttons(root)

    root.mainloop()
