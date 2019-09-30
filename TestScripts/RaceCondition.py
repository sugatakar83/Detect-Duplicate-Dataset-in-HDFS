import threading

x=0

def incrementGlobal():
    global x
    x += 1

# a thread which will call the incremental function for n times
#def callIncrement(): # without lock
def callIncrement(lock):  # with lock
    for i in range(1000):
        # acquire lock
        lock.acquire()
        incrementGlobal()
        lock.release()

# create the main function which will call two threads
def main():
    global x
    x = 0
    lock = threading.Lock() # assign the lock
    t1 = threading.Thread(target=callIncrement, args=(lock,))
    t2 = threading.Thread(target=callIncrement, args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# execute the funstions with a range
if __name__ == '__main__':
    for i in range(5):
        main()
        print("x = {1} after Iteration {0}".format(i, x))
