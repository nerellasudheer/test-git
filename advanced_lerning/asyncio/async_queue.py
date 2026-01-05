import asyncio
queue = asyncio.Queue()

async def supplier():
    for id in range(5):
        await asyncio.sleep(1)
        await queue.put(id)
        print(f"supplier added the item with id :{id}")

async def reciver():
    while True:
        job=await queue.get()
        print(f"Reciver got the item of id {job}")
        await asyncio.sleep(2)
        print(f"Reciver processed the item of id {job}")
        queue.task_done()

async def main():
    producer_task = asyncio.create_task(supplier())
    consumer_task = asyncio.create_task(reciver())

    await producer_task
    await queue.join()     # wait until all jobs are processed
    consumer_task.cancel()

asyncio.run(main())