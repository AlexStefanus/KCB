import sys
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

def recommend_keyboard(preference):
    df = pd.read_csv('Keyboard.csv')
    # Dummy recommendation logic based on user preference
    recommendations = df[df['Type'].str.contains(preference, case=False)]
    return recommendations

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python keyboard.py <preference>")
        sys.exit(1)
    
    preference = sys.argv[1]
    recommendations = recommend_keyboard(preference)
    print(recommendations.to_json(orient='records'))

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

def get_keyboard_recommendation():
    print("Selamat datang di program rekomendasi keyboard!")

    # Meminta input dari pengguna melalui pilihan ganda
    price_range = get_price_range()
    connection_type = get_connection_type()
    case_material = get_case_material()
    switch_type = get_switch_type()

    # Membaca data keyboard dari file CSV menggunakan pandas
    keyboards_df = pd.read_csv('Keyboard.csv')

    # Mencari rentang harga tersedia untuk preferensi pengguna
    available_options = find_available_options(keyboards_df, connection_type, case_material, switch_type)

    if len(available_options) == 0:
        print("Mohon maaf, tidak ada keyboard yang sesuai dengan preferensi Anda.")
        return
    elif price_range not in available_options:
        print(f"Tidak ada keyboard yang sesuai dengan preferensi Anda di rentang harga {price_range}.")
        print("Silakan coba rentang harga lain yang tersedia:")
        for option in available_options:
            print(f"- {option[0]} - {option[1]}")
        return

    # Membuat daftar node awal dari data keyboard
    start_nodes = [Node(row) for _, row in keyboards_df.iterrows()]

    # Mencari rekomendasi keyboard menggunakan BFS
    recommended_node = bfs(start_nodes, price_range, connection_type, case_material, switch_type)

    # Menampilkan rekomendasi keyboard
    if recommended_node:
        print("Rekomendasi keyboard untuk Anda:")
        print(recommended_node)
    else:
        print("Mohon maaf, tidak ada keyboard yang sesuai dengan preferensi Anda.")

def get_price_range():
    print("Pilih rentang harga:")
    print("1. Di bawah 400.000")
    print("2. Di bawah 500.000")
    print("3. Di bawah 700.000")
    print("4. Di bawah 1.000.000")
    print("5. Di atas 1.000.000")
    choice = input("Masukkan pilihan Anda (1-5): ")
    if choice == "1":
        return (0, 399999)
    elif choice == "2":
        return (400000, 499999)
    elif choice == "3":
        return (500000, 699999)
    elif choice == "4":
        return (700000, 999999)
    else:
        return (1000000, float('inf'))

def get_connection_type():
    print("Pilih jenis koneksi:")
    print("1. Wired")
    print("2. Wireless")
    choice = input("Masukkan pilihan Anda (1 atau 2): ")
    if choice == "1":
        return "Wired"
    else:
        return "Wireless"

def get_case_material():
    print("Pilih material case:")
    print("1. Plastic")
    print("2. Aluminium")
    choice = input("Masukkan pilihan Anda (1 atau 2): ")
    if choice == "1":
        return "plastic"
    else:
        return "aluminium"

def get_switch_type():
    print("Pilih jenis switch:")
    print("1. Linear")
    print("2. Tactile")
    print("3. Clicky")
    choice = input("Masukkan pilihan Anda (1-3): ")
    if choice == "1":
        return "linear"
    elif choice == "2":
        return "tactile"
    else:
        return "clicky"

# Menjalankan program
get_keyboard_recommendation()