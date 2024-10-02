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

    frame = ttk.Frame(new_window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    data_label = ttk.Label(frame, text="Введите данные через запятую:", font=("Helvetica", 12))
    data_label.grid(row=0, column=0, pady=10, sticky="w")

    data_entry = ttk.Entry(frame, width=50)
    data_entry.grid(row=1, column=0, pady=10, sticky="w")

    prob_label = ttk.Label(frame, text="Введите желаемую доверительную вероятность:", font=("Helvetica", 12))
    prob_label.grid(row=3, column=0, pady=10, sticky="w")

    prob_entry_frame = ttk.Frame(frame)
    prob_entry_frame.grid(row=4, column=0, pady=10, sticky="w")

    prob_entry = ttk.Entry(prob_entry_frame, width=50)
    prob_entry.grid(row=5, column=0, pady=10, sticky="w")
    prob_entry.insert(0, "0.95")
    prob_entry.focus_set()

    result_label = ttk.Label(frame, text="Результаты будут отображены здесь", font=("Helvetica", 12))
    result_label.grid(row=6, column=0, pady=20, sticky="w")

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

    load_button = ttk.Button(frame, text="Загрузить выборку из файла", command=load_data_from_file)
    load_button.grid(row=1, column=1, pady=10, padx=20)

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
                result = func(data=data)
            elif func == get_error_estimation:
                result = func(data=data)
            else:
                result = "Неизвестная функция"
            result_label.config(text=f"Результат: {result}")
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

    norm_button = ttk.Button(frame, text="Расчет для выборочного среднего", command=lambda:
                             calculate_confidence_interval("get_mean"))
    norm_button.grid(row=3, column=1, pady=10, padx=20, sticky="w")

    chisq_button = ttk.Button(frame, text="Расчет для дисперсии", command=lambda: calculate_confidence_interval(get_variance_interval_borders_chisq))
    chisq_button.grid(row=4, column=1, pady=10, padx=20, sticky="w")

    error_button = ttk.Button(frame, text="Расчет для оценки ошибки", command=lambda: calculate_confidence_interval(get_error_estimation))
    error_button.grid(row=5, column=1, pady=10, padx=20, sticky="w")

    plot_frame = ttk.Frame(frame)
    plot_frame.grid(row=7, column=0, rowspan=7, padx=20, pady=10, sticky="nsew")

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    frame.grid_columnconfigure(2, weight=1)
    frame.grid_rowconfigure(7, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    button = ttk.Button(root, text="Открыть окно расчета доверительных интервалов", command=lambda: open_confidence_interval_window(root))
    button.pack(pady=20)
    root.mainloop()