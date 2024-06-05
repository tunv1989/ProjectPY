import tkinter as tk
from tkinter import messagebox

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

    except ValueError as ve:
        messagebox.showerror("Lỗi", str(ve))
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi không mong muốn: {str(e)}")