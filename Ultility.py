

# Hàm đọc dữ liệu từ file txxt lưu lại trong List
def ReadfileTxt(fileAccount_Path):
    lines = []
    try:
        with open(fileAccount_Path, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"The file {fileAccount_Path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines