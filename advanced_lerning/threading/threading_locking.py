import threading
import time
lock= threading.Lock()

amount=1000


def amount_withdraw(person, w_amount):
    global amount
    print(f"{person} is trying to acquire lock")
    with lock:
        print(f"{person} acquired lock")
        if amount>=w_amount:
            
            print(f"{person} your balance is {amount}")
            time.sleep(0.001)
            amount=amount-w_amount
            print(f"{person} withdraed {w_amount} and your {amount}")
        else:
            print(f"{person} insufficient funds!{amount}")
        
        

t1=threading.Thread(target=amount_withdraw,args=("sudheer",600))
t2=threading.Thread(target=amount_withdraw,args=("ram",600))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"End of the transctions {amount}")
