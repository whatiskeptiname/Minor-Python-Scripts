from threading import Thread
from time import sleep 

def compute(text):
    for i in range(100):
        print(text)
        return i
        sleep(1)
    
t1= Thread(target= compute, args=("a"))
t2= Thread(target= compute, args=("b"))

t1.start()

