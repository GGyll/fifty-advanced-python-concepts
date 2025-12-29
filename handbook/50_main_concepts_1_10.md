# Advanced Python Interview Reference

## Concepts 1–10 (Senior-Level)

---

## 1. Arrays (Python `array` module)

This one actually threw me off in a real interview.

Python arrays are **not the same as lists**. Python has a built-in `array` module that lets you create **type-specific arrays**.

You have to specify a **type code** when you create them, which means every element in the array must be the same type.

**Why arrays matter:**

- They are **more memory-efficient** than lists
- They enforce type consistency
- They’re faster when working with large datasets of the same type

**Trade-offs:**

- Can only store one type
- Less flexible than lists
- Not dynamically typed like lists

Use arrays when:

- You care about **memory**
- You’re working with **large numeric data**
- You don’t need list flexibility

**Related Examples**

- [`1.arrays.py`](../1.arrays.py)

---

## 2. Garbage Collection & Circular References

Python manages memory automatically, mostly using **reference counting**.

But it struggles with **circular references**.

Example:

- Object A references Object B
- Object B references Object A
- Even after deleting both, memory might not be freed

This is where Python’s **garbage collector** kicks in to detect and clean cycles.

You can:

- Manually trigger garbage collection
- Use tools like `weakref` (covered later)

This matters when:

- You’re working with complex object graphs
- You’re debugging memory leaks
- You’re building long-running services

**Related Examples**

- [`2.garbage_collection.py`](../2.garbage_collection.py)

---

## 3. Not Returning Dicts & Lists from Functions

This is subtle but important.

In Python, **lists and dictionaries are passed by reference**, not copied.

That means:

- If a function modifies a list or dict, the original object is modified
- You don’t need to return it unless you want to

Example idea:

- Pass a list into a function
- Modify it inside the function
- The caller sees the changes automatically

This shows you understand:

- Python object references
- Mutability
- Memory behavior

**Related Examples**

- [`3.no_return.py`](../3.no_return.py)
- [`no_return_other.py`](../no_return_other.py)

---

## 4. Method Resolution Order (MRO)

MRO defines **the order Python looks for methods and attributes**.

This becomes critical with **multiple inheritance**.

Python uses something called **C3 Linearization**, which:

- Resolves inheritance from left to right
- Ensures a consistent lookup order
- Avoids ambiguity when possible

The classic issue here is the **Diamond Problem**, where:

- Two parent classes inherit from the same base class
- A child class inherits from both parents

Understanding MRO helps prevent:

- Unexpected behavior
- Bugs in complex class hierarchies

**Related Examples**

- [`4.method_resolution_order.py`](../4.method_resolution_order.py)

---

## 5. Walrus Operator (`:=`)

Officially called the **assignment expression**.

It lets you **assign and use a value in the same expression**.

Instead of:

- Assigning a variable
- Then checking it

You can do both at once.

This:

- Reduces boilerplate
- Makes conditionals cleaner
- Shows strong Python fluency

It’s small, but interviewers notice it.

**Related Examples**

- [`5.walrus_operator.py`](../5.walrus_operator.py)

---

## 6. `operator.attrgetter`

This is a **performance-optimized alternative to lambdas** for attribute access.

It’s especially useful when:

- Sorting objects
- Accessing nested attributes dynamically

Example use case:

- Sorting people by `person.address.city`
- Sorting by `person.company.name`

Why it’s powerful:

- Supports **deeply nested attributes**
- Accepts dynamic strings
- Implemented in **C**, so it’s faster than lambdas

Great for:

- Automation systems
- Config-driven logic
- Clean, readable sorting logic

**Related Examples**

- [`6.operator_attrgetter.py`](../6.operator_attrgetter.py)

---

## 7. CPython

When people say “Python”, they usually mean **CPython**.

CPython:

- Is written in C
- Compiles Python code into **bytecode**
- Executes it using the **Python Virtual Machine**

Key points:

- Python code → bytecode → executed by VM
- Huge standard library
- Supports C extensions for performance

Downsides:

- Slower than compiled languages
- Has the **Global Interpreter Lock (GIL)**

Understanding CPython shows you:

- Know Python internals
- Can reason about performance

**Related Examples**

- [`34.python_bytecode.py`](../34.python_bytecode.py)

---

## 8. Global Interpreter Lock (GIL)

The GIL ensures:

> Only **one thread executes Python bytecode at a time**

Why it exists:

- CPython uses **reference counting** for memory
- GIL keeps reference updates thread-safe
- Simplifies memory management

Consequences:

- Multithreading **does not give true parallelism**
- CPU-bound tasks don’t scale with threads
- IO-bound tasks still benefit

Important distinction:

- GIL affects **threads**
- It does NOT affect **multiprocessing**

This is a core senior-level topic.

**Related Examples**

- [`8.global_interpreter_lock.py`](../8.global_interpreter_lock.py)

---

## 9. Concurrency vs Parallelism

These are **not the same thing**.

**Concurrency**

- Managing multiple tasks at once
- Tasks are interleaved
- Often uses context switching

**Parallelism**

- Tasks run at the same time
- Requires multiple cores or processes

Python supports concurrency via:

- Threads
- Async programming
- Multiprocessing (true parallelism)

Key challenges:

- Race conditions
- Non-deterministic bugs
- GIL limitations

**Related Examples**

- [`10.multithreading.py`](../10.multithreading.py)
- [`11.multiprocessing.py`](../11.multiprocessing.py)
- [`50.asyncio.py`](../50.asyncio.py)

---

## 10. Multithreading

Threads:

- Share the same memory
- Are lightweight
- Are good for **IO-bound work**

Because of the GIL:

- Only one thread runs Python bytecode at a time
- Threads take turns holding the GIL

Why threading still matters:

- While one thread waits for IO, another can run
- Great for:

  - Network requests
  - File IO
  - APIs

Best practice:

- Use `ThreadPoolExecutor`
- Don’t manage threads manually

**Related Examples**

- [`10.multithreading.py`](../10.multithreading.py)
- [`12.multiprocessing_locks.py`](../12.multiprocessing_locks.py)
- [`12.multiprocessing_race_conditions.py`](../12.multiprocessing_race_conditions.py)
