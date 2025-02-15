import threading
import time

def cpu_task():
    for _ in range(10**7):
        pass  # Simulates CPU work

threads = [threading.Thread(target=cpu_task) for _ in range(4)]

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Time taken: {time.time() - start}")
