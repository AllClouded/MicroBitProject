import serial



import serial.tools.list_ports as port_list
ports = list(port_list.comports())
for p in ports:
    print (p)


try:
    port = serial.Serial('/dev/ttyACM0', 115200)

    print("Started")

    while True:
        message = port.readline().decode().strip()
        print(message)
except:
    print("failed")