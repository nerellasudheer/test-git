import time
import asyncio

async def fetch_data():
    print("Data initialization is began 1")
    await asyncio.sleep(4)
    print("Data is fetched after the initialization- done")

async def open_data(delay):
    print("Data opening is started2")
    await asyncio.sleep(delay)
    print("Data is opened and ready to read - done")


async def delete_data(delay):
    print("Data deletion is started3")
    await asyncio.sleep(delay)
    print("Data is deletion- done")
 
async def main():
    task3=asyncio.create_task(delete_data(2))
    print("initial3") ##3
    print("Process started") #2
    task1=asyncio.create_task(fetch_data())
    print("initial1") ##1
    task2=asyncio.create_task(open_data(2))
    print("initial2") ##2
    await task2
    print("test2")
    await task3
    print("test3")
    await task1
    print("test1")


    print("Process ended")


start_time= time.time()
print(start_time) #1
asyncio.run(main())
end_time=time.time()
diff_time= end_time-start_time
print(diff_time) 