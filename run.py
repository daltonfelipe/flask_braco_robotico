from app import app, socket
import RPi.GPIO as GPIO

if __name__ == "__main__":
    try:
        print('Iniciando Servidor!')
        socket.run(app, debug=False,host='0.0.0.0', port=8000)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Servidor encerrado!")
