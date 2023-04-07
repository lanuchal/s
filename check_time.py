import datetime
import time


while True:
    # เช็คเวลาปัจจุบัน
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"เวลาปัจจุบัน: {current_time}")
    
    # ตรวจสอบเวลา หากถึงเวลา 22.00 น. ให้ break ออกจากลูป
    if current_time >= "09:35:00":
        print("เวลาถึง 22.00 น. จบการทำงาน")
        break
    

