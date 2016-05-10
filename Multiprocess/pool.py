import multiprocessing as mp

class Test():
    
    def f1(self):
        for number in range("1"):
            print(number),
    
    def f2(self):
        for number in range(100):
            print("2")

testObj = Test()
def callf1(testObj):
    testObj.f1()
def callf2(testObj):
    testObj.f2()

#freeze.support()
pool = mp.Pool()
pool.apply_async(callf1)
pool.apply_async(callf2)