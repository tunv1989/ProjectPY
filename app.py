import tkinter as tk
from tkinter import ttk
import Ultility


root = tk.Tk()
root.title("CHƯƠNG TRÌNH KỸ THUẬT AN TOÀN")

# Lấy kích thước màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Thiết lập kích thước cửa sổ
root.geometry(f"{screen_width}x{screen_height}")

# Thiết lập tọa độ gốc
a = 0
b = 20

# Path các file config
NhanVien_Path = "config/NhanVien.txt"

# Đọc danh sách từ file NhanVien.txt để lấy dữ liệu về Tên và chức vụ đơn vị công tác
DonVi_List = Ultility.ReadfileTxt(NhanVien_Path)
Name_List = []
Chucvu_List = []
DienLuc_List = []
MaNV_List = []
for ele in DonVi_List:
    Info = ele.split(", ")
    Name_List.append(Info[0])
    Chucvu_List.append(Info[1])
    DienLuc_List.append(Info[2])
    MaNV_List.append(Info[3])

# Tạo một Label "Đại diện đơn vị công tác"
label = tk.Label(root, text="1. Đại diện đơn vị công tác", font=("Arial", 11))
label.place(x=10 + a, y=50 + b)

# Tạo một Label "Chức vụ đại diện đơn vị công tác"
label = tk.Label(root, text="Chức vụ", font=("Arial", 11))
label.place(x=450 + a, y=50 + b)

# Tạo một Label "Đơn vị công tác"
label = tk.Label(root, text="Đơn vị", font=("Arial", 11))
label.place(x=750 + a, y=50 + b)

# Tạo một Label "Mã nhân viên Đơn vị công tác"
label = tk.Label(root, text="Mã NV", font=("Arial", 11))
label.place(x=1000 + a, y=50 + b)

# Tạo một Text widget chức vụ nhân viên đơn vị công tác
txt_ChucvuDVCT = tk.Text(root, width=20, height=0, font="Arial")
txt_ChucvuDVCT.place(x=520 + a, y=50 + b)

# Tạo một Text widget "đơn vị nhân viên đơn vị công tác"
txt_DonViDVCT = tk.Text(root, width=15, height=0, font="Arial")
txt_DonViDVCT.place(x=820 + a, y=50 + b)

# Tạo một Text widget "Mã nhân viên đơn vị công tác"
txt_MaNVDVCT = tk.Text(root, width=5, height=0, font="Arial")
txt_MaNVDVCT.place(x=1060 + a, y=50 + b)

# Tạo thanh lựa chọn và thiết lập các lựa chọn
selected_option_NVDVCT = tk.StringVar()   # Tạo biến lưu trữ lựa chọn được chọn
cbo_NVDVCT = ttk.Combobox(root, textvariable=selected_option_NVDVCT, values=Name_List, font="Arial")
cbo_NVDVCT.place(x=200 + a, y=50 + b)

# Hàm để tự động điền chức vụ, đơn vị theo tên nhân viên đơn vị công tác
def on_combobox_select(event):
    txt_ChucvuDVCT.delete('1.0', tk.END)
    txt_DonViDVCT.delete('1.0', tk.END)
    txt_MaNVDVCT.delete('1.0', tk.END)
    value_Name = cbo_NVDVCT.get()  # Hoặc dùng selected_option.get()
    for i in range(len(Name_List)):
        if Name_List[i] == value_Name:
            txt_ChucvuDVCT.insert(tk.END, Chucvu_List[i])
            txt_DonViDVCT.insert(tk.END, DienLuc_List[i])
            txt_MaNVDVCT.insert(tk.END, MaNV_List[i])

cbo_NVDVCT.bind("<<ComboboxSelected>>", on_combobox_select)

#=================ĐƠN VỊ QUẢN LÝ VẬN HÀNH=============================================
# Tạo một Label "Đại diện đơn vị QLVH"
label = tk.Label(root, text="2. Đại diện đơn vị QLVH", font=("Arial", 11))
label.place(x=10 + a, y=90 + b)

# Tạo một Label "Chức vụ đại diện đơn vị công tác"
label = tk.Label(root, text="Chức vụ", font=("Arial", 11))
label.place(x=450 + a, y=90 + b)

