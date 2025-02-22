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
from handlers_functions.point_estimate.distribution_estimate import estimate_distribution
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

    hist_formula_frame = ttk.Frame(main_frame)
    hist_formula_frame.pack(pady=10, fill=tk.X, padx=20)

    vector_y_label = ttk.Label(hist_formula_frame, text="Выберите формулу расчёта интервалов:", font=("Helvetica", 12))
    vector_y_label.pack(side=tk.LEFT, pady=5)

    prob_combobox = ttk.Combobox(hist_formula_frame, values=["Брукс-Каррузер", "Хайнхольд-Гёде", "Стерджесс"], width=20,
                                 state="readonly", font=("Helvetica", 11))
    prob_combobox.pack(side=tk.RIGHT, pady=5, padx=20)
    prob_combobox.current(0)

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
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, main_frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

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
        formula = prob_combobox.get()
        intervals = get_intervals(formula, data)
        ax.axhline(0, color='black', linewidth=0.8)
        ax.hist(data, bins=intervals, range=(sorted_data[0], sorted_data[-1]), edgecolor='black')
        ax.set_xlabel('Значения')
        ax.set_ylabel('Частота')
        ax.set_ylim(bottom=0)
        canvas.draw()

    def calculate(function):
        data_entry.focus_force()
        input_text = data_entry.get()
        try:
            data = input_text.split(",")

            plot_histogram(data)

            result_label.config(text=f"Оценка правдоподобия: {0}, дисперсия выборочного среднего: {0}")
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

    size_button = ttk.Button(button_frame, text="Расчитать оптимальный размер выборки для проверки гипотезы",
                             command=lambda: calculate(check_len), style="TButton")
    size_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

    a_0_button = ttk.Button(button_frame, text="Проверить гипотезу о выборочном среднем",
                            command=lambda: calculate(a0_hyp), style="TButton")
    a_0_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

    var_button = ttk.Button(button_frame, text="Проверить гипотезу о дисперсии",
                            command=lambda: calculate(sigma_sq0_hyp), style="TButton")
    var_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
    hyp_button = ttk.Button(button_frame, text="Оценить гипотезу",
                            command=lambda: calculate(get_prob), style="TButton")
    hyp_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
    dist_type_button = ttk.Button(button_frame, text="Оценить распределение",
                                  command=lambda: calculate(estimate_distribution), style="TButton")
    dist_type_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

    for i in range(5):
        button_frame.columnconfigure(i, weight=1)

    plot_empty_histogram()


if __name__ == "__main__":
    root = tk.Tk()
    open_hypothises_window(root)
    root.mainloop()
