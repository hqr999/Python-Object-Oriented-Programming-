# Classe TV 

class TV():
    def __init__(self):
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
        if self.isOn:
            print('     TV is: ON')
            print('     Channel is:',self.channelList[self.channelIndex])
            if self.isMuted:
                print('     Volume is:',self.volume,'(sound is muted)')
            else:
                print('     Volume is:',self.volume)
        else:
            print('     TV is: OFF')





# Código principal
oTV = TV() # Cria o objeto TV 
# Liga a TV e mostra o status 
oTV.power()
oTV.showInfo()
# Muda o canal para cima duas vezes, aumenta o volume duas vezes, mostar status
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()
# Desliga a TV, mostra o status, liga a TV, mostra o status
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()
# Diminui o volume, muta o som, mostra o status
oTV.volumeDown()
oTV.mute()
oTV.showInfo()
# Muda o canal para o 11, muta o som, mostra o status
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()
