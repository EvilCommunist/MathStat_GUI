import tkinter as tk
from tkinter import *
import sys
import os

sys.path.append(os.path.abspath('python_interface/handlers_functions/selection'))
from one_dim_selection import *


def open_new_window(root):
    
    new_window = tk.Toplevel(root)
    new_window.title("Выборка")
    new_window.geometry('400x400')
    
    close_button = tk.Button(new_window, text = ('<-'), command = new_window.destroy)
    close_button.place(x = 350, y = 0)
    
    # Entry
    #frame = Frame(new_window)
    #frame.pack()
    
   # vector_entry = Entry(frame, width = 20)
    #vector_entry.insert(0, "")
    #vector_entry.pack(padx = 5, pady = 5)
    
    def starter():
        
        input_text = vector_1.get()
        
        try:
            
            data = list(map(float, input_text.split(',')))
            sorted_data = get_sort_data(data)
            mean = get_chosen_middle(sorted_data)
            disp = get_chosen_disp(sorted_data, mean)
            median = get_chosen_median(sorted_data)
            quartile = get_quartile(sorted_data)
        
            result_text = f"Среднее: {mean}\nДисперсия: {disp}\nМедиана: {median}\nПервый квартиль: {quartile}"
            result_label.config(text=result_text)
            
        except Exception as e:
            
            result_label.config(text=f"Ошибка: {e}")

    
    def getter():
        text = vector_1.get()
        list_1.append(text)
    
    
    list_1 = []
    list_2 = []
    
    vector_1 = Entry(new_window)
    vector_1.pack(padx=30,pady=10)
    
    start_button = tk.Button(root, text="Вычислить", command=starter)
    start_button.pack()
    
    result_label = tk.Label(root, text="Результаты будут отображены здесь")
    result_label.pack()
    
    
    
    root.mainloop()