# Assignment 4: Threads & Synchronization

## Objective
The goal of this assignment is to demonstrate the concept of a **Race Condition** in a multi-threaded environment and show how to resolve it using synchronization primitives like **Mutex Locks**.

## The Problem: Race Condition
In Part 1, multiple threads try to increment a shared global counter simultaneously without any protection. 

A race condition occurs because the operation `counter += 1` is not atomic. It involves:
1. Reading the value.
2. Adding 1.
3. Writing the value back.

When two threads read the same value at the same time, they both increment that same value and overwrite each other's work, leading to a final result that is significantly lower than expected.

## The Solution: Mutex Lock
In Part 2, I implemented a **`threading.Lock()`**. This ensures **Mutual Exclusion**:
- Only one thread can enter the "critical section" (where the counter is modified) at a time.
- Other threads must wait until the lock is released before they can proceed.
- This guarantees that every increment is correctly recorded.

## Execution Results
As shown in the output below, the unsynchronized execution fails to reach the target, while the synchronized version is 100% accurate.

**Terminal Output:**
- **Expected:** 2000
- **Unsync Actual:** 107 (approximate)
- **Sync Actual:** 2000

## Proof of Execution

before modifications 


PS C:\Users\XPS\Downloads\OS_Course_2026\Assignment4> py thread_sync.py
--- Running WITHOUT Lock (Unsync) ---
Expected Result: 4000000
Actual Result:   4000000
Difference:      0

--- Running WITH Lock (Sync) ---
Expected Result: 4000000
Actual Result:   4000000
Difference:      0



after modifications 

PS C:\Users\XPS\Downloads\OS_Course_2026\Assignment4> py thread_sync.py
--- Running WITHOUT Lock (Unsync) ---
Expected Result: 2000
Actual Result:   107
Difference:      1893

--- Running WITH Lock (Sync) ---
Expected Result: 2000
Actual Result:   2000
Difference:      0

PS C:\Users\XPS\Downloads\OS_Course_2026\Assignment4>