from app import socket
from app.utils.servo import ServoPWM, Led

base = ServoPWM(18)
height = ServoPWM(12)
garra = ServoPWM(13)
frente = ServoPWM(19)
led = Led(26)

@socket.on('change-base-value-x')
def message_base(value):
    #print("x: ",value)
    base.set_angle(float(value))


@socket.on('change-base-value-y')
def message_height(value):
    #print("y: ",value)
    height.set_angle(float(value))


@socket.on('change-garra-value')
def message_garra(value):
    garra.set_angle(float(value))
    if (int(value) == 90):
        led.on()
        print("garra: aberta")
    elif (int(value) == 20):
        led.off()
        print("garra: fechada")




@socket.on('change-frente-value')
def message_frente(value):
    print("frente: ",value)
    frente.set_angle(float(value))
   
