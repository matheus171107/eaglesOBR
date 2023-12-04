import serial

arduino = serial.Serial('/dev/ttyUSB0', 9600)

if arduino.isOpen():
    print("Conect Sucesseful!!")
    
    while True:
        Read_Serial = arduino.read()
        cmd = int(input("Digite o Comando: "))
        print(Read_Serial)
        if cmd == 1:
            arduino.write(1)
        elif cmd == 0:
            arduino.write(0)
