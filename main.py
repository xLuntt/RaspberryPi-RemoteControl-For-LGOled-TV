import bluetooth
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print("Accepted connection from ",address)

while True:
    data = client_sock.recv(1024)
    if not data:
        break
    print("Received: ", data)
    if data == b'on':
        GPIO.output(12, GPIO.HIGH)
    elif data == b'off':
        GPIO.output(12, GPIO.LOW)

client_sock.close()
server_sock.close()
