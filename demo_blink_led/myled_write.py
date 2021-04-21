import serial

import time

serdev = '/dev/ttyACM0'                # use the device name you get from `ls /dev/ttyACM*`

s = serial.Serial(serdev, 9600)

for i in range(10):
    s.write(bytes("/myled3/write 1\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/myled3/write 0\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

s.close()