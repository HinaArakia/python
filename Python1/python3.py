#課題3
print("身長を入力")
height = (input())
print("体重を入力")
weight =  (input())

weight = float(weight)
height = float(height)

bmi = ((weight / (height * height)))
print("bmiは",bmi)

if bmi < 18.5:
 print("あなたはやせです")
elif 18.5 < bmi and bmi < 25:
 print("あなたは標準です")
elif 25 < bmi and bmi < 30:
 print("あなたは肥満です")
elif  30 < bmi:
 print("あなたは高度肥満です")