# Tạo một Label "Đơn vị công tác"
label = tk.Label(root, text="Đơn vị", font=("Arial", 11))
label.place(x=750 + a, y=90 + b)

# Tạo một Label "Mã nhân viên Đơn vị QLVH"
label = tk.Label(root, text="Mã NV", font=("Arial", 11))
label.place(x=1000 + a, y=90 + b)

# Tạo thanh lựa chọn và thiết lập các lựa chọn cho nhân viên đơn vị QLVH
selected_option_NVQLVH_1 = tk.StringVar()   # Tạo biến lưu trữ lựa chọn được chọn
cbo_NVQLVH_1 = ttk.Combobox(root, textvariable=selected_option_NVQLVH_1, values=Name_List, font="Arial")
cbo_NVQLVH_1.place(x=200 + a, y=90 + b)

# Tạo một Text widget chức vụ nhân viên đơn vị công tác
txt_ChucvuQLVH_1 = tk.Text(root, width=20, height=0, font="Arial")
txt_ChucvuQLVH_1.place(x=520 + a, y=90 + b)

# Tạo một Text widget "đơn vị nhân viên đơn vị công tác"
txt_DonViQLVH_1 = tk.Text(root, width=15, height=0, font="Arial")
txt_DonViQLVH_1.place(x=820 + a, y=90 + b)

# Tạo một Text widget "Mã nhân viên QLVH"
txt_MaNVQLVH_1 = tk.Text(root, width=5, height=0, font="Arial")
txt_MaNVQLVH_1.place(x=1060 + a, y=90 + b)

# Hàm để tự động điền chức vụ, đơn vị theo tên nhân viên đơn vị công tác
def on_combobox_select_qlvh_1(event):
    txt_ChucvuQLVH_1.delete('1.0', tk.END)
    txt_DonViQLVH_1.delete('1.0', tk.END)
    txt_MaNVQLVH_1.delete('1.0', tk.END)
    value_Name = cbo_NVQLVH_1.get()  # Hoặc dùng selected_option.get()
    for i in range(len(Name_List)):
        if Name_List[i] == value_Name:
            txt_ChucvuQLVH_1.insert(tk.END, Chucvu_List[i])
            txt_DonViQLVH_1.insert(tk.END, DienLuc_List[i])
            txt_MaNVQLVH_1.insert(tk.END, MaNV_List[i])

cbo_NVQLVH_1.bind("<<ComboboxSelected>>", on_combobox_select_qlvh_1)

# Tạo thanh lựa chọn và thiết lập các lựa chọn cho nhân viên đơn vị QLVH
selected_option_NVQLVH_2 = tk.StringVar()   # Tạo biến lưu trữ lựa chọn được chọn
cbo_NVQLVH_2 = ttk.Combobox(root, textvariable=selected_option_NVQLVH_2, values=Name_List, font="Arial")
cbo_NVQLVH_2.place(x=200 + a, y=130 + b)

# Tạo một Text widget chức vụ nhân viên đơn vị công tác
txt_ChucvuQLVH_2 = tk.Text(root, width=20, height=0, font="Arial")
txt_ChucvuQLVH_2.place(x=520 + a, y=130 + b)

# Tạo một Text widget "đơn vị nhân viên đơn vị công tác"
txt_DonViQLVH_2 = tk.Text(root, width=15, height=0, font="Arial")
txt_DonViQLVH_2.place(x=820 + a, y=130 + b)

# Tạo một Text widget "Mã nhân viên QLVH"
txt_MaNVQLVH_2 = tk.Text(root, width=5, height=0, font="Arial")
txt_MaNVQLVH_2.place(x=1060 + a, y=130 + b)

