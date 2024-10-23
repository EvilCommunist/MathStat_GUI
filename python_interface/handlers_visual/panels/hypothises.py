import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from handlers_functions.hypothises_checking.hyp_check import (
    get_good_data_len as check_len,
    get_hyp_prob_result as get_prob,
    check_a0_hypothises as a0_hyp,
    check_variance0_hypothises as sigma_sq0_hyp
)
from handlers_functions.selection.one_dim_selection import get_intervals, get_sort_data


def open_hypothises_window(root):
    new_window = tk.Toplevel(root)
    new_window.title("Проверка гипотиз")
    new_window.configure(background='white')

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 14), padding=10)
    style.configure("TButton", font=("Helvetica", 14), padding=10)

    main_frame = ttk.Frame(new_window)
    main_frame.pack(fill=tk.BOTH, expand=True)

    data_label = ttk.Label(main_frame, text="Введите данные через запятую:", style="TLabel")
    data_label.pack(pady=10, fill=tk.X)

    data_entry_frame = ttk.Frame(main_frame)
    data_entry_frame.pack(pady=10, fill=tk.X, padx=20)

    data_entry = ttk.Entry(data_entry_frame, width=50)
    data_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    data_entry.focus_set()

    def load_data_from_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.read().strip()
                    data_entry.delete(0, tk.END)
                    data_entry.insert(0, data)
                    data_entry.focus_force()
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

    load_button = ttk.Button(data_entry_frame, text="Загрузить из файла", command=load_data_from_file, style="TButton")
    load_button.pack(side=tk.RIGHT, padx=10)

    result_label = ttk.Label(main_frame, text="Результаты будут отображены здесь", style="TLabel")
    result_label.pack(pady=20, fill=tk.X)

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, main_frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def plot_empty_histogram():
        ax.clear()
        ax.axhline(0, color='black', linewidth=0.8)
        ax.set_xlabel('Значения')
        ax.set_ylabel('Частота')
        ax.set_ylim(bottom=0)
        canvas.draw()

    def plot_histogram(data):
        ax.clear()
        sorted_data = get_sort_data(data)
        intervals = get_intervals(data)
        ax.axhline(0, color='black', linewidth=0.8)
        ax.hist(data, bins=intervals, range=(sorted_data[0], sorted_data[-1]), edgecolor='black')
        ax.set_xlabel('Значения')
        ax.set_ylabel('Частота')
        ax.set_ylim(bottom=0)
        canvas.draw()

    def calculate_likelihood(distribution):
        data_entry.focus_force()
        input_text = data_entry.get()
        try:
            data = input_text.split(",")
            if distribution in ["poisson", "binomial"]:
                data = list(map(int, data))
            else:
                data = list(map(float, data))

            plot_histogram(data)

            if distribution == "poisson":
                result = get_pois_function_likelihood(data)
                variance_mean = var_smean(data)
            elif distribution == "binomial":
                result = get_binomial_function_likelihood(data)
                variance_mean = var_smean(data)
            elif distribution == "normal":
                result = get_normal_function_likelihood(data)
                variance_mean = var_smean(data)
            else:
                result = "Неизвестное распределение"
                variance_mean = "распределение не определено"
            result_label.config(text=f"Оценка правдоподобия: {result}, дисперсия выборочного среднего: {variance_mean}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_from_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.read().strip().split(",")
                    data_entry.delete(0, tk.END)
                    data_entry.insert(0, ",".join(data))
                    data_entry.focus_force()
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=20, fill=tk.X)

    style = ttk.Style()
    style.configure("TButton", background="DodgerBlue3")

    poisson_button = ttk.Button(button_frame, text="Расчет для Пуассона", command=lambda: calculate_likelihood("poisson"), style="TButton")
    poisson_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

    binomial_button = ttk.Button(button_frame, text="Расчет для Биномиального",
                                 command=lambda: calculate_likelihood("binomial"), style="TButton")
    binomial_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    normal_button = ttk.Button(button_frame, text="Расчет для Нормального",
                               command=lambda: calculate_likelihood("normal"), style="TButton")
    normal_button.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

    for i in range(3):
        button_frame.columnconfigure(i, weight=1)

    plot_empty_histogram()


if __name__ == "__main__":
    root = tk.Tk()
    open_likelihood_window(root)
    root.mainloop()