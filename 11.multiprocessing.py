from multiprocessing import Process
import os

def worker(name):
    print(f"Process {name} is running in process ID: {os.getpid()}")

if __name__ == "__main__":
    process1 = Process(target=worker, args=("A",))
    process2 = Process(target=worker, args=("B",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both processes finished")


