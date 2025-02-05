# import asyncio

# async def greet():
#     print("Hello!")
#     await asyncio.sleep(1)  # Pause for 1 second
#     print("World!")

# asyncio.run(greet())  # Output: Hello! (pause) World!





# import asyncio

# async def task_1():
#     print("Task 1: Start")
#     await asyncio.sleep(2)
#     print("Task 1: End")

# async def task_2():
#     print("Task 2: Start")
#     await asyncio.sleep(1)
#     print("Task 2: End")

# async def main():
#     # Run tasks concurrently
#     await asyncio.gather(task_1(), task_2())

# asyncio.run(main())




import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        await queue.put(f"Item {i}")
        print(f"Produced Item {i}")

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())


