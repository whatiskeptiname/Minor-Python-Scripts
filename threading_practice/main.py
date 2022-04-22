import threading
import time

# Get the start time
start = time.perf_counter()


def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")


# Create threads
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# Start threads
t1.start()
t2.start()

# Wait until threads are done
t1.join()
t2.join()

# Get the end time
finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
