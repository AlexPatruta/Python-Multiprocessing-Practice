from time import sleep

class ProcessTest():
    """
    Test class created for testing the behaviour of the multiprocessing module
    """
    @staticmethod
    def F1():
        """
        Loop waiting time: 0.05
        """
        print('\nINFO | Calling staticmethod F1')
        for index in range(100):
            sleep(0.05)
            print('F2 | Step: %d' % index)
    #--------------------------------------------------------------------------
    @staticmethod
    def F2():
        """
        Loop waiting time: 0.3
        """
        print('\nINFO | Calling staticmethod F2')
        for index in range(100):
            sleep(0.03)
            print('F1 | Step: %d' % index)
    #--------------------------------------------------------------------------
    @classmethod
    def F3(cls, limit, time=0.3):
        """
        F3(limit[, time])
        classmethod (passes class as the first argument)
        
        Parameters: 
        limit -> integer, set where the range() function will stop
        time -> integer/float, set the sleep time [default: 0.03]
        """
        print('\nINFO | Calling classmethod F3')
        for index in range(limit):
            sleep(time)
            print('F3 | Step: %d' % index)
    #--------------------------------------------------------------------------
    def F4(self, time=2, limit=3):
        """
        F4([time, limit])
        This is a method that passes the object as the first argument

        Parameters:
        time -> int/float Determine the time you want between two steps
                in the 'for' loop that prints the steps
        limit -> int Determine how many steps you want the function to run
                     Note that the step numbers will be multiplied with 
                     the time you wait per loop, giving the total time you
                     will be waiting for this function to run.
        """
        print('\nINFO | Calling method F4')
        for index in range(limit):
            sleep(time)
            print('F4 | Step: %d' % index)
