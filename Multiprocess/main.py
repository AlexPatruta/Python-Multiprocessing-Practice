from process_test import *
import multiprocessing as mp

processTestObject = ProcessTest()

p1 = mp.Process(target=processTestObject.F1)
p2 = mp.Process(target=processTestObject.F2)
p3 = mp.Process(target=processTestObject.F3, args=(10,))
p4 = mp.Process(target=processTestObject.F4)

if __name__ == '__main__':
    print("INFO | Starting main application")
    p1.start()
    p1.join()
    p2.start()
    p3.start()
    p4.start()




