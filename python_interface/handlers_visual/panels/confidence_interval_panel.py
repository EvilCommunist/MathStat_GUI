import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from handlers_functions.confidence_interval.confidence_interval import *
from handlers_functions.standard_functions.r_functions import var_unbased as uvar, mean


def open_confidence_interval_window(root):
    new_window = tk.Toplevel(root)
    new_window.title("Расчет доверительных интервалов")
    new_window.geometry("800x600")
    new_window.configure(background='white')

    main_frame = ttk.Frame(new_window, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    top_frame = ttk.Frame(main_frame)
    top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    data_frame = ttk.Frame(top_frame)
    data_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    data_label = ttk.Label(data_frame, text="Введите элементы выборки через запятую:", font=("Helvetica", 12))
    data_label.pack(pady=5, anchor="w")

    data_entry = ttk.Entry(data_frame, width=50)
    data_entry.pack(pady=5, fill=tk.X)

    prob_label = ttk.Label(data_frame, text="Введите желаемую доверительную вероятность:", font=("Helvetica", 12))
    prob_label.pack(pady=5, anchor="w")

    prob_entry = ttk.Entry(data_frame, width=50)
    prob_entry.pack(pady=5, fill=tk.X)
    prob_entry.insert(0, "0.95")
    prob_entry.focus_set()

    result_label = ttk.Label(data_frame, text="Результаты будут отображены здесь", font=("Helvetica", 12))
    result_label.pack(pady=10, anchor="w")

    button_frame = ttk.Frame(top_frame)
    button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)

    def load_data_from_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.read().strip()
                    data_entry.delete(0, tk.END)
                    data_entry.insert(0, data)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

    load_button = ttk.Button(button_frame, text="Загрузить элементы выборки из файла", command=load_data_from_file)
    load_button.pack(pady=5, fill=tk.X)

    def calculate_confidence_interval(func):
        input_text = data_entry.get()
        input_prob = prob_entry.get()
        try:
            data = list(map(float, input_text.split(",")))
            prob = float(input_prob)
            if func == "get_mean" and len(data) < 35:
                result = get_mean_interval_borders_t(selection_size=len(data), average_weight=mean(data),
                                                     unbased_disp=uvar(data, mean(data)), alpha=(1-prob))
            elif func == "get_mean" and len(data) >= 35:
                result = get_mean_inteval_borders_norm(selection_size=len(data), average_weight=mean(data),
                                                       std_deviation=uvar(data, mean(data))**0.5, confidence_prob=prob)
            elif func == get_variance_interval_borders_chisq:
                result = func(data=data, alpha=1-prob)
            elif func == get_error_estimation:
                result = func(data=data, alpha=1-prob)
            else:
                result = "Неизвестная функция"

            result_label.config(text=f"Результат: {result[:-1]}")
            update_plot(data, result)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def update_plot(data, result):
        if isinstance(result, tuple) and (len(result) == 2 or len(result) == 3):
            left = result[0]
            right = result[1]
        else:
            left, right = min(data), max(data)

        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        ax.axvline(x=left, color='red', linestyle='--', label='Левая граница')
        if len(result) == 3:
            if result[2] == "mean":
                ax.axvline(x=mean(data), color='blue', linestyle='--', label='Оценка среднего')
            elif result[2] == "var":
                ax.axvline(x=uvar(data), color='blue', linestyle='--', label='Оценка дисперсии')
        ax.axvline(x=right, color='green', linestyle='--', label='Правая граница')
        ax.axvspan(left, right, color='yellow', alpha=0.3)
        ax.legend()

        for widget in plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    style = ttk.Style()
    style.configure("TButton", background="DodgerBlue3")

    norm_button = ttk.Button(button_frame, text="Оценка выборочного среднего", command=lambda: calculate_confidence_interval("get_mean"))
    norm_button.pack(pady=5, fill=tk.X)

    chisq_button = ttk.Button(button_frame, text="Оценка дисперсии", command=lambda: calculate_confidence_interval(get_variance_interval_borders_chisq))
    chisq_button.pack(pady=5, fill=tk.X)

    error_button = ttk.Button(button_frame, text="Оценка ошибки", command=lambda: calculate_confidence_interval(get_error_estimation))
    error_button.pack(pady=5, fill=tk.X)

    plot_frame = ttk.Frame(main_frame)
    plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    button = ttk.Button(root, text="Открыть окно расчета доверительных интервалов", command=lambda: open_confidence_interval_window(root))
    button.pack(pady=20)
    root.mainloop()