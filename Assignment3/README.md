# Process Creation & Inter-Process Communication (IPC)

## Project Overview
This project demonstrates the fundamentals of process management and communication within an Operating System. The application creates a parent-child relationship and establishes a communication bridge to exchange and transform data.

## Features
- **Process Creation**: Uses the Python `multiprocessing` module to spawn a child process.
- **IPC Mechanism**: Implements a **Pipe** for bidirectional communication.
- **Data Transformation**: The parent sends a lowercase string, and the child transforms it to uppercase before returning it.
- **PID Tracking**: Real-time console logging of Process IDs (PIDs) to distinguish between the parent and child execution contexts.

## IPC Mechanism Reflection
For this task, I chose the **`multiprocessing.Pipe()`** mechanism. 

### Why Pipe?
1. **Efficiency**: A Pipe is highly efficient for communication between exactly two processes. Unlike a `Queue`, it doesn't require complex locking mechanisms since it's a simple point-to-point connection.
2. **Duplex Communication**: Python's Pipe is bidirectional (duplex) by default. This made it perfect for the "Send -> Receive -> Respond" flow required by the assignment.
3. **Simplicity**: It mimics the standard Unix pipe concept, providing a clean `send()` and `recv()` interface that clearly demonstrates how data travels across process boundaries.

## result
PS C:\Users\XPS\Downloads\OS_Course_2026\Assignment3> python process_ipc.py
Parent [PID 7620]: Starting application.
Parent [PID 7620]: Sending 'hello from the parent process' to child...
Child  [PID 17508]: Received 'hello from the parent process' from parent.
Child  [PID 17508]: Sending transformed data back...
Parent [PID 7620]: Received 'HELLO FROM THE PARENT PROCESS' from child.
Parent [PID 7620]: Task completed. Exiting.
PS C:\Users\XPS\Downloads\OS_Course_2026\Assignment3>


