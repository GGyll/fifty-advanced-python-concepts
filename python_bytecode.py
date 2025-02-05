import dis 

def count_to_ten():
    for i in range(10):
        print(i)

dis.dis(count_to_ten)
