import threading 
import time
def print_message(msg, delay):
    time.sleep(delay)
    print(msg)

    
t1=threading.Thread(target=print_message,args=("Thread 1 running",2))
t2=threading.Thread(target=print_message,args=("Thread 2 running",1))


t1.start()
print(threading.current_thread().name)

t2.start()
print(threading.current_thread().name)

t1.join()
print(threading.current_thread().name)

t2.join()


print("Main thread finished")