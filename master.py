#using this code you can get your RS485 register value easily via serial port.


import time
import minimalmodbus
import serial
import sys

port = 'COM6'
slave_id = 1

try:
    instrument = minimalmodbus.Instrument(port=port,slaveaddress=slave_id)
    print('Instrument Created')
    instrument.serial.baudrate = 4800
    instrument.serial.bytesize = 8
    instrument.serial.parity = serial.PARITY_NONE
    instrument.serial.stopbits = 1
except:
    print(f"Could not connect to {port}")
    sys.exit(1)

if __name__=='__main__':
    while True:
        try:
            data = instrument.read_register(0)
            print(data)
        except minimalmodbus.NoResponseError:
            print("Request will fail on first poll")

        time.sleep(2)
