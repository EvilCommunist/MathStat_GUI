import tkinter as tk
from tkinter import *
import sys
import os

from handlers_functions.selection.one_dim_selection import *
from handlers_functions.standard_functions.math_functions import *

sys.path.append(os.path.abspath("python_interface/handlers_functions/selection"))


def open_new_window(root):

    new_window = tk.Toplevel(root)
    new_window.title("Выборка")
    new_window.geometry("400x400")

    close_button = tk.Button(new_window, text="<-", command=new_window.destroy)
    close_button.place(x=350, y=0)

    def starter():

        input_text = vector_1.get()

        try:

            data = list(map(float, input_text.split(",")))
            sorted_data = get_sort_data(data)
            mean1 = mean(sorted_data)
            disp = var_unbased(sorted_data, mean1)
            median = get_chosen_median(sorted_data)
            quartile = get_quartile(sorted_data)

            result_text = f"Среднее: {mean1}\nДисперсия: {disp}\nМедиана: {median}\nПервый квартиль: {quartile}"
            result_label.config(text=result_text)

        except Exception as e:

            result_label.config(text=f"Ошибка: {e}")

    def getter():
        text = vector_1.get()
        list_1.append(text)

    list_1 = []
    list_2 = []

    vector_1 = Entry(new_window)
    vector_1.pack(padx=30, pady=10)

    start_button = tk.Button(new_window, text="Вычислить", command=starter)
    start_button.pack()

    result_label = tk.Label(new_window, text="Результаты будут отображены здесь")
    result_label.pack()

    root.mainloop()
