from iqoptionapi.stable_api import IQ_Option
import mysql.connector
import time


# email = "anucha.luerach@cmu.ac.th"
# password = "KAO@anucha425"

# I_want_money = IQ_Option(email, password)
# I_want_money.connect()


interested_actives = ['EURUSD', 'EURGBP', 'GBPJPY', 'EURJPY', 'GBPUSD', 'USDJPY']

mydb = mysql.connector.connect(
  host="203.159.93.65",
  user="anucha",
  password="KAO@anucha425",
  database="iq_data"
)

mycursor = mydb.cursor()


action="call"#put



# แสดงผลลัพธ์
# print(result[3])

while True:
  # ทำการส่งคำสั่ง SQL และประมวลผล
  mycursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
  result = mycursor.fetchone()
  mydb.commit()
  if result[3] == "lost":
    if result[3] == "lost":
      if result[1] == "call":
        action = "put"
      if result[1] == "put":
        action = "call"
    print(f"{result[1]}: {action} / {result[3]}, ative = {result[4]}, id = {result[0]}")
  else:
    action=result[1]
    print(f"{result[1]}: {action} / {result[3]}, ative = {result[4]}, id = {result[0]}")

  time.sleep(10)


# profit_table = I_want_money.get_all_profit()

# # ตัวแปรสำหรับเก็บชื่อคู่สกุลเงินที่ turbo_profit เกิน 0.82 เป็น string
# high_profit_actives = ""


# if profit_table:
#     print("ค่าตอบแทนของคู่สกุลเงินทั้งหมด:")
#     for active, profit in profit_table.items():
#         if active in interested_actives:
#             turbo_profit = profit.get("turbo", 0)
#             if turbo_profit > 0.82:
#               high_profit_actives = active
#               print(f"{active}: {turbo_profit}%, ative = {high_profit_actives}")
#               break
# else:
#     print("ไม่สามารถเรียกดูค่าตอบแทนของคู่สกุลเงินได้")

