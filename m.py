import tkinter as tk
from tkinter import ttk
from helper import save_text  # Import hàm từ file helper.py

# Danh sách để lưu dữ liệu từ TextBox và ComboBox
data_list = []

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Lưu dữ liệu từ TextBox và ComboBox vào List")

# Tạo TextBox
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=10)

# Tạo CheckBox
checkbox_var = tk.BooleanVar()  # Biến để theo dõi trạng thái của CheckBox
checkbox = tk.Checkbutton(root, text="Thêm 'checkbox=True'", variable=checkbox_var)
checkbox.pack(padx=10, pady=10)

# Tạo các ComboBox
combobox1 = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox1.pack(padx=10, pady=10)
combobox2 = ttk.Combobox(root, values=["Option A", "Option B", "Option C"])
combobox2.pack(padx=10, pady=10)
combobox3 = ttk.Combobox(root, values=["Choice X", "Choice Y", "Choice Z"])
combobox3.pack(padx=10, pady=10)

# Tạo Button và truyền các đối tượng cần thiết vào hàm save_text
button = tk.Button(root, text="Lưu", command=lambda: save_text(entry, checkbox_var, combobox1, combobox2, combobox3, data_list))
button.pack(padx=10, pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()