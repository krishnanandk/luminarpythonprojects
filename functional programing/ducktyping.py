class Swift:
    def start(self):
        print("swift car start method")

    def accelerate(self):
        print("acceleration functionality in swift")

    def brk(self):
        print("swift car break method")


class Innova:
    def start(self):
        print("innova car start method")

    def accelerate(self):
        print("acceleration functionality in innova")

    def brk(self):
        print("innova car break method")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.brk()

sw=Swift()
ino=Innova()
p=Person()
p.drive(sw)
p.drive(ino)