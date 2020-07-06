class Vihicle:
    def __init__(self, driver, engine, do):
       self.driver = driver
       self.engine = engine
       self.do = do
    def drive(self): 
        print( self.driver +  "は" + self.engine + "を" + self.do + "と進みます。")

class Car(Vihicle):
    pass

class Bike(Vihicle):
    pass

class Boat(Vihicle):
    pass

class Airplane(Vihicle):
    pass

car = Car("自動車","アクセル","踏む")
bike = Bike("自転車","ペダル","漕ぐ")
boat = Boat("船","スクリュー","回す")
airplane = Airplane("飛行機","プロペラ","回す")

car.drive()
bike.drive()
boat.drive()
airplane.drive()


