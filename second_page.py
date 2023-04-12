import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณยอดรวมทั้งหมด
def calculate_total():
    try:
        # รับข้อมูลเริ่มต้นเงิน, อัตราดอกเบี้ยต่อวัน, และจำนวนวันที่ต้องการคำนวน
        initial_amount = float(initial_amount_entry.get())
        interest_rate = float(interest_rate_entry.get())
        num_of_days = int(num_of_days_entry.get())

        # คำนวณยอดรวมทั้งหมด
        total_amount = initial_amount * (1 + (interest_rate / 100)) ** num_of_days

        # แสดงผลลัพธ์ในกล่องข้อความผลลัพธ์
        result_label.config(text="ยอดรวมทั้งหมดหลังจาก {} วัน: {:.2f} บาท".format(num_of_days, total_amount))

    except ValueError:
        # แสดงข้อความแจ้งเตือนกรณีป้อนข้อมูลไม่ถูกต้อง
        messagebox.showerror("ผิดพลาด", "กรุณาป้อนข้อมูลให้ถูกต้อง")

# ฟังก์ชันคำนวณดอกเบี้ยต่อวัน
def calculate_interest_rate():
    try:
        # รับข้อมูลเงินเริ่มต้น, จำนวนวัน, และยอดรวมทั้งหมด
        initial_amount = float(initial_amount_entry2.get())
        num_of_days = int(num_of_days_entry2.get())
        total_amount = float(total_amount_entry.get())

        # คำนวณอัตราดอกเบี้ยต่อวัน
        interest_rate = ((total_amount / initial_amount) ** (1 / num_of_days) - 1) * 100

        # แสดงผลลัพธ์ในกล่องข้อความผลลัพธ์
        result_label2.config(text="อัตราดอกเบี้ยต่อวัน: {:.2f} %".format(interest_rate))

    except ValueError:
        # แสดงข้อความแจ้งเตือนกรณีป้อนข้อมูลไม่ถูกต้อง
        messagebox.showerror("ผิดพลาด", "กรุณาป้อนข้อมูลให้ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณยอดรวมและดอกเบี้ยต่อวัน")
root.geometry("400x400")

# ส่วนของการคำนวณยอดรวมทั้งหมด
frame1 = tk.Frame(root)
frame1.pack(pady=10)

initial_amount_label = tk.Label(frame1, text="เงินเริ่มต้น (บาท):")
initial_amount_label.pack(side=tk.LEFT, padx=10)

initial_amount_entry = tk.Entry(frame1)
initial_amount_entry.pack(side=tk.LEFT)

interest_rate_label = tk.Label(frame1, text="อัตราดอกเบี้ยต่อวัน (%):")
interest_rate_label.pack(side=tk.LEFT, padx=10)

interest_rate_entry = tk.Entry(frame1)
interest_rate_entry.pack(side=tk.LEFT)

num_of_days_label = tk.Label(frame1, text="จำนวนวัน:")
num_of_days_label.pack(side=tk.LEFT, padx=10)

num_of_days_entry = tk.Entry(frame1)
num_of_days_entry.pack(side=tk.LEFT)

calculate_total_button = tk.Button(root, text="คำนวณยอดรวมทั้งหมด", command=calculate_total)
calculate_total_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# ส่วนของการคำนวณดอกเบี้ยต่อวัน
frame2 = tk.Frame(root)
frame2.pack(pady=10)

initial_amount_label2 = tk.Label(frame2, text="เงินเริ่มต้น (บาท):")
initial_amount_label2.pack(side=tk.LEFT, padx=10)

initial_amount_entry2 = tk.Entry(frame2)
initial_amount_entry2.pack(side=tk.LEFT)

num_of_days_label2 = tk.Label(frame2, text="จำนวนวัน:")
num_of_days_label2.pack(side=tk.LEFT, padx=10)

num_of_days_entry2 = tk.Entry(frame2)
num_of_days_entry2.pack(side=tk.LEFT)

total_amount_label = tk.Label(frame2, text="ยอดรวมทั้งหมด (บาท):")
total_amount_label.pack(side=tk.LEFT, padx=10)

total_amount_entry = tk.Entry(frame2)
total_amount_entry.pack(side=tk.LEFT)

calculate_interest_rate_button = tk.Button(root, text="คำนวณอัตราดอกเบี้ยต่อวัน", command=calculate_interest_rate)
calculate_interest_rate_button.pack(pady=10)

result_label2 = tk.Label(root, text="")
result_label2.pack()

root.mainloop()

