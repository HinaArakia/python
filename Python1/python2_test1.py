#課題1
speed = (input("速度"))
distance = (input("距離"))

speed = float(speed)
distance = float(distance)

#時間を求める関数
def time(speed,distance):
     result = distance / speed
     return result
print(time(speed,distance))

