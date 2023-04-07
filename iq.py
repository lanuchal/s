from iqoptionapi.stable_api import IQ_Option

email = "anucha.luerach@cmu.ac.th"
password = "KAO@anucha425"

I_want_money = IQ_Option(email, password)
I_want_money.connect()


interested_actives = ['EURUSD', 'EURGBP', 'GBPJPY', 'EURJPY', 'GBPUSD', 'USDJPY']

profit_table = I_want_money.get_all_profit()

# ตัวแปรสำหรับเก็บชื่อคู่สกุลเงินที่ turbo_profit เกิน 0.82 เป็น string
high_profit_actives = ""


if profit_table:
    print("ค่าตอบแทนของคู่สกุลเงินทั้งหมด:")
    for active, profit in profit_table.items():
        if active in interested_actives:
            turbo_profit = profit.get("turbo", 0)
            if turbo_profit > 0.82:
              high_profit_actives = active
              print(f"{active}: {turbo_profit}%, ative = {high_profit_actives}")
              break
else:
    print("ไม่สามารถเรียกดูค่าตอบแทนของคู่สกุลเงินได้")

