import kk
from urllib import request
from play import play
import time
while(True):
    number = 0
    with request.urlopen('http://192.68.3.176/1.html') as f:
        number = int(f.read())
        print('number ', number)
        if number!=1:
            
            print("1")
            3.dian()
            play()
            time.sleep(1)
            print("2")
            
            
