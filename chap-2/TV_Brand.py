# Classe TV 

class TV():
    def __init__(self,brand,location):
        self.brand = brand 
        self.location = location 
        self.isOn = False 
        self.isMuted = False 

        # Alguns canais na lista padrão de canais  
        self.channelList = [2,4,5,7,8,11,20,36,44,54,65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0 
        self.VOL_MIN = 0 # constante 
        self.VOL_MAX = 10 # constante 
        self.volume = self.VOL_MAX // 2 


    def power(self):
        self.isOn = not self.isOn # Mudar 

    def volumeUp(self):
        if not self.isOn:
            return 
        if self.isMuted:
            self.isMuted = False # Ajustar o volume enquanto o som está silenciado reativa o som 
        if self.volume < self.VOL_MAX:
            self.volume += 1 
    def volumeDown(self):
        if not self.isOn:
            return 
        if self.isMuted:
            self.isMuted = False # Ajustar o volume enquanto o som está silenciado reativa o som 

        if self.volume > self.VOL_MIN:
            self.volume -= 1
   
    def channelUp(self):
        if not self.isOn:
            return 

        self.channelIndex += 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0 # passar para o primeiro canal  

    
    def channelDown(self):
        if not self.isOn:
            return 

        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1 # passar para o canal superior 
    
    def mute(self):
        if not self.isOn:
            return 

        self.isMuted = not self.isMuted 
    def setChannel(self,newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel) # Se o novo canal não está na lista de canais, não faz nada.


    def showInfo(self):
        print()
        print('TV Status')
        print('Status of TV:',self.brand)
        print('     Location:',self.location)
        if self.isOn:
            print('     TV is: ON')
            print('     Channel is:',self.channelList[self.channelIndex])
            if self.isMuted:
                print('     Volume is:',self.volume,'(sound is muted)')
            else:
                print('     Volume is:',self.volume)
        else:
            print('     TV is: OFF')



# Dois objetos que são instâncias da classe TV
oTV1 = TV('Samsung', 'Family room')
oTV2 = TV('Sony', 'Bedroom')

oTV1.showInfo()
print('=============================')
oTV2.showInfo()
