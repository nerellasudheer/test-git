# # ==============
# # Exercise 1 :
# import threading
# import time
# lock= threading.Lock()

# class TicketBookingSystem:
#     def __init__(self,total_tickets=10):
#         self.total_tickets=total_tickets
        
#     def book_tickets(self,customer_name,num_tickets):
#         if self.total_tickets> num_tickets:
#             print(f"{customer_name} available tickets: {self.total_tickets}")
#             time.sleep(0.1)
#             print(f"{customer_name} booked the ticket of:{num_tickets}")
#             self.total_tickets-=num_tickets
#             print(f"After {customer_name} booked , availabel tickets are : {self.total_tickets}")
#         else:
#             print(f"No suffecient tickets : {self.total_tickets}")
# person1=TicketBookingSystem()
# person2=TicketBookingSystem()
# person3=TicketBookingSystem()
# person4=TicketBookingSystem()
# person5=TicketBookingSystem()

# t1=threading.Thread(target=person1.book_tickets,args=("Customer A",3))
# t2=threading.Thread(target=person2.book_tickets,args=("Customer B",4))
# t3=threading.Thread(target=person3.book_tickets,args=("Customer C",2))
# t4=threading.Thread(target=person4.book_tickets,args=("Customer D",5))
# t5=threading.Thread(target=person5.book_tickets,args=("Customer E",3))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()


# # ==============
# # Exercise 2 :
import threading
import time
lock= threading.Lock();
