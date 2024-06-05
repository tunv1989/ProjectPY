import tkinter as tk
from tkinter import messagebox, ttk

# Hàm xử lý sự kiện khi nhấn nút "Lưu"
def save_text(entry, checkbox_var, combobox1, combobox2, combobox3, data_list):
    try:
        text = entry.get().strip()  # Lấy dữ liệu từ TextBox và loại bỏ khoảng trắng thừa
        combo1_text = combobox1.get().strip()
        combo2_text = combobox2.get().strip()
        combo3_text = combobox3.get().strip()

        if not text:
            raise ValueError("TextBox không có dữ liệu.")
        if not combo1_text:
            raise ValueError("ComboBox 1 không có dữ liệu.")
        if not combo2_text:
            raise ValueError("ComboBox 2 không có dữ liệu.")
        if not combo3_text:
            raise ValueError("ComboBox 3 không có dữ liệu.")

        if checkbox_var.get():
            text += ",checkbox=True"

        # Ghép tất cả dữ liệu lại
        combined_data = f"{text},{combo1_text},{combo2_text},{combo3_text}"
        data_list.append(combined_data)  # Lưu dữ liệu vào danh sách

        messagebox.showinfo("Thông báo", "Dữ liệu đã được lưu!")
        entry.delete(0, tk.END)  # Xóa nội dung TextBox sau khi lưu
        checkbox_var.set(False)  # Xóa dấu tích của CheckBox
        print(data_list)

    except ValueError as ve:
        messagebox.showerror("Lỗi", str(ve))
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi không mong muốn: {str(e)}")

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