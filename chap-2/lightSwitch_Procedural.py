# Switch que liga a luza de forma procedural 

def turnOn():
    global switchIsOn 
    # Liga a luz 
    switchIsOn = True



def turnOff():
    global switchIsOn 
    # Desliga a luz 
    switchIsOn = False



# Código principal 
switchIsOn = False 

print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)


