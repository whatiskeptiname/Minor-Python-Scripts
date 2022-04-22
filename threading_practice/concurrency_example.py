import concurrent.futures
import time


# Get the start time
start = time.perf_counter()

# Define a function to do some work
def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"


# Create a thread executor
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]  # Create a list of seconds to sleep
    # Map returns the result in order they are started
    results = executor.map(do_something, secs)  # Create a list of results

    for result in results:
        print(result)

# Get the end time
finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
