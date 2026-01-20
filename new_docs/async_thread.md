# Python Concurrency - Complete Guide

> Async, Threading, Multiprocessing, and Queues Explained Simply

---

## Table of Contents

1. [The Big Idea](#1-the-big-idea)
2. [Mental Model - The Restaurant Analogy](#2-mental-model---the-restaurant-analogy)
3. [Async (Asynchronous)](#3-async-asynchronous)
4. [Coroutines](#4-coroutines)
5. [Concurrency vs Parallelism](#5-concurrency-vs-parallelism)
6. [Threading](#6-threading)
7. [Process & Multiprocessing](#7-process--multiprocessing)
8. [Queues](#8-queues)
9. [Comparison Table](#9-comparison-table)
10. [When to Use What](#10-when-to-use-what)
11. [Related Important Concepts](#11-related-important-concepts)
12. [Timeline Diagrams](#12-timeline-diagrams)
13. [Coroutine vs Event Loop](#13-coroutine-vs-event-loop)
14. [asyncio.TaskGroup](#14-asynciotaskgroup)
15. [asyncio.Future](#15-asynciofuture)
16. [asyncio.Lock](#16-asynciolock)
17. [asyncio.Semaphore & Event](#17-asynciosemaphore--event)
18. [Remaining asyncio Concepts](#18-remaining-asyncio-concepts)
19. [Learning Roadmap](#19-learning-roadmap)

---

## 1. The Big Idea

Before any terms, understand this:

> **A program is just work that needs to be done.**

Different techniques exist to:
- Do **more work**
- Do work **faster**
- Do work **without waiting**

All the confusing words exist only to answer **one question**:

> **How do we handle multiple things happening?**

---

## 2. Mental Model - The Restaurant Analogy

Think of **a restaurant**:

| Concept | Real-life Meaning |
|---------|-------------------|
| Program | The restaurant |
| CPU | The cook |
| Task | One dish |
| Thread | Extra hands of the same cook |
| Process | Another cook |
| Async | One cook switching smartly |
| Queue | Order line |

**Keep this image in mind throughout.**

---

## 3. Async (Asynchronous)

### What async really means

> **Async = Don't wait doing nothing**

### Real-life example

You:
- Put tea water on stove
- While waiting, you wash dishes
- When tea finishes, you switch back

You are **one person**, but **never idle**. That's async.

### Async does NOT mean

| Wrong | Correct |
|-------|---------|
| Multiple CPUs | Smart waiting |
| Multiple people | Single worker, smart switching |
| Faster CPU | Efficient time usage |

---

## 4. Coroutines

### What is a coroutine?

> A **coroutine** is a task that can **pause** and **resume later**.

Real-life: "I'll wait for the kettle - call me when ready."

### Python example

```python
async def boil_water():
    await asyncio.sleep(3)
```

This function:
- Can pause
- Can continue later

### Subroutine vs Coroutine

| Subroutine (normal function) | Coroutine |
|-----------------------------|-----------|
| `time.sleep(3)` | `await asyncio.sleep(3)` |
| Blocks everything | Pauses without blocking |
| Cannot pause nicely | Lets others run |

---

## 5. Concurrency vs Parallelism

### Concurrency

> Handling many things **by switching**

One cook, many dishes. **Async gives concurrency.**

### Parallelism

> Doing many things **at the same time**

Many cooks, many dishes. **Threads & processes give parallelism.**

| Aspect | Concurrency | Parallelism |
|--------|-------------|-------------|
| Workers | 1 | Many |
| How | Switching | Simultaneous |
| Example | Async | Multiprocessing |

---

## 6. Threading

### What is threading?

> **Thread = Extra hands of the SAME worker**

Real-life:
- One cook
- Two hands
- Chopping & stirring

Same memory, same kitchen.

### Python example

```python
import threading

def tea():
    print("Making tea")

t = threading.Thread(target=tea)
t.start()
```

### Python GIL (Global Interpreter Lock)

Python allows only **one thread to think at a time**.

So:
- Threading is **not great for heavy math**
- But good for **waiting tasks** (I/O)

### Pros and Cons

| Pros | Cons |
|------|------|
| Easy to understand | GIL limits CPU usage |
| Shared memory | Hard to debug |
| Good for I/O tasks | Race conditions |

---

## 7. Process & Multiprocessing

### What is a process?

> **Process = A completely separate worker**

Real-life:
- Two cooks
- Two kitchens
- No shared memory

### Python example

```python
from multiprocessing import Process

def cook():
    print("Cooking")

p = Process(target=cook)
p.start()
```

### What is multiprocessing?

> Using **many processes together**

Real-life: Restaurant hires multiple cooks.

### Pros and Cons

| Pros | Cons |
|------|------|
| True parallelism | More memory |
| Uses multiple CPU cores | Slower to start |
| No GIL problem | Communication is hard |

### When to use multiprocessing?

- Heavy calculations
- Image processing
- Machine learning

---

## 8. Queues

### What is a queue?

> **Queue = Line of work**

Real-life:
- Customers waiting in line
- First come, first served

### Python example

```python
from queue import Queue

q = Queue()
q.put("Make tea")
task = q.get()
```

### Why queues matter?

Queues:
- Avoid chaos
- Share work safely
- Prevent data corruption

### Types of queues

| Queue Type | Used With |
|------------|-----------|
| `queue.Queue` | Threads |
| `multiprocessing.Queue` | Processes |
| `asyncio.Queue` | Async |

---

## 9. Comparison Table

| Concept | Workers | Best for | Real-life |
|---------|---------|----------|-----------|
| Async | 1 | Waiting tasks | One smart cook |
| Threading | 1 CPU | Light parallel | Extra hands |
| Process | Many CPUs | Heavy work | Many cooks |
| Multiprocessing | Many CPUs | CPU-heavy | Restaurant |
| Queue | Organizer | Task control | Order line |

---

## 10. When to Use What

### Golden Rules

| Use Case | Best Tool |
|----------|-----------|
| APIs, web, network | Async |
| I/O tasks (file, DB) | Threading |
| CPU heavy work | Multiprocessing |
| Sharing tasks safely | Queue |

### One-Sentence Memory Trick

- **Async** = Smart waiting
- **Thread** = Same brain, more hands
- **Process** = New brain
- **Queue** = Task line

---

## 11. Related Important Concepts

### Blocking vs Non-Blocking

#### Blocking

> You start something and **everything waits** until it finishes.

```python
time.sleep(3)  # blocks everything
```

#### Non-Blocking

> You start something and **do other work while waiting**

```python
await asyncio.sleep(3)  # non-blocking
```

**Async only works because of non-blocking behavior.**

---

### I/O-Bound vs CPU-Bound

This decides **what tool to use**.

| Type | Examples | Best Tools |
|------|----------|------------|
| **I/O-Bound** (waiting) | Network, File, API, Database | async, threading |
| **CPU-Bound** (thinking) | Math, Image processing, ML | multiprocessing |

---

### Event Loop

> The **event loop** is the manager that decides: "Who runs now? Who waits?"

Real-life: A manager switching between workers.

You don't see it much, but **async cannot work without it**.

---

### Deadlock

> Everyone is waiting on everyone else - nothing moves.

Real-life: Two people blocking a door waiting for the other to move.

Happens mostly with:
- Threads
- Locks
- Shared resources

---

### Race Condition

> Two workers try to change the same thing at the same time.

Real-life: Two people editing the same document.

Solved using:
- Locks
- Queues

---

## 12. Timeline Diagrams

### Normal (Blocking) Program

```
Time ─────────────────────────▶

Task A: ██████████████ DONE
Task B:               ██████████████ DONE

Total Time = A + B
```

One thing after another. Wasteful waiting.

---

### Async (Concurrency)

```
Time ─────────────────────────▶

Task A: ████ WAIT ████ DONE
Task B:     ███ WAIT ███ DONE

Total Time = max(A, B)
```

One worker, smart switching, no idle time.

---

### Threading (Shared Memory)

```
CPU ─────────────────────────▶

Thread 1: ██████ DONE
Thread 2: ██████ DONE
(shared brain)
```

Same memory, can conflict, limited by GIL.

---

### Process (True Parallelism)

```
CPU Core 1: ██████ DONE
CPU Core 2: ██████ DONE

(separate brains)
```

True parallel work, heavy but powerful.

---

### Multiprocessing

```
CPU Core 1: ██████
CPU Core 2: ██████
CPU Core 3: ██████
CPU Core 4: ██████
```

Many processes, maximum CPU usage.

---

### Queue (Task Organizer)

```
[Task 1] → [Task 2] → [Task 3] → [Task 4]
           ↑
        Worker takes next
```

Order, safety, no chaos.

---

### Lock

```
Resource
Thread A → uses → releases
Thread B → waits → uses
```

Prevents race conditions and data corruption.

---

## 13. Coroutine vs Event Loop

### The Relationship

Async programming has **two main parts**:

| Part | Role |
|------|------|
| **Coroutine** | The work (a job that can pause and resume) |
| **Event Loop** | The manager (decides which job runs now) |

### Kitchen Analogy

#### Coroutine = A Recipe Step

Each recipe step (boil water, chop vegetables, wait for rice):
- Can be **paused**
- Can be **resumed later**

> "I'm boiling water - call me when it's ready."

#### Event Loop = The Cook's Brain

The cook's brain:
- Watches all pots
- Decides what to do next
- Switches tasks when something is waiting

> "Rice is boiling → I'll chop vegetables."

### Key Insight

> **Coroutines don't run themselves. The event loop runs them.**

### Python Examples

#### Coroutine in Python

```python
async def make_tea():
    await asyncio.sleep(3)
    print("Tea ready")
```

This function can pause, can resume, but does NOTHING by itself.

#### Event Loop in Python

```python
asyncio.run(make_tea())
```

This:
- Creates the event loop
- Runs the coroutine
- Manages pausing and resuming

### Common Beginner Mistake

```python
make_tea()  # WRONG - does NOT run the coroutine
```

You need:

```python
await make_tea()
# or
asyncio.run(make_tea())
```

### Side-by-Side Comparison

| Aspect | Coroutine | Event Loop |
|--------|-----------|------------|
| What it is | A task | A manager |
| Role | Does work | Schedules work |
| Can pause? | Yes | No |
| Can resume tasks? | No | Yes |
| Runs by itself? | No | Yes |
| Created by | `async def` | `asyncio.run()` |
| Count | Many | One (usually) |

### Important Rule

> **You can have many coroutines, but only one event loop running them (per thread).**

### One-Sentence Summary

> **Coroutine = What to do**
> **Event Loop = When to do it**

---

## 14. asyncio.TaskGroup

### What is TaskGroup?

**`TaskGroup` is a structured way to run multiple async tasks together.**

Think of it as:

> "Run these tasks as a group, and manage them safely."

Added in **Python 3.11**.

### Why TaskGroup exists

With `asyncio.gather`:
- If **one task fails**, behavior can be confusing
- You must remember special options (`return_exceptions=True`)
- Tasks may keep running even after failure

**TaskGroup solves this by default.**

### Mental Model

Think of a **TaskGroup like a school project team**:
- All students (tasks) start together
- If **one student fails badly**, the teacher:
  - Stops the whole group
  - Reports the error clearly
- When the group finishes, everything is cleaned up

### Basic Example

```python
import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 done")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())

asyncio.run(main())
```

**What happens:**
1. TaskGroup starts
2. Both tasks start together
3. Task 2 finishes first
4. Task 1 finishes later
5. TaskGroup exits **only after all tasks finish**

### Error Handling

```python
async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(good_task())
            tg.create_task(bad_task())
    except* ValueError as e:
        print("Handled ValueError:", e)

asyncio.run(main())
```

**Key point:** `except*` is used for **multiple errors** (ExceptionGroup).

### TaskGroup vs gather

| Feature | gather | TaskGroup |
|---------|--------|-----------|
| Python version | 3.7+ | **3.11+** |
| Error handling | Manual | **Automatic & safe** |
| Cancel other tasks on error | Optional | **Always** |
| Structured cleanup | No | **Yes** |

### When to use TaskGroup?

| Use TaskGroup | Use gather |
|---------------|------------|
| Python 3.11+ | Older Python versions |
| Safe batch execution | Partial success needed |
| Failure should stop all | Independent tasks |

---

## 15. asyncio.Future

### What is a Future?

A **Future** is an object that represents a **result that will be available later**.

> **"A promise that something will finish in the future."**

### Real-life Analogy

Ordering food at a restaurant:
- You get a **token number**
- Food is **not ready yet**
- Later, you use the token to get your food

That token is like a **Future**.

### What a Future does

A Future:
- Starts **empty**
- Later gets a **result** or an **error**
- Other code can **wait** for it using `await`

### Basic Example

```python
import asyncio

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # set the result later
    loop.call_later(1, future.set_result, "Done!")

    result = await future
    print(result)

asyncio.run(main())
```

### Future vs Task

| Future | Task |
|--------|------|
| Holds a result | Runs a coroutine |
| Low-level | High-level |
| Usually internal | What you usually use |
| Doesn't run code | Executes async code |

**Task = coroutine + Future combined**

### Important Rule

You **rarely create Futures yourself**. Most of the time, Tasks, async functions, and asyncio APIs create and manage Futures for you.

---

## 16. asyncio.Lock

### Why do we need Lock?

When using `asyncio`, **many tasks run concurrently**. If **multiple tasks try to change the same data**, problems happen (race condition).

### What is asyncio.Lock?

> **`asyncio.Lock` allows only ONE task to enter a critical section at a time.**

Think of it as:

> **A bathroom key** - Only the task holding the key can enter. Others must wait.

### Mental Model

- Lock is **free** → task can enter
- Lock is **taken** → other tasks must wait
- Task finishes → lock is released → next task enters

### Full Example

```python
import asyncio

lock = asyncio.Lock()
counter = 0

async def increase_counter(name):
    global counter
    print(f"{name} waiting for lock")

    async with lock:
        print(f"{name} acquired lock")
        temp = counter
        await asyncio.sleep(1)   # simulate work
        counter = temp + 1
        print(f"{name} updated counter to {counter}")

    print(f"{name} released lock")

async def main():
    await asyncio.gather(
        increase_counter("Task 1"),
        increase_counter("Task 2"),
        increase_counter("Task 3"),
    )

asyncio.run(main())
```

### Output

```
Task 1 waiting for lock
Task 1 acquired lock
Task 2 waiting for lock
Task 3 waiting for lock
Task 1 updated counter to 1
Task 1 released lock
Task 2 acquired lock
Task 2 updated counter to 2
Task 2 released lock
Task 3 acquired lock
Task 3 updated counter to 3
Task 3 released lock
```

### Without a Lock

All tasks would:
- Read `counter = 0`
- Sleep
- Write back `counter = 1`

Final result might be **1 instead of 3**. This is a **race condition**.

### When to Use Lock

| Use Lock | Don't Use Lock |
|----------|----------------|
| Multiple tasks modify shared data | Tasks are independent |
| Tasks access shared files | No shared state exists |
| Tasks update shared memory | |

### asyncio.Lock vs threading.Lock

| asyncio.Lock | threading.Lock |
|--------------|----------------|
| For async code | For threads |
| Uses `await` | Blocks thread |
| Non-blocking | Blocking |

---

## 17. asyncio.Semaphore & Event

### Semaphore

#### What is it?

> **`asyncio.Semaphore` allows a limited number of tasks to run at the same time.**

Think of it as:

> **Limited entry tickets** - If there are 3 tickets, only 3 tasks can enter at once.

#### When to use?

- Limit concurrency
- API rate limits
- Database connections
- Network connections

#### Example

```python
import asyncio

sem = asyncio.Semaphore(2)

async def worker(name):
    async with sem:
        print(f"{name} started")
        await asyncio.sleep(2)
        print(f"{name} finished")

async def main():
    await asyncio.gather(
        worker("Task 1"),
        worker("Task 2"),
        worker("Task 3"),
        worker("Task 4"),
    )

asyncio.run(main())
```

Only **2 tasks** run at once. Others wait until a slot is free.

#### Semaphore vs Lock

| Lock | Semaphore |
|------|-----------|
| Only 1 task allowed | Multiple tasks allowed |
| Binary (locked/unlocked) | Counter-based |
| Protect shared data | Limit concurrency |

---

### Event

#### What is it?

> **`asyncio.Event` is a signal used to notify tasks that something has happened.**

Think of it as:

> **Traffic signal** - Red = wait, Green = go

#### What Event does

- Tasks **wait** for an event
- Another task **sets** the event
- All waiting tasks **resume at once**

#### Example

```python
import asyncio

event = asyncio.Event()

async def waiter(name):
    print(f"{name} waiting for event")
    await event.wait()
    print(f"{name} received event")

async def setter():
    await asyncio.sleep(2)
    print("Event set!")
    event.set()

async def main():
    await asyncio.gather(
        waiter("Task 1"),
        waiter("Task 2"),
        setter(),
    )

asyncio.run(main())
```

#### Output

```
Task 1 waiting for event
Task 2 waiting for event
Event set!
Task 1 received event
Task 2 received event
```

#### Event Methods

| Method | Description |
|--------|-------------|
| `event.set()` | Signal the event (wake up waiters) |
| `event.wait()` | Wait for the event |
| `event.clear()` | Reset the event |
| `event.is_set()` | Check if event is set |

#### Semaphore vs Event

| Semaphore | Event |
|-----------|-------|
| Limits number of tasks | Signals tasks |
| Controls access | Controls timing |
| Tasks enter one by one | Tasks resume together |
| Used for rate limiting | Used for coordination |

---

## 18. Remaining asyncio Concepts

### asyncio.Queue

#### What it is

An **async-safe queue** to pass data between tasks.

> **Producer puts items, Consumer takes items**

#### Why you need it

- Safest way to share data between tasks
- Avoids locks
- Very common in real apps

#### Example

```python
import asyncio

queue = asyncio.Queue()

async def producer():
    for i in range(3):
        await queue.put(i)
        print(f"Produced {i}")
        await asyncio.sleep(1)

async def consumer():
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    await asyncio.gather(producer(), consumer())

asyncio.run(main())
```

---

### Cancellation

#### What is it?

Stopping a running task safely.

#### Example

```python
async def task():
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("Task was cancelled")

t = asyncio.create_task(task())
await asyncio.sleep(1)
t.cancel()
```

**Rule:** Always clean up resources in `except CancelledError`.

---

### Timeouts (`asyncio.wait_for`)

#### What it does

Stops waiting if a task takes too long.

#### Example

```python
try:
    await asyncio.wait_for(asyncio.sleep(5), timeout=2)
except asyncio.TimeoutError:
    print("Timeout!")
```

---

### create_task vs await

| `await` | `create_task` |
|---------|---------------|
| Waits immediately | Runs in background |
| Blocks current task | Allows concurrency |
| Simpler | More control |

```python
asyncio.create_task(task())  # background
await task()                 # wait now
```

---

### Shielding tasks (`asyncio.shield`)

Protects a task from cancellation.

```python
task = asyncio.create_task(long_task())
await asyncio.shield(task)
```

Used rarely, but useful in cleanup.

---

### Context managers (`async with`)

Used with:
- Locks
- Semaphores
- TaskGroup
- Streams

Always prefer:

```python
async with lock:
    # protected code
```

over manual acquire/release.

---

### When NOT to use asyncio

| Don't Use For | Use Instead |
|---------------|-------------|
| CPU-heavy work | multiprocessing |
| Blocking functions (`time.sleep`) | threading |
| Non-async libraries | threading |

---

## 19. Learning Roadmap

### Recommended Order

1. Blocking vs Non-blocking
2. I/O-bound vs CPU-bound
3. Async + await (only basics)
4. Threading (with queue)
5. Multiprocessing (concept only)

**Skip advanced locks & deadlocks for now.**

### Mental Map

```
Event Loop
 ├── Tasks
 │    ├── Coroutines
 │    ├── Futures
 │
 ├── Synchronization
 │    ├── Lock
 │    ├── Semaphore
 │    ├── Event
 │    ├── Queue
 │
 └── Control
      ├── Timeout
      ├── Cancellation
      ├── TaskGroup
```

### Final Summary

| Concept | Purpose |
|---------|---------|
| `async/await` | Non-blocking code |
| `Task` | Running coroutine |
| `TaskGroup` | Safe batch execution |
| `Lock` | Protect shared data |
| `Semaphore` | Limit concurrency |
| `Event` | Signal tasks |
| `Queue` | Pass data safely |
| Timeouts & cancellation | Control execution |

**You now cover ~90% of asyncio fundamentals.**

---
