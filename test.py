import Ultility

DonVi_List = Ultility.ReadfileTxt("NhanVien.txt")

Name_List = []
Chucvu_List = []

for ele in DonVi_List:
    Info = ele.split(", ")
    Name_List.append(Info[0])
    Chucvu_List.append(Info[1])

value = "Võ Công Trung"
for i in range(len(Name_List)):
    if Name_List[i] == value:
        print(Chucvu_List[i])