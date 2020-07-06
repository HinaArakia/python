#Vihicleクラスにmoveメソッドを定義
class Vihicle:
    def __init__(self, driver, engine, do):
        self.driver = driver
        self.engine = engine
        self.do = do

    def move(self): 
        print( self.driver +  "は" + self.engine + "を" + self.do + "と進みます。")

#子クラスで継承
class Car(Vihicle):
    def move(self):
     super().move()

class Bike(Vihicle):
    def move(self):
     super().move()

class Boat(Vihicle):
    def move(self):
     super().move()

class Airplane(Vihicle):
    def move(self):
     super().move()

car = Car("自動車","アクセル","踏む")
bike = Bike("自転車","ペダル","漕ぐ")
boat = Boat("船","スクリュー","回す")
airplane = Airplane("飛行機","プロペラ","回す")


car.move()
bike.move()
boat.move()
airplane.move()


