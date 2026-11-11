import threading

for thread in threading.enumerate():
    print(f"仍在运行的线程: {thread.name}, 是否为守护线程: {thread.daemon}")
