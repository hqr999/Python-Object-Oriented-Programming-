# Regulador de Intensidade de Luz
class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False 
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1 
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print('Switch is on ?',self.switchIsOn)
        print('Brightness is:',self.brightness)


# Código Principal 
oDimmer = DimmerSwitch()
# Liga o switch, e aumenta a claridade em 5 níveis  
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()
# Diminui a claridade em 2 níveis, depois desliga o switch 
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()
# Liga o switch, e depois aumenta a claridade em 3 níveis
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()
