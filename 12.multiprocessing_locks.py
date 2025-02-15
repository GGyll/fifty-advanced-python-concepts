
import multiprocessing

def increment(n, lock):
    for _ in range(100000):
        with lock:
            n.value += 1

if __name__ == '__main__':
    number = multiprocessing.Value('i', 0)

    lock = multiprocessing.Lock()
    
    p1 = multiprocessing.Process(target=increment, args=(number, lock))
    p2 = multiprocessing.Process(target=increment, args=(number, lock))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(number.value)