from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time



# Hàm truy cập vào website
def launchBrowser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://ktat.cpc.vn/Hethong/Dangnhap.aspx'
    browser.get(url)
    return browser

# Hàm đọc dữ liệu từ file Account.txt để lấy usernam và passwword
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


try:
    browser = launchBrowser()
    browser.maximize_window()
    print("Truy cập website thành công !")
    
    # Login tài khoản vào Website
    fileAccount_Path = "Account.txt"    # Đường dẫn file tài khoản truy cập
    lines = ReadfileTxt(fileAccount_Path)
    username = browser.find_element(By.ID, "Txtusername").send_keys(lines[0])
    passwword = browser.find_element(By.ID, "Txtpass").send_keys(lines[1])
    login = browser.find_element(By.NAME, "Tcap").click()

    # Truy cập vào Modile "Lập BBKSHT"
    browser.find_element(By.XPATH, '//img[@class="downarrowclass"]').click()
    Elememts_List = browser.find_elements(By.XPATH, '//li')
    for Element_LapBBKS in Elememts_List:
        if Element_LapBBKS.text == "LẬP BIÊN BẢN KHẢO SÁT":
            break
    Element_LapBBKS.click()

    # Truy cập vào Button "Tạo mới BBKSHT"
    browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_cmdThemPhieu").click()

    input("Nhấn Enter để tắt trình duyệt")
except Exception as e:
    print(f"An error occurred: {e}")