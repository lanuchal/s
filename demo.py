

from iqoptionapi.stable_api import IQ_Option
import logging
import random
import time
import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="203.159.93.65",
  user="anucha",
  password="KAO@anucha425",
  database="iq_data"
)

mycursor = mydb.cursor()

# 
email = "anucha.luerach@cmu.ac.th"
password = "KAO@anucha425"
# 
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
I_want_money=IQ_Option(email,password)
I_want_money.connect()#connect to iqoption

ACTIVES="EURGBP"
duration=1 #minute 1 or 5
amount=1
action="call"#put
percent = 1

mycursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
result = mycursor.fetchone()
mydb.commit()

state_percent = 1

state_percent_old = 3
if result[3] == "lost":
    print(f"start lost {float(result[5])}$ / {action}$")
    state_percent = 0
    amount = float(result[5]) * 2.25
    if result[3] == "lost":
        if result[1] == "call":
            action = "put"
        if result[1] == "put":
            action = "call"
else:
    action=result[1]
    state_percent_old = 0
    balance = I_want_money.get_balance()
    amount = round(balance * 10 / 100)
    print(f"start won {amount}$ / {action}$")

interested_actives = ['EURUSD', 'EURGBP', 'GBPJPY', 'EURJPY']

percent_tatol = 0
tatol_today = 0
base_amount = 0
while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time2 = now.strftime("%Y-%m-%d %H:%M:%S")

    if state_percent == 1:
        balance = I_want_money.get_balance()
        amount = round(balance * percent / 100)
        base_amount = amount
        percent_tatol = round(balance * 10 / 100)
        state_percent = 0
        print(f"ยอดที่มี {balance},ยอดที่เทรดต่อไม้วันนี้ {amount} ,ยอดที่ควรได้วันนี้ {percent_tatol} , ยอดที่ได้ {tatol_today}")
    else:
        balance = I_want_money.get_balance()
        amount = round(balance * percent / 100)
        base_amount = amount
        percent_tatol = round(balance * 10 / 100)
        print(f"ยอดที่มี {balance},ยอดที่เทรดต่อไม้วันนี้ {amount} ,ยอดที่ควรได้วันนี้ {percent_tatol} , ยอดที่ได้ {tatol_today}")

    if current_time >= "12:00:00" or tatol_today > percent_tatol:
        print(f"เวลาถึง {current_time} น. จบการทำงาน -> ยอดที่ควรได้วันนี้ {percent_tatol} , ยอดที่ได้ {tatol_today}")
        break




    profit_table = I_want_money.get_all_profit()

    if profit_table:
        for active, profit in profit_table.items():
            if active in interested_actives:
                turbo_profit = profit.get("turbo", 0)
                if turbo_profit > 0.82:
                    ACTIVES = active
                    break
                
    else:
        print("ไม่สามารถเรียกดูค่าตอบแทนของคู่สกุลเงินได้")

    # สั่งซื้อและเก็บ order id
    print(f"You order {amount}$ / {action} / {ACTIVES}")

    _, order_id = I_want_money.buy_digital_spot(ACTIVES, amount, action, duration)

    # ตรวจสอบสถานะการซื้อ
    if order_id != "error":
        while True:
            check, win = I_want_money.check_win_digital_v2(order_id)
            if check == True:
                break
        # ตรวจสอบผลตอบแทนเพื่อตัดสินใจซื้อ/ขายต่อไป
        if win < 0:
            amount *= 2.25  # increase amount if lose
            balance = I_want_money.get_balance()
            action = "put" if action == "call" else "call"  # reverse action
            sql = "INSERT INTO `iq_data`.`data` (`order`, `trade`, `money`, `result`, `total` ,`profit`,`datetime`) VALUES (%s, %s, %s, '%s', '%s', '%s' ,%s)"
            val = (action, ACTIVES,"lost",amount,balance,abs(win),current_time2)
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"{amount}, You lost {abs(win)}$")
        else:
            if state_percent_old != state_percent:
                state_percent = 0
                state_percent_old = state_percent
                print(f"frist win")
            action = action
            if state_percent == 0:
               tatol_today = tatol_today + abs(win)
               print(f"tatol_today = {tatol_today}")
            balance = I_want_money.get_balance()
            sql = "INSERT INTO `iq_data`.`data` (`order`, `trade`, `money`, `result`, `total`,`profit`,`datetime`) VALUES (%s, %s, %s, '%s', '%s', '%s',%s)"
            val = (action, ACTIVES,"win",amount,balance,abs(win),current_time2)
            mycursor.execute(sql, val)
            mydb.commit()
            amount = base_amount # reset amount to 100 USD if win
            print(f"{amount}, You won {win}$, today result {tatol_today}")
            
    # หยุดการเทรดเมื่อเกิดข้อผิดพลาด
    else:
        print("please try again")
        break
    time.sleep(2)