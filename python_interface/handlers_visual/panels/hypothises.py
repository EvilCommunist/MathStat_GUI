import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
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
from handlers_functions.standard_functions.standart_functions import convert_list_to_tuple as ltt

DISTRIBUTION_TRANSLATOR: dict = {
 "norm": "Нормальное", "pois": "Пуассоновское", "binom": "Биномиальное", "unset": "Неопределено"
}


def open_hypothises_window(root):
    new_window = tk.Toplevel(root)
    new_window.title("Проверка гипотиз")
    new_window.configure(background='white')

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 14), padding=10)
    style.configure("TButton", font=("Helvetica", 14), padding=10)

    main_frame = ttk.Frame(new_window)
    main_frame.pack(fill=tk.BOTH, expand=True)

    data_label = ttk.Label(main_frame, text="Введите элементы выборки через запятую:", style="TLabel")
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

    load_button = ttk.Button(data_entry_frame, text="Загрузить элементы выборки из файла", command=load_data_from_file, style="TButton")
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

    def get_parameter_for_calc(par_name: str, par_num: int) -> float | tuple[float, float]:
        parameter = simpledialog.askstring(f"Запрос на ввод", f"Введите следующие параметры: {par_name}.")
        try:
            if par_num > 1:
                data = list(map(float, parameter.split(",")))
                return ltt(data)
            else:
                data = float(parameter)
                return float(data)
        except Exception as ex:
            messagebox.showerror("Ошибка", str(ex))
        return 0

    def calculate(function):
        data_entry.focus_force()
        input_text = data_entry.get()
        try:
            alpha = float(alpha_entry.get())
            beta = float(beta_entry.get())

            res: float
            if function == a0_hyp:
                data = list(map(float, input_text.split(",")))
                plot_histogram(get_sort_data(data))
                res = function(data, get_parameter_for_calc("математическое ожидание", 1), alpha)
                if res:
                    result_label.config(text=f"Гипотеза верна.")
                else:
                    result_label.config(text=f"Гипотеза неверна.")
            elif function == sigma_sq0_hyp:
                data = list(map(float, input_text.split(",")))
                plot_histogram(get_sort_data(data))
                res = function(data, get_parameter_for_calc("дисперсия", 1), alpha)
                if res:
                    result_label.config(text=f"Гипотеза верна.")
                else:
                    result_label.config(text=f"Гипотеза неверна.")
            elif function == check_len:
                params = get_parameter_for_calc("дисперсия, мат. ожидание, мат. ожидание для альтернативной гипотезы.", 3)
                res = function(params[1], params[2], params[0], alpha, beta)
                result_label.config(text=f"Оптимальная длина выборки на основе ваших данных: {res} элемента.")
            elif function == get_prob:
                data = list(map(float, input_text.split(",")))
                plot_histogram(get_sort_data(data))
                res = function(data, get_parameter_for_calc("выборочное среднее", 1), alpha)
                if res:
                    result_label.config(text=f"Гипотеза верна.")
                else:
                    result_label.config(text=f"Гипотеза неверна.")
            elif function == estimate_distribution:
                data = list(map(float, input_text.split(",")))
                plot_histogram(get_sort_data(data))
                res = function(data)
                result_label.config(text=f"Выбранное распределение: {DISTRIBUTION_TRANSLATOR[res[0]]}, p-значение полученного сравнения: {res[1]}, D-значение: {res[2]}")

        except Exception as ex:
            messagebox.showerror("Ошибка", str(ex))

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
    hyp_button = ttk.Button(button_frame, text="Оценить гипотезу с текушим значением α",
                            command=lambda: calculate(get_prob), style="TButton")
    hyp_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
    dist_type_button = ttk.Button(button_frame, text="Оценить распределение",
                                  command=lambda: calculate(estimate_distribution), style="TButton")
    dist_type_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

    for i in range(5):
        button_frame.columnconfigure(i, weight=1)

    plot_empty_histogram()

    # Ввод желаемого значения ошибок 1-го и 2-го рода

    prob_label = ttk.Label(button_frame, text="Введите желаемые значения ошибок:", font=("Helvetica", 12))
    prob_label.grid(row=5, column=0, pady=10, sticky="w")

    prob_entry_frame = ttk.Frame(button_frame)
    prob_entry_frame.grid(row=6, column=0, pady=10, sticky="w")

    prob_label = ttk.Label(prob_entry_frame, text="I-го рода:", font=("Helvetica", 12))
    prob_label.grid(row=0, column=0, pady=10, sticky="w")

    alpha_entry = ttk.Entry(prob_entry_frame, width=10)
    alpha_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")
    alpha_entry.insert(0, "0.1")
    alpha_entry.focus_set()

    prob_label = ttk.Label(prob_entry_frame, text="II-го рода:", font=("Helvetica", 12))
    prob_label.grid(row=0, column=2, pady=10, sticky="w")

    beta_entry = ttk.Entry(prob_entry_frame, width=10)
    beta_entry.grid(row=0, column=3, padx=20, pady=10, sticky="w")
    beta_entry.insert(0, "0.05")
    beta_entry.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    open_hypothises_window(root)
    root.mainloop()
