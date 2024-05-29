import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ví dụ về Checkbox")

# Hàm xử lý sự kiện khi checkbox thay đổi trạng thái
def on_checkbox_change():
    chophep = False
    if var1.get():
        chophep = True
    print(chophep)

# Tạo các biến BooleanVar để giữ trạng thái của checkbox
var1 = tk.BooleanVar()

# Tạo các checkbox
checkbox1 = tk.Checkbutton(root, text="Tùy chọn 1", variable=var1, command=on_checkbox_change)
checkbox1.pack(pady=5)


# Chạy vòng lặp chính của Tkinter
root.mainloop()