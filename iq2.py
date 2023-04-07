

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

ACTIVES="EURUSD"
duration=1#minute 1 or 5
amount=1
action="call"#put

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time >= "12:00:00":
        print("เวลาถึง {current_time} น. จบการทำงาน")
        break
    
    # สั่งซื้อและเก็บ order id
    print(f"You order {amount}$ / {action}$")
    _, order_id = I_want_money.buy_digital_spot(ACTIVES, amount, action, duration)

    # ตรวจสอบสถานะการซื้อ
    if order_id != "error":
        while True:
            check, win = I_want_money.check_win_digital_v2(order_id)
            if check == True:
                break
        # ตรวจสอบผลตอบแทนเพื่อตัดสินใจซื้อ/ขายต่อไป
        if win < 0:
            print(f"You lost {abs(win)}$")
            amount *= 2.25  # increase amount if lose
            balance = I_want_money.get_balance()
            action = "put" if action == "call" else "call"  # reverse action
            sql = "INSERT INTO `iq_data`.`data` (`order`, `trade`, `money`, `result`, `total` ,`profit`) VALUES (%s, %s, %s, '%s', '%s', '%s')"
            val = (action, ACTIVES,"lost",amount,balance,abs(win))
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            print(f"You won {win}$")
            amount = 1  # reset amount to 100 USD if win
            action = action
            balance = I_want_money.get_balance()
            sql = "INSERT INTO `iq_data`.`data` (`order`, `trade`, `money`, `result`, `total`,`profit`) VALUES (%s, %s, %s, '%s', '%s', '%s')"
            val = (action, ACTIVES,"win",amount,balance,abs(win))
            mycursor.execute(sql, val)
            mydb.commit()
            
    # หยุดการเทรดเมื่อเกิดข้อผิดพลาด
    else:
        print("please try again")
        break
    time.sleep(2)