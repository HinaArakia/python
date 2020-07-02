debt = float(input("借金を入力"))
interest_rate = float(input("利率を入力"))
repayment =  float(input("返済額を入力"))
month = 0
#借金が返済額より大きい時
while debt > repayment :
    month += 1
    debt = debt*(1+ interest_rate/12) - repayment
    print(str(month)+"ヶ月目: 返済額=",repayment,"円","残り",float(debt),"円")
month += 1
debt = debt*(1+ interest_rate/12)
print(str(month)+"ヶ月目:返済額",float(debt),",返済完了。")