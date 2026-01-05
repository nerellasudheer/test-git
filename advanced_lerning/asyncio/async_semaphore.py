import asyncio
sem = asyncio.Semaphore(2)

async def test_sem(task):
    async with sem:
        print(f"{task} task is started")
        await asyncio.sleep(2)
        print(f"{task} task is completed ")
async def main():
    t1=asyncio.create_task(test_sem(task="task1"))
    t2=asyncio.create_task(test_sem(task="task2"))
    t3=asyncio.create_task(test_sem(task="task3"))
    t4=asyncio.create_task(test_sem(task="task4"))
    result = await asyncio.gather(t1,t2,t3,t4)
asyncio.run(main())
