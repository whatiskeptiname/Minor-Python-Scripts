import threading
import time

# Get the start time
start = time.perf_counter()


def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")


# Create thread object list
threads = []

# Create multiple threads
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

# Wait for all threads to complete
for thread in threads:
    thread.join()


# Get the end time
finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
