import tkinter as tk
from tkinter import ttk
import difflib
from tkinter import messagebox

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

# Chương trình tạo ra danh sách từ gợi ý
KeyWord_Path = "config/KeyWord.txt"
word_list = ReadfileTxt(KeyWord_Path)

class AutocompleteEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<KeyRelease>", self.check_input)
        self.bind("<Up>", self.move_up)
        self.bind("<Down>", self.move_down)
        self.bind("<Return>", self.select_suggestion)
        self.listbox = None
        self.listbox_open = False

    def check_input(self, event):
        if event.keysym in ["Up", "Down", "Return"]:
            return

        typed_text = self.get()
        if typed_text:
            matches = self.find_matches(typed_text)
            if matches:
                self.show_listbox(matches)
            else:
                if self.listbox:
                    self.listbox.destroy()
                    self.listbox_open = False
        else:
            if self.listbox:
                self.listbox.destroy()
                self.listbox_open = False

    def find_matches(self, typed_text):
        # Tìm các từ có chứa typed_text ở bất kỳ vị trí nào trong từ
        matches = [word for word in word_list if typed_text.lower() in word.lower()]
        # Sắp xếp các từ dựa trên độ tương đồng
        matches = sorted(matches, key=lambda word: difflib.SequenceMatcher(None, typed_text.lower(), word.lower()).ratio(), reverse=True)
        return matches[:5]

    def show_listbox(self, matches):
        if self.listbox:
            self.listbox.destroy()
        
        self.listbox = tk.Listbox(width=self["width"])
        self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
        self.listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.listbox_open = True

        for match in matches:
            self.listbox.insert(tk.END, match)
        
        self.listbox.selection_set(0)

    def on_listbox_select(self, event):
        if not self.listbox:
            return
        
        selected_word = self.listbox.get(self.listbox.curselection())
        self.delete(0, tk.END)
        self.insert(0, selected_word)
        self.listbox.destroy()
        self.listbox_open = False

    def move_up(self, event):
        if self.listbox_open:
            current_selection = self.listbox.curselection()
            if current_selection:
                index = current_selection[0]
                if index > 0:
                    self.listbox.selection_clear(index)
                    index -= 1
                    self.listbox.selection_set(index)
                    self.listbox.activate(index)

    def move_down(self, event):
        if self.listbox_open:
            current_selection = self.listbox.curselection()
            if current_selection:
                index = current_selection[0]
                if index < self.listbox.size() - 1:
                    self.listbox.selection_clear(index)
                    index += 1
                    self.listbox.selection_set(index)
                    self.listbox.activate(index)

    def select_suggestion(self, event):
        if self.listbox_open:
            current_selection = self.listbox.curselection()
            if current_selection:
                selected_word = self.listbox.get(current_selection)
                self.delete(0, tk.END)
                self.insert(0, selected_word)
                self.listbox.destroy()
                self.listbox_open = False

