import multiprocessing
import os

def product(num):
    print(f"{os.name} in function process going {os.getpid()}")
    count = 0
    for i in range(1, num + 1):
        count += i
    print(f"finnal result is {count}")

def pro():
    p=multiprocessing.Process(target=product, args=(1000000000,), name="pid1")
    p.start()
    print(f"{p.name} process started {p.pid}")
    print(f"process done {p.pid}")

if __name__ == "__main__":
    print(f"main process id {os.getpid()}")
    for i in range(1,111111):
        print(f'process {i} started')
        pro()
    print("all done !!!")
