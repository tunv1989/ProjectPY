import tkinter as tk
from tkinter import ttk
import difflib

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

        typed_text = self.get("1.0", "end-1c")
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
        

def on_bt_Open_click():
    messagebox.showinfo("Thông báo", "Nút bấm đã được nhấn!")