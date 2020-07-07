from abc import ABCMeta, abstractclassmethod

#Vihicleクラス(抽象クラス)にmoveメソッドを定義
class Vihicle(metaclass=ABCMeta):
    def __init__(self, driver, engine, do):
        self.driver = driver
        self.engine = engine
        self.do = do

    @abstractclassmethod
    def move(self):
      pass

#子クラスで継承
class Car(Vihicle):
   def move(self):
      print( self.driver + "は" + self.engine + "を" + self.do + "と進みます。" )

class Bike(Vihicle):
    def move(self):
      print( "自動車は" + self.engine + "を" + self.do + "と進みます。" )
    
class Boat(Vihicle):
    def move(self):
      print( self.driver + "は" + self.engine + "を" + self.do + "と進みます。" )
      
class Airplane(Vihicle):
    def move(self):
      print( self.driver + "は" + self.engine + "を" + self.do + "と進みます。" )

car = Car("自動車","アクセル","踏む")
bike = Bike("自転車","ペダル","漕ぐ")
boat = Boat("船","スクリュー","回す")
airplane = Airplane("飛行機","プロペラ","回す")

car.move()
bike.move()
boat.move()
airplane.move()


