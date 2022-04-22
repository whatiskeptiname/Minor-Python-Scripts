import threading
import time

# Get the start time
start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done Sleeping...")


# Create thread object list
threads = []

# Create multiple threads
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

# Wait for all threads to complete
for thread in threads:
    thread.join()


# Get the end time
finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
