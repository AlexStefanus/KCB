import tkinter as tk
from tkinter import ttk, messagebox
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
    # Membaca data keyboard dari file CSV menggunakan pandas
    keyboards_df = pd.read_csv('Keyboard.csv')

    # Mencari rentang harga tersedia untuk preferensi pengguna
    available_options = find_available_options(keyboards_df, connection_type, case_material, switch_type)

    if len(available_options) == 0:
        return "Mohon maaf, tidak ada keyboard yang sesuai dengan preferensi Anda."
    elif price_range not in available_options:
        available_ranges = "\n".join([f"{option[0]} - {option[1]}" for option in available_options])
        return f"Tidak ada keyboard yang sesuai dengan preferensi Anda di rentang harga {price_range}. Silakan coba rentang harga lain yang tersedia:\n{available_ranges}"

    # Membuat daftar node awal dari data keyboard
    start_nodes = [Node(row) for _, row in keyboards_df.iterrows()]

    # Mencari rekomendasi keyboard menggunakan BFS
    recommended_node = bfs(start_nodes, price_range, connection_type, case_material, switch_type)

    # Menampilkan rekomendasi keyboard
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

# Membuat GUI dengan tkinter
root = tk.Tk()
root.title("Sistem Rekomendasi Keyboard")

tk.Label(root, text="Rentang Harga").grid(row=0, column=0, pady=5)
price_var = tk.StringVar()
price_options = ["Di bawah 400.000", "Di bawah 500.000", "Di bawah 700.000", "Di bawah 1.000.000", "Di atas 1.000.000"]
price_menu = ttk.Combobox(root, textvariable=price_var, values=price_options)
price_menu.grid(row=0, column=1, pady=5)

tk.Label(root, text="Jenis Koneksi").grid(row=1, column=0, pady=5)
connection_var = tk.StringVar()
connection_options = ["Wired", "Wireless"]
connection_menu = ttk.Combobox(root, textvariable=connection_var, values=connection_options)
connection_menu.grid(row=1, column=1, pady=5)

tk.Label(root, text="Material Case").grid(row=2, column=0, pady=5)
case_var = tk.StringVar()
case_options = ["plastic", "aluminium"]
case_menu = ttk.Combobox(root, textvariable=case_var, values=case_options)
case_menu.grid(row=2, column=1, pady=5)

tk.Label(root, text="Jenis Switch").grid(row=3, column=0, pady=5)
switch_var = tk.StringVar()
switch_options = ["linear", "tactile", "clicky"]
switch_menu = ttk.Combobox(root, textvariable=switch_var, values=switch_options)
switch_menu.grid(row=3, column=1, pady=5)

submit_button = tk.Button(root, text="Dapatkan Rekomendasi", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
