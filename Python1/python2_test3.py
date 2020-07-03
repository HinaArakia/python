from PIL import Image
import math

#課題3
img = Image.open("Python1\orange.jpg")
w, h = img.size
#アスペクト比判定
def aspect(w,h):
    greatest_common_divisor = math.gcd(w,h)
    resulta = w / greatest_common_divisor
    resultb = h / greatest_common_divisor
    return resulta,resultb
print( aspect(w,h))

