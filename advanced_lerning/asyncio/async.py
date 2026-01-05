import time
import asyncio


# # test1:
# async def make_tea():
#     print(f"Start boiling water for tea")
#     await asyncio.sleep(3)
#     print(f"Tea is ready")
    
# async def make_rice():
#     print(f"Start boiling water for rice")
#     await asyncio.sleep(2)
#     print(f"Rice is ready")   

# async def main():
#     start_time=time.time()
#     (start_time)
#     batch_processing = asyncio.gather(make_tea(),make_rice())
#     batch_process=await batch_processing
#     # task1=asyncio.create_task(make_tea())
#     # task2=asyncio.create_task(make_rice())
#     # result1=await task1
#     # result2=await task2
#     end_time=time.time()
#     print(end_time)
#     total_time=end_time-start_time
#     print(total_time)


# asyncio.run(main())

# # ////////////////
# # test2:

# async def fetch_data():
#     print("Data initialization is done")
#     await asyncio.sleep(4)
#     print("Data is fetched after the initialization ")

# async def open_data():
#     print("Data opening is done")
#     await asyncio.sleep(2)
#     print("Data is fetched after opening")
# ## below main coroutines are not created as tasks , so it will run normally .
# # async def main():
# #     await fetch_data()
# #     await open_data()

# ## below main coroutines are created as task, so async will automatically pick another task while one is on wait . 
# ## When Task 1 starts waiting (hits an await), the event loop picks up Task 2 and runs it
# ##If Task 1's wait completes while Task 2 is running, Task 1 doesn't immediately interrupt Task 2
# ##Task 2 continues until it hits its own await or completes
# ##Then the scheduler decides which ready task to run next (could be Task 1, Task 2, or another task)  
# async def main():
#     print("Process started")
#     # task1=asyncio.create_task(fetch_data())
#     # task2=asyncio.create_task(open_data())
#     # await task1
#     # await task2
#     batch_processing = asyncio.gather(fetch_data(),open_data())
#     await batch_processing
#     print("Process ended")


# start_time= time.time()
# print(start_time)
# asyncio.run(main())
# end_time=time.time()
# diff_time= end_time-start_time
# print(diff_time)

##////////////////////////////
## task3 

async def test_data(delay, id):
    print(f"Process started for id : {id}")
    await asyncio.sleep(delay)
    print(f"Process is completed for the id : {id}")

async def main():
    ## await test_data(1,1)
    ## await test_data(2,2)
    ## await test_data(3,3)
    
    # task1 = asyncio.create_task(test_data(1,1))
    # task2 = asyncio.create_task(test_data(3,2))
    # task3 = asyncio.create_task(test_data(2,3))
    # await task1
    # await task2
    # await task3
    batch_tasks= await asyncio.gather(test_data(1,1),test_data(3,2),test_data(2,3))






start_time= time.time()
print(start_time)
asyncio.run(main())
end_time=time.time()
diff_time= end_time-start_time
print(diff_time)