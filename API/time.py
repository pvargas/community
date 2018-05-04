import time as pt
from threading import Timer

def hello_world():
    Timer(3600, hello_world).start() # called every hour
    print("timey time:", int((pt.time())))

hello_world()

'''

now = int((pt.time()/60)/60)
later = now + 1
print(now,'late', later)


'''