import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from handlers_functions.selection.one_dim_selection import get_sort_data, get_quartile, get_intervals
from handlers_functions.standard_functions.r_functions import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def open_new_window(root):
    new_window = tk.Toplevel(root)
    new_window.title("Выборка")
    new_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    new_window.configure(background='white')

    notebook = ttk.Notebook(new_window)
    notebook.pack(fill='both', expand=True)

    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)

    notebook.add(tab1, text="Одномерные расчеты")
    notebook.add(tab2, text="Двумерные расчеты")

    create_one_dim_tab(tab1)
    create_two_dim_tab(tab2)


def create_one_dim_tab(tab):
    vector_1_label = ttk.Label(tab, text="Введите элементы выборки через запятую:", font=("Helvetica", 12))
    vector_1_label.pack(pady=5)

    input_frame = ttk.Frame(tab)
    input_frame.pack(pady=10)

    vector_1 = ttk.Entry(input_frame, width=50)
    vector_1.pack(side=tk.TOP, pady=10, padx=10)

    def load_from_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                data = file.read().strip()
                vector_1.delete(0, tk.END)
                vector_1.insert(0, data)

    load_button = ttk.Button(input_frame, text="Загрузить элементы выборки из файла", command=load_from_file)
    load_button.pack(side=tk.TOP, padx=10)

    result_label = ttk.Label(tab, text="Результаты будут отображены здесь", font=("Helvetica", 12))
    result_label.pack(pady=10)

    vector_y_label = ttk.Label(input_frame, text="Выберите формулу расчёта интервалов:", font=("Helvetica", 12))
    vector_y_label.pack(side=tk.LEFT, pady=10)

    prob_combobox = ttk.Combobox(input_frame, values=["Брукс-Каррузер", "Хайнхольд-Гёде", "Стерджесс"], width=25,
                                 state="readonly")
    prob_combobox.pack(side=tk.RIGHT, pady=10, padx=20)
    prob_combobox.current(0)

    canvas = None
    toolbar = None

    def starter():
        nonlocal canvas, toolbar
        input_text = vector_1.get()

        try:
            formula = prob_combobox.get()
            data = list(map(float, input_text.split(",")))
            sorted_data = get_sort_data(data)
            mean_value = mean(sorted_data)
            variance = var_unbased(sorted_data)
            median_value = median(sorted_data)
            quartile_1 = get_quartile(sorted_data, 1)
            quartile_3 = get_quartile(sorted_data, 3)

            result_text = f"Среднее: {mean_value:.2f}\nДисперсия: {variance:.2f}\nМедиана: {median_value:.2f}\nПервый квартиль: {quartile_1:.2f}\nТретий квартиль: {quartile_3:.2f}"
            result_label.config(text=result_text)

            intervals = get_intervals(formula, sorted_data)  # СДЕЛАТЬ ВЫБОР СПОСОБА РАСЧЁТА ИНТЕРВАЛОВ!
            # Plot histogram
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.hist(sorted_data, bins=intervals, range=(sorted_data[0], sorted_data[-1]), edgecolor='black')
            ax.set_title('Гистограмма')
            ax.set_xlabel('Значения')
            ax.set_ylabel('Частота')

            if canvas:
                canvas.get_tk_widget().destroy()
            if toolbar:
                toolbar.destroy()

            canvas = FigureCanvasTkAgg(fig, master=tab)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            toolbar = NavigationToolbar2Tk(canvas, tab)
            toolbar.update()
            toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    start_button = ttk.Button(tab, text="Вычислить", command=starter)
    start_button.pack(pady=10)

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.hist([], bins=10, edgecolor='black')
    ax.set_title('Гистограмма')
    ax.set_xlabel('Значения')
    ax.set_ylabel('Частота')

    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, tab)
    toolbar.update()
    toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def create_two_dim_tab(tab):
    button_frame = ttk.Frame(tab)
    button_frame.pack(side=tk.LEFT, padx=10, pady=10)
    canvas_frame = ttk.Frame(tab)
    canvas_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    vector_x_label = ttk.Label(button_frame, text="Введите элементы выборки 1 через запятую:", font=("Helvetica", 12))
    vector_x_label.pack(pady=5)

    vector_x = ttk.Entry(button_frame, width=50)
    vector_x.pack(padx=30, pady=10)

    vector_y_label = ttk.Label(button_frame, text="Введите элементы выборки 2 через запятую:", font=("Helvetica", 12))
    vector_y_label.pack(pady=5)

    vector_y = ttk.Entry(button_frame, width=50)
    vector_y.pack(padx=30, pady=10)

    vector_y_label = ttk.Label(button_frame, text="Выберите формулу расчёта интервалов:", font=("Helvetica", 12))
    vector_y_label.pack(pady=5)

    prob_combobox = ttk.Combobox(button_frame, values=["Брукс-Каррузер", "Хайнхольд-Гёде", "Стерджесс"], width=20,
                                 state="readonly")
    prob_combobox.pack(pady=10, padx=20)
    prob_combobox.current(0)

    result_label = ttk.Label(button_frame, text="Результаты будут отображены здесь", font=("Helvetica", 12))
    result_label.pack(pady=20)

    canvas = None
    toolbar = None

    def load_from_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                data = file.read().strip().split('\n')
                if len(data) >= 2:
                    vector_x.delete(0, tk.END)
                    vector_x.insert(0, data[0].strip())
                    vector_y.delete(0, tk.END)
                    vector_y.insert(0, data[1].strip())

    style = ttk.Style()
    style.configure("TButton", background="DodgerBlue3")

    load_button = ttk.Button(button_frame, text="Загрузить элементы выборок из файла", command=load_from_file, style="TButton")
    load_button.pack(pady=10)

    def starter():
        nonlocal canvas, toolbar
        input_text_x = vector_x.get()
        input_text_y = vector_y.get()

        try:
            formula = prob_combobox.get()
            data_x = list(map(float, input_text_x.split(",")))
            data_y = list(map(float, input_text_y.split(",")))
            sdata_x = get_sort_data(data_x)
            sdata_y = get_sort_data(data_y)
            cor_coef = get_cor_coef(data_x, data_y)

            int_x = get_intervals(formula, sdata_x)
            int_y = get_intervals(formula, sdata_y)

            result_text = f"Коэффициент корреляции: {cor_coef:.2f}"
            result_label.config(text=result_text)

            fig = plt.figure(figsize=(10, 7))
            ax = fig.add_subplot(111, projection='3d')
            hist, xedges, yedges = np.histogram2d(sdata_x, sdata_y, bins=[len(int_x), len(int_y)])
            xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
            xpos = xpos.ravel()
            ypos = ypos.ravel()
            zpos = 0
            dx = dy = 0.9*np.ones_like(zpos)
            dz = hist.ravel()
            ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', edgecolor='black')
            ax.set_title('Гистограмма распределения')
            ax.set_xlabel('Выборка 1')
            ax.set_ylabel('Выборка 2')
            ax.set_zlabel('Частота')

            if canvas:
                canvas.get_tk_widget().destroy()
            if toolbar:
                toolbar.destroy()

            canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            toolbar = NavigationToolbar2Tk(canvas, canvas_frame)
            toolbar.update()
            toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    start_button = ttk.Button(button_frame, text="Вычислить", command=starter, style="TButton")
    start_button.pack(pady=10)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    hist, xedges, yedges = np.histogram2d([0,0,0], [0,0,0], bins=[10, 10])
    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', edgecolor='black')
    ax.set_title('Гистограмма распределения')
    ax.set_xlabel('Выборка 1')
    ax.set_ylabel('Выборка 2')
    ax.set_zlabel('Частота')

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, canvas_frame)
    toolbar.update()
    toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    open_new_window(root)
    root.mainloop()