debt = float(250000)
interest_rate = float(0.14)
repayment =  float(30000)
month = 0

while debt > 0:
    month += 1
    #　その月の返済額に年利を月割りした分を上乗せする
    debt = debt*(1 + interest_rate / 12)
    
    if debt > repayment:
        debt -= repayment
        print("{}か月目:返済額:{}円,残り{}円".format(month,repayment,debt))
    else:
        repayment = debt
        debt = 0
    print("{}か月目 : 返済額={}円,返済完了".format(month,repayment)) 