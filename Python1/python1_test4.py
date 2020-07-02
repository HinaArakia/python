debt = float(250000)
interest_rate = float(0.14)
repayment =  float(30000)
month = 0
#返済額を下回った時はelseで分岐
while (debt > repayment):
    month += 1
    debt = debt*(1+ interest_rate/12) - repayment
    print(str(month)+"ヶ月目: 返済額=",repayment,"円","残り",float(debt),"円")
else:
    month += 1
    print(str(month)+"ヶ月目:返済額",float(debt),",返済完了。") 