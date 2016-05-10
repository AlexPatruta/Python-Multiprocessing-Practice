import multiprocessing as mp
import time
from array import *

class TestFunc():
    def f1(self, string, array, lock=None):
        for number in range(100):
            time.sleep(0.1)
            array[number] = str(number)

def f2(args):
    for number in range(100):
        time.sleep(0.2)
        print("2: " + args + ' Step: ' + str(number))
testObj = TestFunc()
arr = array('u', str(range(100)) )       

p1 = mp.Process(target=testObj.f1,
	              args=('One', arr))
	      
p2 = mp.Process(target=f2,
                 args=('Two', arr))

p1.start()
p2.start()

p1.join()
p2.join()
