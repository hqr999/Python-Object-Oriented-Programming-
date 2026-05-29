# Switch de Luz orientado a Objeto 

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False 

    def turnOn(self):
        # Liga a luz 
        self.switchIsOn = True

    def turnOff(self):
        # Desliga a luz 
        self.switchIsOn = False 

    def show(self):
        print('O switch de luz está...')
        if self.switchIsOn:
            print('\n Ligado!!!')
        else:
            print('\n Desligado!!!!')


# Código principal 
oLightSwitch = LightSwitch()
# Chama o método 
oLightSwitch.show()   # Cria um LightSwitch objectoLightSwitch.turnOn()
oLightSwitch.turnOn()
oLightSwitch.show()


oLightSwitch2 = LightSwitch()
oLightSwitch2.show()
oLightSwitch2.turnOn()
oLightSwitch2.show()
