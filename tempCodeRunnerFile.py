import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import pandas as pd
from collections import deque

class Node:
    def __init__(self, keyboard_data):
        self.merek = keyboard_data['Merek']
        self.seri = keyboard_data['Seri']
        self.harga = keyboard_data['Harga']
        self.koneksi = keyboard_data['Koneksi']
        self.case = keyboard_data['Case']
        self.switch = keyboard_data['Switch']
        self.parent = None

    def __str__(self):
        return f"{self.merek} {self.seri} (Harga: {self.harga}, Koneksi: {self.koneksi}, Case: {self.case}, Switch: {self.switch})"

def bfs(start_nodes, price_range, connection_type, case_material, switch_type):
    queue = deque(start_nodes)
    visited = set()

    while queue:
        node = queue.popleft()
        if (
            node.harga >= price_range[0]
            and node.harga <= price_range[1]
            and node.koneksi == connection_type
            and node.case.lower() == case_material
            and switch_type in node.switch.lower()
        ):
            return node

        visited.add(node)

    return None

def find_available_options(keyboards_df, connection_type, case_material, switch_type):
    available_options = []
    for price_range in [(0, 399999), (400000, 499999), (500000, 699999), (700000, 999999), (1000000, float('inf'))]:
        matching_keyboards = keyboards_df[
            (keyboards_df['Harga'].between(price_range[0], price_range[1]))
            & (keyboards_df['Koneksi'] == connection_type)
            & (keyboards_df['Case'].str.lower() == case_material)
            & (keyboards_df['Switch'].str.lower().str.contains(switch_type))
        ]
        if not matching_keyboards.empty:
            available_options.append(price_range)
    return available_options

def get_keyboard_recommendation(price_range, connection_type, case_material, switch_type):
    keyboards_df = pd.read_csv('Keyboard.csv')
    available_options = find_available_options(keyboards_df, connection_type, case_material, switch_type)

    if len(available_options) == 0:
        return "Mohon maaf, tidak ada keyboard yang sesuai dengan preferensi Anda."
    elif price_range not in available_options:
        available_ranges = "\n".join([f"{option[0]} - {option[1]}" for option in available_options])
        return f"Tidak ada keyboard yang sesuai dengan preferensi Anda di rentang harga {price_range}. Silakan coba rentang harga lain yang tersedia:\n{available_ranges}"

    start_nodes = [Node(row) for _, row in keyboards_df.iterrows()]
    recommended_node = bfs(start_nodes, price_range, connection_type, case_material, switch_type)

    if recommended_node:
        return f"Rekomendasi keyboard untuk Anda:\n{recommended_node}"
    else:
        return "Mohon maaf, tidak ada keyboard yang sesuai dengan preferensi Anda."

def on_submit():
    try:
        price_range = get_price_range()
        connection_type = connection_var.get()
        case_material = case_var.get()
        switch_type = switch_var.get()

        recommendation = get_keyboard_recommendation(price_range, connection_type, case_material, switch_type)
        messagebox.showinfo("Rekomendasi Keyboard", recommendation)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_price_range():
    choice = price_var.get()
    if choice == "Di bawah 400.000":
        return (0, 399999)
    elif choice == "Di bawah 500.000":
        return (400000, 499999)
    elif choice == "Di bawah 700.000":
        return (500000, 699999)
    elif choice == "Di bawah 1.000.000":
        return (700000, 999999)
    else:
        return (1000000, float('inf'))

# Membuat GUI dengan ttkbootstrap
root = tb.Window(themename="superhero")
root.title("Sistem Rekomendasi Keyboard")
root.geometry("1024x768")  # Mengatur rasio 4:3
root.resizable(True, True)

frame = tb.Frame(root, padding="20")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Menempatkan frame di tengah

title_label = tb.Label(frame, text="Sistem Rekomendasi Keyboard", font=("Arial", 24, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

tb.Label(frame, text="Rentang Harga", font=("Arial", 16)).grid(row=1, column=0, pady=10, sticky=tk.E)
price_var = tk.StringVar()
price_options = ["Di bawah 400.000", "Di bawah 500.000", "Di bawah 700.000", "Di bawah 1.000.000", "Di atas 1.000.000"]
price_menu = tb.Combobox(frame, textvariable=price_var, values=price_options, state="readonly", font=("Arial", 14))
price_menu.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

tb.Label(frame, text="Jenis Koneksi", font=("Arial", 16)).grid(row=2, column=0, pady=10, sticky=tk.E)
connection_var = tk.StringVar()
connection_options = ["Wired", "Wireless"]
connection_menu = tb.Combobox(frame, textvariable=connection_var, values=connection_options, state="readonly", font=("Arial", 14))
connection_menu.grid(row=2, column=1, pady=10, padx=10, sticky=tk.W)

tb.Label(frame, text="Material Case", font=("Arial", 16)).grid(row=3, column=0, pady=10, sticky=tk.E)
case_var = tk.StringVar()
case_options = ["plastic", "aluminium"]
case_menu = tb.Combobox(frame, textvariable=case_var, values=case_options, state="readonly", font=("Arial", 14))
case_menu.grid(row=3, column=1, pady=10, padx=10, sticky=tk.W)

tb.Label(frame, text="Jenis Switch", font=("Arial", 16)).grid(row=4, column=0, pady=10, sticky=tk.E)
switch_var = tk.StringVar()
switch_options = ["linear", "tactile", "clicky"]
switch_menu = tb.Combobox(frame, textvariable=switch_var, values=switch_options, state="readonly", font=("Arial", 14))
switch_menu.grid(row=4, column=1, pady=10, padx=10, sticky=tk.W)

# Menggunakan Style untuk mengatur font pada Button
style = tb.Style()
style.configure('TButton', font=('Arial', 16))

submit_button = tb.Button(frame, text="Dapatkan Rekomendasi", command=on_submit, bootstyle=SUCCESS, style='TButton')
submit_button.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
