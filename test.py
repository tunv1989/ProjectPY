import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ví dụ về Text Widget với Scrollbar")

# Tạo Text widget
text_widget = tk.Text(root, wrap='none', height=10, width=50)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Tạo Scrollbar
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Kết nối Scrollbar với Text widget
text_widget.config(yscrollcommand=scrollbar.set)

# Thêm nội dung vào Text widget
for i in range(100):
    text_widget.insert(tk.END, f"Dòng {i + 1}\n")

# Chạy vòng lặp chính của Tkinter
root.mainloop()