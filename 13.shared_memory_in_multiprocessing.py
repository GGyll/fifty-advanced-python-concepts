from multiprocessing import Process, Value

def increment(shared_value):
    with shared_value.get_lock():  # Synchronize access
        shared_value.value += 1

if __name__ == "__main__":
    shared_value = Value('i', 0)  # Shared integer initialized to 0
    processes = [Process(target=increment, args=(shared_value,)) for _ in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(shared_value.value)  # Output: 5
