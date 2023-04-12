import tkinter as tk
import webbrowser

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("หน้า Login")
root.geometry("800x600")  # กำหนดขนาดหน้าต่างเป็น 800x600 pixels

# สร้าง Frame สำหรับเก็บองค์ประกอบต่างๆ
frame = tk.Frame(root)
frame.pack(pady=100)

# สร้าง Label แสดงข้อความ "ชื่อผู้ใช้งาน"
label_username = tk.Label(frame, text="ชื่อผู้ใช้งาน", font=("Helvetica", 14))
label_username.pack(pady=10)

# สร้าง Entry สำหรับใส่ชื่อผู้ใช้งาน
entry_username = tk.Entry(frame, font=("Helvetica", 14))
entry_username.pack(pady=10)

# สร้าง Label แสดงข้อความ "รหัสผ่าน"
label_password = tk.Label(frame, text="รหัสผ่าน", font=("Helvetica", 14))
label_password.pack(pady=10)

# สร้าง Entry สำหรับใส่รหัสผ่าน
entry_password = tk.Entry(frame, font=("Helvetica", 14), show="*")
entry_password.pack(pady=10)

# ฟังก์ชันสำหรับเข้าสู่ระบบ
def login():
    username = entry_username.get()
    password = entry_password.get()
    print("ชื่อผู้ใช้งาน:", username)
    print("รหัสผ่าน:", password)

# สร้างปุ่ม "เข้าสู่ระบบ"
btn_login = tk.Button(frame, text="เข้าสู่ระบบ", font=("Helvetica", 14), command=login)
btn_login.pack(pady=10)

# ฟังก์ชันสำหรับเปิดลิงก์สมัครสมาชิก
def register():
    webbrowser.open("https://www.google.com")

# สร้าง Label แสดงลิงก์สมัครสมาชิก
label_register = tk.Label(root, text="สมัครสมาชิก", font=("Helvetica", 14), fg="blue", cursor="hand2")
label_register.pack()
label_register.bind("<Button-1>", lambda event: register())  # ผูกเหตุการณ์คลิกของ Label กับฟังก์ชัน register

root.mainloop()