# Gợi ý kiểu Text
class AutocompleteText(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<KeyRelease>", self.check_input)
        self.bind("<Up>", self.move_up)
        self.bind("<Down>", self.move_down)
        self.bind("<Return>", self.select_suggestion)
        self.listbox = None
        self.listbox_open = False

    def check_input(self, event):
        if event.keysym in ["Up", "Down", "Return"]:
            return

        # Kiểm tra xem có văn bản trong đối tượng Text không
        if not self.compare("end-1c", "==", "1.0"):
            typed_text = self.get("1.0", "end-1c")
            matches = self.find_matches(typed_text)
            if matches:
                self.show_listbox(matches)
            else:
                if self.listbox:
                    self.listbox.destroy()
                    self.listbox_open = False
        else:
            if self.listbox:
                self.listbox.destroy()
                self.listbox_open = False

    def find_matches(self, typed_text):
        # Tìm các từ có chứa typed_text ở bất kỳ vị trí nào trong từ
        matches = [word for word in word_list if typed_text.lower() in word.lower()]
        # Sắp xếp các từ dựa trên độ tương đồng
        matches = sorted(matches, key=lambda word: difflib.SequenceMatcher(None, typed_text.lower(), word.lower()).ratio(), reverse=True)
        return matches[:5]

    def show_listbox(self, matches):
        if self.listbox:
            self.listbox.destroy()
        
        self.listbox = tk.Listbox(width=self["width"])
        self.listbox.place(x=self.winfo_rootx(), y=self.winfo_rooty() + self.winfo_height())
        self.listbox.bind("<ButtonRelease-1>", self.on_listbox_select)
        self.listbox_open = True

        for match in matches:
            self.listbox.insert(tk.END, match)
        
        self.listbox.selection_set(0)

    def on_listbox_select(self, event):
        if not self.listbox:
            return
        
        selected_word = self.listbox.get(self.listbox.curselection())
        self.delete("1.0", tk.END)
        self.insert("1.0", selected_word)
        self.listbox.destroy()
        self.listbox_open = False

    def move_up(self, event):
        if self.listbox_open:
            current_selection = self.listbox.curselection()
            if current_selection:
                index = current_selection[0]
                if index > 0:
                    self.listbox.selection_clear(index)
                    index -= 1
                    self.listbox.selection_set(index)
                    self.listbox.activate(index)

    def move_down(self, event):
        if self.listbox_open:
            current_selection = self.listbox.curselection()
            if current_selection:
                index = current_selection[0]
                if index < self.listbox.size() - 1:
                    self.listbox.selection_clear(index)
                    index += 1
                    self.listbox.selection_set(index)
                    self.listbox.activate(index)

    def select_suggestion(self, event):
        if self.listbox_open:
            current_selection = self.listbox.curselection()
            if current_selection:
                selected_word = self.listbox.get(current_selection)
                self.delete("1.0", tk.END)
                self.insert("1.0", selected_word)
                self.listbox.destroy()
                self.listbox_open = False
            return "break"  # Ngăn chặn Enter chèn dòng mới vào Text widget
        

def save_data_ThietBiCat_to_list(textbox, checkbox_var, combobox1, combobox2, combobox3, data_list):
    try:
        text = textbox.get("1.0", tk.END).strip()  # Lấy dữ liệu từ TextBox và loại bỏ khoảng trắng thừa
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
        else:
            text += ",checkbox=False"

        # Ghép tất cả dữ liệu lại
        combined_data = f"{text},{combo1_text},{combo2_text},{combo3_text}"
        data_list.append(combined_data)  # Lưu dữ liệu vào danh sách
        print(data_list)

        messagebox.showinfo("Thông báo", "Dữ liệu đã được lưu!")
        textbox.delete("1.0", tk.END)  # Xóa nội dung TextBox sau khi lưu
        checkbox_var.set(False)  # Xóa dấu tích của CheckBox

    except ValueError as ve:
        messagebox.showerror("Lỗi", str(ve))
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi không mong muốn: {str(e)}")
        print(e)


def save_data_ViTriTiepDia_to_list(textbox, checkbox_var, combobox1, combobox2, combobox3, data_list):
    try:
        text = textbox.get("1.0", tk.END).strip()  # Lấy dữ liệu từ TextBox và loại bỏ khoảng trắng thừa
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
        else:
            text += ",checkbox=False"

        # Ghép tất cả dữ liệu lại
        combined_data = f"{text},{combo1_text},{combo2_text},{combo3_text}"
        data_list.append(combined_data)  # Lưu dữ liệu vào danh sách
        print(data_list)

        messagebox.showinfo("Thông báo", "Dữ liệu đã được lưu!")
        textbox.delete("1.0", tk.END)  # Xóa nội dung TextBox sau khi lưu
        checkbox_var.set(False)  # Xóa dấu tích của CheckBox

    except ValueError as ve:
        messagebox.showerror("Lỗi", str(ve))
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi không mong muốn: {str(e)}")
        print(e)



def save_data_ViTriTreoBienBao_to_list(textbox, checkbox_var, combobox1, combobox2, combobox3, data_list):
    try:
        text = textbox.get("1.0", tk.END).strip()  # Lấy dữ liệu từ TextBox và loại bỏ khoảng trắng thừa
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
        else:
            text += ",checkbox=False"

        # Ghép tất cả dữ liệu lại
        combined_data = f"{text},{combo1_text},{combo2_text},{combo3_text}"
        data_list.append(combined_data)  # Lưu dữ liệu vào danh sách
        print(data_list)

        messagebox.showinfo("Thông báo", "Dữ liệu đã được lưu!")
        textbox.delete("1.0", tk.END)  # Xóa nội dung TextBox sau khi lưu
        checkbox_var.set(False)  # Xóa dấu tích của CheckBox

    except ValueError as ve:
        messagebox.showerror("Lỗi", str(ve))
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi không mong muốn: {str(e)}")
        print(e)


def save_data_NoiDungLuuY_to_list(textbox, data_list):
    try:
        text = textbox.get("1.0", tk.END).strip()  # Lấy dữ liệu từ TextBox và loại bỏ khoảng trắng thừa
        

        if not text:
            raise ValueError("TextBox không có dữ liệu.")
        

        
        # Ghép tất cả dữ liệu lại
        data_list.append(text)  # Lưu dữ liệu vào danh sách
        print(data_list)

        messagebox.showinfo("Thông báo", "Dữ liệu đã được lưu!")
        textbox.delete("1.0", tk.END)  # Xóa nội dung TextBox sau khi lưu

    except ValueError as ve:
        messagebox.showerror("Lỗi", str(ve))
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi không mong muốn: {str(e)}")
        print(e)


def display_data_in_text_widgets(list1, text1):
    text1.delete("1.0", tk.END)
    
    for item in list1:
        text1.insert(tk.END, "- " + str(item) + "\n")


def update_BPAT_lists(text1, text2, text3, text4, list1, list2, list3, list4):
    # Cập nhật lại danh sách từ các Text widgets
    # Cập nhật lại danh sách từ các Text widgets, loại bỏ các phần tử trắng và ký tự "-" ở đầu mỗi dòng
    list1[:] = [item.lstrip('-').strip() for item in text1.get("1.0", tk.END).strip().split("\n") if item.strip()]
    list2[:] = [item.lstrip('-').strip() for item in text2.get("1.0", tk.END).strip().split("\n") if item.strip()]
    list3[:] = [item.lstrip('-').strip() for item in text3.get("1.0", tk.END).strip().split("\n") if item.strip()]
    list4[:] = [item.lstrip('-').strip() for item in text4.get("1.0", tk.END).strip().split("\n") if item.strip()]

    print("Updated lists:")
    print("List 1:", list1)
    print("List 2:", list2)
    print("List 3:", list3)
    print("List 4:", list4)