#課題3
print("身長を入力")
height = (input())
print("体重を入力")
weight = (input())

weight = float(weight)
height = float(height)

bmi = weight / height ** 2

if bmi < 18.5:
 print("あなたは「やせ」です")
elif 18.5 < bmi and bmi < 25:
 print("あなたは「標準」です")
elif 25 < bmi and bmi < 30:
 print("あなたは「肥満」です")
elif 30 < bmi:
 print("あなたは「高度肥満」です")