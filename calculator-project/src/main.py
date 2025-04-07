import tkinter as tk
from tkinter import messagebox

def click_button(value):
    """버튼 클릭 시 호출되는 함수"""
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("오류", "잘못된 수식입니다.")
    else:
        entry.insert(tk.END, value)

# GUI 설정
root = tk.Tk()
root.title("계산기")
root.geometry("400x600")
root.resizable(False, False)

# 결과 표시 창
entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 버튼 레이아웃
buttons = [
    "C", "(", ")", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "=", 
]

# 버튼 생성
row = 1
col = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, font=("Arial", 18), bg="lightblue", command=lambda b=button: click_button(b))
    else:
        btn = tk.Button(root, text=button, font=("Arial", 18), command=lambda b=button: click_button(b))
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# 행과 열 크기 조정
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# GUI 실행
root.mainloop()