import asyncio

as_event=asyncio.Event()


async def test_sem(task):
    print(f"{task} task is started")
    await as_event.wait()
    print(f"{task} task is completed ")

async def as_event_test():
    print("Event is initiated")
    await asyncio.sleep(2)
    as_event.set()

async def main():
    t1=asyncio.create_task(test_sem(task="task1"))
    t2=asyncio.create_task(test_sem(task="task2"))
    ev=asyncio.create_task(as_event_test())

    result = await asyncio.gather(t1,t2)

asyncio.run(main())