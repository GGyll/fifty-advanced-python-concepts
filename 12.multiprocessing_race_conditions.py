import multiprocessing

def increment(n):
    global counter
    for _ in range(100000):
        n.value += 1

if __name__ == '__main__':
    number = multiprocessing.Value('i', 0)
    p1 = multiprocessing.Process(target=increment, args=(number,))
    p2 = multiprocessing.Process(target=increment, args=(number,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(number.value)  