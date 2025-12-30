from multiprocessing import Process, Queue

def producer(q1):
    for x in [1, 2, 3]:
        print("Producer:", x)
        q1.put(x)
    q1.put(None)

def add_one(q1, q2):
    while True:
        x = q1.get()
        if x is None:
            q2.put(None)
            break
        y = x + 1
        print("Add one:", y)
        q2.put(y)

def multiply(q2):
    while True:
        x = q2.get()
        if x is None:
            break
        print("Multiply:", x * 5)

if __name__ == "__main__":
    q1 = Queue()
    q2 = Queue()

    p1 = Process(target=producer, args=(q1,))
    p2 = Process(target=add_one, args=(q1, q2))
    p3 = Process(target=multiply, args=(q2,))

    # What will be printed (order may vary because processes run in parallel):
    #   Producer: 1
    #   Add one: 2
    #   Multiply: 10
    #   Producer: 2
    #   Add one: 3
    #   Multiply: 15
    #   Producer: 3
    #   Add one: 4
    #   Multiply: 20
    #
    # Notes:
    # - Exact interleaving is NOT guaranteed.
    # - These 9 lines are the expected set of outputs.

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
