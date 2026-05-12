import threading
import time

# Global shared variables
counter = 0
iterations = 500  # Number of increments per thread
num_threads = 20  # High number of threads to ensure a race condition

# PART 1: Without Synchronization (Forcing a Race Condition)
def increment_unsync():
    global counter
    for _ in range(iterations):
        current_value = counter
        # Force the OS to context-switch between threads at the worst moment
        time.sleep(0.00001) 
        counter = current_value + 1

# PART 2: With Synchronization (Using a Mutex Lock)
lock = threading.Lock()
def increment_sync():
    global counter
    for _ in range(iterations):
        with lock:  # The Mutex ensures mutual exclusion
            counter += 1

def run_experiment(use_lock=False):
    global counter
    counter = 0
    threads = []
    
    target_function = increment_sync if use_lock else increment_unsync
    mode_label = "WITH Lock (Sync)" if use_lock else "WITHOUT Lock (Unsync)"
    
    print(f"--- Running {mode_label} ---")
    
    for i in range(num_threads):
        t = threading.Thread(target=target_function)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    expected = num_threads * iterations
    print(f"Expected Result: {expected}")
    print(f"Actual Result:   {counter}")
    print(f"Difference:      {expected - counter}\n")

if __name__ == "__main__":
    # Experiment 1: Demonstrate the Race Condition
    run_experiment(use_lock=False)
    
    # Experiment 2: Demonstrate the Fix
    run_experiment(use_lock=True)