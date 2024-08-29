import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from python_interface.handlers_functions.confidence_interval.confidence_interval import *

def open_confidence_interval_window(root):
    new_window = tk.Toplevel(root)
    new_window.title("Расчет доверительных интервалов")
    new_window.geometry("600x600")
    new_window.configure(background='white')

    frame = ttk.Frame(new_window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    data_label = ttk.Label(frame, text="Введите данные через запятую:", font=("Helvetica", 12))
    data_label.grid(row=0, column=0, pady=10, sticky="w")

    data_entry = ttk.Entry(frame, width=50)
    data_entry.grid(row=1, column=0, pady=10, sticky="w")

    result_label = ttk.Label(frame, text="Результаты будут отображены здесь", font=("Helvetica", 12))
    result_label.grid(row=2, column=0, pady=20, sticky="w")

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

    load_button = ttk.Button(frame, text="Загрузить из файла", command=load_data_from_file)
    load_button.grid(row=1, column=1, padx=10)

    def calculate_confidence_interval(func):
        input_text = data_entry.get()
        try:
            data = list(map(float, input_text.split(",")))
            if func == get_inteval_borders_norm:
                result = func(selection_size=len(data), average_weight=mean(data), std_deviation=uvar(data, mean(data))**0.5)
            elif func == get_interval_borders_t:
                result = func(selection_size=len(data), average_weight=mean(data), unbased_disp=uvar(data, mean(data)))
            elif func == get_interval_borders_chisq:
                result = func(data=data)
            elif func == get_error_estimation:
                result = func(data=data)
            else:
                result = "Неизвестная функция"
            result_label.config(text=f"Результат: {result}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    style = ttk.Style()
    style.configure("TButton", background="DodgerBlue3")

    norm_button = ttk.Button(frame, text="Расчет для нормального распределения", command=lambda: calculate_confidence_interval(get_inteval_borders_norm))
    norm_button.grid(row=3, column=0, pady=10, sticky="w")

    t_button = ttk.Button(frame, text="Расчет для t-распределения", command=lambda: calculate_confidence_interval(get_interval_borders_t))
    t_button.grid(row=4, column=0, pady=10, sticky="w")

    chisq_button = ttk.Button(frame, text="Расчет для chi-squared распределения", command=lambda: calculate_confidence_interval(get_interval_borders_chisq))
    chisq_button.grid(row=5, column=0, pady=10, sticky="w")

    error_button = ttk.Button(frame, text="Расчет для оценки ошибки", command=lambda: calculate_confidence_interval(get_error_estimation))
    error_button.grid(row=6, column=0, pady=10, sticky="w")

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)