# Hàm để tự động điền chức vụ, đơn vị theo tên nhân viên đơn vị công tác
def on_combobox_select_qlvh_2(event):
    txt_ChucvuQLVH_2.delete('1.0', tk.END)
    txt_DonViQLVH_2.delete('1.0', tk.END)
    txt_MaNVQLVH_2.delete('1.0', tk.END)
    value_Name = cbo_NVQLVH_2.get()  # Hoặc dùng selected_option.get()
    for i in range(len(Name_List)):
        if Name_List[i] == value_Name:
            txt_ChucvuQLVH_2.insert(tk.END, Chucvu_List[i])
            txt_DonViQLVH_2.insert(tk.END, DienLuc_List[i])
            txt_MaNVQLVH_2.insert(tk.END, MaNV_List[i])
cbo_NVQLVH_2.bind("<<ComboboxSelected>>", on_combobox_select_qlvh_2)

#=================ĐƠN VỊ CÓ LIÊN QUAN=============================================

# Tạo một Label "Đại diện đơn vị QLVH"
label = tk.Label(root, text="3. Đại diện các đơn vị LQ", font=("Arial", 11))
label.place(x=10 + a, y=170 + b)

# Tạo một Label "Chức vụ đại diện đơn vị công tác"
label = tk.Label(root, text="Chức vụ", font=("Arial", 11))
label.place(x=450 + a, y=170 + b)

# Tạo một Label "Đơn vị công tác"
label = tk.Label(root, text="Đơn vị", font=("Arial", 11))
label.place(x=750 + a, y=170 + b)

# Tạo một Label "Mã nhân viên Đơn vị QLVH"
label = tk.Label(root, text="Mã NV", font=("Arial", 11))
label.place(x=1000 + a, y=170 + b)

# Tạo thanh lựa chọn và thiết lập các lựa chọn cho nhân viên đơn vị QLVH
selected_option_DVLQ_1 = tk.StringVar()   # Tạo biến lưu trữ lựa chọn được chọn
cbo_DVLQ_1 = ttk.Combobox(root, textvariable=selected_option_DVLQ_1, values=Name_List, font="Arial")
cbo_DVLQ_1.place(x=200 + a, y=170 + b)

# Tạo một Text widget chức vụ nhân viên đơn vị công tác
txt_ChucvuDVLQ_1 = tk.Text(root, width=20, height=0, font="Arial")
txt_ChucvuDVLQ_1.place(x=520 + a, y=170 + b)

# Tạo một Text widget "đơn vị nhân viên đơn vị công tác"
txt_DonViDVLQ_1 = tk.Text(root, width=15, height=0, font="Arial")
txt_DonViDVLQ_1.place(x=820 + a, y=170 + b)

# Tạo một Text widget "Mã nhân viên QLVH"
txt_MaNVDVLQ_1 = tk.Text(root, width=5, height=0, font="Arial")
txt_MaNVDVLQ_1.place(x=1060 + a, y=170 + b)

#=================ĐỊA ĐIỂM, THỜI GIAN TIẾN HÀNH CÔNG TÁC=============================================
# Tạo một Label "Đại diện đơn vị QLVH"
label = tk.Label(root, text="4. Địa điểm thực hiện CT", font=("Arial", 11))
label.place(x=10 + a, y=230 + b)

# Tạo một Text widget "Địa điểm thực hiện công tác"
txt_DiaDiemLV = tk.Text(root, width=84, height=5, font="Arial")
txt_DiaDiemLV.place(x=200 + a, y=230 + b)

#=================NỘI DUNG CÔNG VIỆC=============================================
# Tạo một Label "5. Nội dung công việc"
label = tk.Label(root, text="5. Nội dung công việc", font=("Arial", 11))
label.place(x=10 + a, y=350 + b)

# Tạo một Text widget "5. Nội dung công việc"
txt_NoiDungCV = tk.Text(root, width=84, height=5, font="Arial")
txt_NoiDungCV.place(x=200 + a, y=350 + b)

#=================THỜI GIAN TIẾN HÀNH CÔNG VIỆC=============================================
# Tạo một Label "5. Nội dung công việc"
label = tk.Label(root, text="5. Nội dung công việc", font=("Arial", 11))
label.place(x=10 + a, y=350 + b)

# Tạo một Text widget "5. Nội dung công việc"
txt_NoiDungCV = tk.Text(root, width=84, height=5, font="Arial")
txt_NoiDungCV.place(x=200 + a, y=350 + b)

root.mainloop()