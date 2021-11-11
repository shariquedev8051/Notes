## Multi Threading

### Types of threading:-

1. Process based multi threading
2. Thread Based Multi Threading

### Ways to create threads in python:-

1. Without class
2. With extending thread class
3. Without extending thread class

### Inbuilt Function:-

1. **current_thread().name** - to get name

2. t = Thread(target = test)

   **t.start()**

3. **active_count()** :- To print active threads

4. **enumerate()** :- To list the thread

​		print(t.name)

5. **isAlive()** :- To check the thread is active or not
6. **join()**:- The main thread will be pause until thread finished
7. **join(5)**:- The child thread paused for 5 sec main thread resume.

### Daemon Threads:-

Which runs in background like garbage collector.

1. **t.isDaemon()**:- To check whether it is daemon or not.
2. **t.setDaemon(True)**:- To set the daemon True or false

### Synchronization:-

have aquire() and release methode

1. Lock
2. Rlock(Reentrant Lock)
3. semaphore

### Inter thread communication:-

Have acquire and release methode

condition = threading.condition()







