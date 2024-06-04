import tkinter as tk
from tkinter import ttk
import Ultility
from tkcalendar import DateEntry

root = tk.Tk()
root.title("CHƯƠNG TRÌNH KỸ THUẬT AN TOÀN")

# Lấy kích thước màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Thiết lập kích thước cửa sổ
root.geometry(f"{screen_width}x{screen_height}")

# Thiết lập tọa độ gốc
a = 0
b = -20

# Path các file config
NhanVien_Path = "config/NhanVien.txt"

# Đọc danh sách từ file NhanVien.txt để lấy dữ liệu về Tên và chức vụ đơn vị công tác
NhanVien_List = Ultility.ReadfileTxt(NhanVien_Path)
Name_List = []
Chucvu_List = []
DienLuc_List = []
MaNV_List = []
for ele in NhanVien_List:
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
# Thời gian bắt đầu
label = tk.Label(root, text="6. Thời gian bắt đầu", font=("Arial", 11))
label.place(x=10 + a, y=460 + b)
#Giờ bắt đầu
txt_GioBatDau = tk.Text(root, width=10, height=0, font="Arial")
txt_GioBatDau.place(x=200 + a, y=460 + b)
label = tk.Label(root, text="giờ", font=("Arial", 11))
label.place(x=300 + a, y=460 + b)
#Phút bắt đầu
txt_PhutBatDau = tk.Text(root, width=10, height=0, font="Arial")
txt_PhutBatDau.place(x=340 + a, y=460 + b)
label = tk.Label(root, text="phút", font=("Arial", 11))
label.place(x=440 + a, y=460 + b)
#Ngày bắt đầu
date_NgayBatDau = DateEntry(root, width=16, background='dark', foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
date_NgayBatDau.place(x=490 + a, y=460 + b)
label = tk.Label(root, text="Ngày", font=("Arial", 11))
label.place(x=620 + a, y=460 + b)

# Thời gian kết thúc
label = tk.Label(root, text="7. Thời gian kết thúc", font=("Arial", 11))
label.place(x=10 + a, y=500 + b)
#Giờ bắt đầu
txt_GioKetThuc = tk.Text(root, width=10, height=0, font="Arial")
txt_GioKetThuc.place(x=200 + a, y=500 + b)
label = tk.Label(root, text="giờ", font=("Arial", 11))
label.place(x=300 + a, y=500 + b)
#Phút bắt đầu
txt_PhutKetThuc = tk.Text(root, width=10, height=0, font="Arial")
txt_PhutKetThuc.place(x=340 + a, y=500 + b)
label = tk.Label(root, text="phút", font=("Arial", 11))
label.place(x=440 + a, y=500 + b)
#Ngày bắt đầu
date_NgayKetThuc = DateEntry(root, width=16, background='dark', foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
date_NgayKetThuc.place(x=490 + a, y=500 + b)
label = tk.Label(root, text="Ngày", font=("Arial", 11))
label.place(x=620 + a, y=500 + b)

#=================NỘI DUNG CÁC BIỆN PHÁP AN TOÀN=============================================

# Path các file config
DonVi_Path = "config/DonVi.txt"

# Đọc danh sách từ file NhanVien.txt để lấy dữ liệu về Tên và chức vụ đơn vị công tác
DonVi_List = Ultility.ReadfileTxt(DonVi_Path)
TenDonVi_List = []
MaDonVi_List = []
for donvi in DonVi_List:
    Info = donvi.split(", ")
    TenDonVi_List.append(Info[0])
    MaDonVi_List.append(Info[1])


# BPAT để tiến hành công việc
label = tk.Label(root, text="8. Biện pháp an toàn", font=("Arial", 11))
label.place(x=10 + a, y=540 + b)
# txt_NhapBPAT = Ultility.AutocompleteEntry(root, width=84, font="Arial")
txt_NhapBPAT = Ultility.AutocompleteText(root, width=84, height=2, font="Arial")
txt_NhapBPAT.place(x=200 + a, y=540 + b)

# Đơn vị thực hiện
label = tk.Label(root, text="8.1 Đơn vị thực hiện", font=("Arial", 11))
label.place(x=50 + a, y=600 + b)

# Tạo thanh lựa chọn và thiết lập các lựa chọn cho nhân viên đơn vị QLVH
selected_option_DonVi = tk.StringVar()   # Tạo biến lưu trữ lựa chọn được chọn
cbo_DonViTH = ttk.Combobox(root, textvariable=selected_option_DonVi, values=TenDonVi_List, font="Arial")
cbo_DonViTH.place(x=200 + a, y=600 + b)
cbo_DonViTH.current(0) # Đặt giá trị mặc định lựa chọn đầu tiên

# Path các file config
BoPhan_Path = "config/BoPhan.txt"

# Đọc danh sách từ file NhanVien.txt để lấy dữ liệu về Tên và chức vụ đơn vị công tác
BoPhan_List = Ultility.ReadfileTxt(BoPhan_Path)
TenBoPhan_List = []
MaBoPhan_List = []
for bophan in BoPhan_List:
    Info = bophan.split(", ")
    TenBoPhan_List.append(Info[0])
    MaBoPhan_List.append(Info[1])

# Bộ phận thực hiện
label = tk.Label(root, text="8.2 Bộ phận", font=("Arial", 11))
label.place(x=420 + a, y=600 + b)
# Tạo thanh lựa chọn và thiết lập các lựa chọn cho nhân viên đơn vị QLVH
selected_option_BoPhanTH = tk.StringVar()   # Tạo biến lưu trữ lựa chọn được chọn
cbo_BoPhanTH = ttk.Combobox(root, textvariable=selected_option_BoPhanTH, values=TenBoPhan_List, font="Arial")
cbo_BoPhanTH.place(x=520 + a, y=600 + b)
cbo_BoPhanTH.current(0) # Đặt giá trị mặc định lựa chọn đầu tiên

# Điện lực thực hiện
DienLucTH_Path = "config/DienLuc.txt"

# Đọc danh sách từ file NhanVien.txt để lấy dữ liệu về Tên và chức vụ đơn vị công tác
DienLucTH_List = Ultility.ReadfileTxt(DienLucTH_Path)
TenDienLucTH_List = []
MaDienLucTH_List = []
for dienluc in DienLucTH_List:
    Info = dienluc.split(", ")
    TenDienLucTH_List.append(Info[0])
    MaDienLucTH_List.append(Info[1])

# Bộ phận thực hiện
label = tk.Label(root, text="8.3 Đơn vị", font=("Arial", 11))
label.place(x=740 + a, y=600 + b)
# Tạo thanh lựa chọn và thiết lập các lựa chọn cho nhân viên đơn vị QLVH
selected_option_DienLucTH = tk.StringVar()   # Tạo biến lưu trữ lựa chọn được chọn
cbo_DienLucTH = ttk.Combobox(root, textvariable=selected_option_DienLucTH, values=TenDienLucTH_List, font="Arial")
cbo_DienLucTH.place(x=820 + a, y=600 + b)
cbo_DienLucTH.current(0) # Đặt giá trị mặc định lựa chọn đầu tiên


# Hàm xử lý sự kiện khi checkbox thay đổi trạng thái
def on_chb_ChoPhep_change():
    chophep = False
    if var_ChoPhep.get():
        chophep = True
# Tạo các biến BooleanVar để giữ trạng thái của checkbox
var_ChoPhep = tk.BooleanVar()
# Tạo các checkbox
checkbox1_ChoPhep = tk.Checkbutton(root, text="Cho phép", variable=var_ChoPhep, command=on_chb_ChoPhep_change)
checkbox1_ChoPhep.place(x=970 + a, y=540 + b)


# Tạo một Label "5. Thiết bị cần cắt"
label = tk.Label(root, text="5. Thiết bị cần cắt", font=("Arial", 11))
label.place(x=1060 + a, y=210 + b)
# Tạo khung (frame) để chứa Text widget và Scrollbar
frame = tk.Frame(root)
frame.place(x=1060 + a, y=240 + b)
# Tạo Text widget
text_widget_ThietBiCanCat = tk.Text(frame, wrap='none', height=10, width=100, font=("Arial", 11))
text_widget_ThietBiCanCat.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Tạo Scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget_ThietBiCanCat.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Kết nối Scrollbar với Text widget
text_widget_ThietBiCanCat.config(yscrollcommand=scrollbar.set)
# Thêm nội dung vào Text widget
for i in range(100):
    text_widget_ThietBiCanCat.insert(tk.END, f"Dòng {i + 1}\n")


# TẠO TEXT WIDGET CHỨA NỘI DUNG "VỊ TRÍ CẦN TIẾP ĐỊA"
label = tk.Label(root, text="5. Vị trí cần tiếp địa", font=("Arial", 11))
label.place(x=1060 + a, y=420 + b)
# Tạo khung (frame) để chứa Text widget và Scrollbar
frame = tk.Frame(root)
frame.place(x=1060 + a, y=450 + b)
# Tạo Text widget
text_widget_ViTriTiepDia = tk.Text(frame, wrap='none', height=10, width=100, font=("Arial", 11))
text_widget_ViTriTiepDia.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Tạo Scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget_ViTriTiepDia.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Kết nối Scrollbar với Text widget
text_widget_ViTriTiepDia.config(yscrollcommand=scrollbar.set)
# Thêm nội dung vào Text widget
for i in range(100):
    text_widget_ViTriTiepDia.insert(tk.END, f"Dòng {i + 1}\n")


# TẠO TEXT WIDGET CHỨA NỘI DUNG "VỊ TRÍ TREO BIỂN BÁO"
label = tk.Label(root, text="5. Vị trí treo biển báo", font=("Arial", 11))
label.place(x=1060 + a, y=630 + b)
# Tạo khung (frame) để chứa Text widget và Scrollbar
frame = tk.Frame(root)
frame.place(x=1060 + a, y=660 + b)
# Tạo Text widget
text_widget_ViTriBienBao = tk.Text(frame, wrap='none', height=10, width=100, font=("Arial", 11))
text_widget_ViTriBienBao.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Tạo Scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget_ViTriBienBao.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Kết nối Scrollbar với Text widget
text_widget_ViTriBienBao.config(yscrollcommand=scrollbar.set)
# Thêm nội dung vào Text widget
for i in range(100):
    text_widget_ViTriBienBao.insert(tk.END, f"Dòng {i + 1}\n")


# TẠO TEXT WIDGET CHỨA NỘI DUNG "NỘI DUNG KHÁC"
label = tk.Label(root, text="5. Lưu ý", font=("Arial", 11))
label.place(x=1060 + a, y=840 + b)
# Tạo khung (frame) để chứa Text widget và Scrollbar
frame = tk.Frame(root)
frame.place(x=1060 + a, y=870 + b)
# Tạo Text widget
text_widget_LuuY = tk.Text(frame, wrap='none', height=5, width=100, font=("Arial", 11))
text_widget_LuuY.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Tạo Scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget_LuuY.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Kết nối Scrollbar với Text widget
text_widget_LuuY.config(yscrollcommand=scrollbar.set)
# Thêm nội dung vào Text widget
for i in range(100):
    text_widget_LuuY.insert(tk.END, f"Dòng {i + 1}\n")



# Tạo LIST CHỨA THÔNG TIN CÁC BIỆN PHÁP AN TOÀN
ThietBiCanCat = []
ViTriTiepDia = []
ViTriTreoBienBao = []


# Tạo Button "Thiết bị cắt"
bt_Open = tk.Button(root, text="Thiết bị cắt",padx=20, pady=5, command=Ultility.on_bt_Open_click)
bt_Open.place(x=200 + a, y=640 + b)

# Tạo Button "Kiểm tra cắt điện"
bt_Open_Check = tk.Button(root, text="Tiếp địa",padx=20, pady=5, command=Ultility.on_bt_Open_click)
bt_Open_Check.place(x=330 + a, y=640 + b)

# Tạo Button "Treo biến báo"
bt_Tiepdia = tk.Button(root, text="Biển báo",padx=20, pady=5, command=Ultility.on_bt_Open_click)
bt_Tiepdia.place(x=440 + a, y=640 + b)







root.mainloop()