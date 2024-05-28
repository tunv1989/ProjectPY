# String Manapulation
# 1. Len = Độ dài của string
# 2. index = 
# 3. split = 
# 4. replace = 
# 5. slice = Tách các ký tự trong một chuỗi
# 6. lowwer = 
# 7. upper = 
# 8. title = 
# 9. swapcase = 
# 10. capitalize = Viết hoa chữ đầu tiên của chuỗi
# 11. Strip = Cắt những ký tự trống "" trong String
# 12. Lstrip
# 13. Rstrip
# 14. isdigit = Check một string có phải là số hay không ?/ Check chữ cái thì Not isdigit
# 15. find = Trả lại vị trí của 1 ký tự/nhóm ký tự trong chuỗi; nếu ký tự không tồn tại trong chuỗi thì giá trị trả về -1
# 16. index = Trả lại vị trí của 1 ký tự/nhóm ký tự trong chuỗi; nếu ký tự không tồn tại trong chuỗi thì giá trị trả về lỗi
# 17. concatenate = Gộp các string lại với nhau
# 18. count = Đếm số ký tự có trong chuỗi

s = "dunglai"

print(len(s)) # Trả về 7

# Index
for i in range(7):
    print(s[i])

print(s[-1]) # Index -1: Ký tự cuối cùng

s1 = "dunglai lap trinh"

#Split => Tạo ra 01 LIST
print(s1.split())

#Replace
print(s1.replace("l", "x"))

#Slice
print(s1[:10])

#Uper, isuper
print(s1.upper())
print(s1.isupper())

#Lower, islower
print(s1.lower())
print(s1.islower())

# Title
print(s1.title())

#Swapcase
s2 = "DUNGlai Lap trinh"
print(s2.swapcase())

#Capitalize
print(s2.capitalize())

# Strip, Lstrip, Rstrip
s3 = "    DUng Lai       "
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())

# isdigit
print(s3.isdigit())

# Find
print(s3.find("D"))
print(s3.find("K"))

# Index
print(s3.index("D"))
