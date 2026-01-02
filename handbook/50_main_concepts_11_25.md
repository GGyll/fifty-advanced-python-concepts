# Advanced Python Interview Reference

## Concepts 11–25 (Senior-Level)

---

## 11. Multiprocessing

Multiprocessing is how you get **true parallelism** in Python.

Instead of threads, you create **separate processes**, and each process has:

- Its own Python interpreter
- Its own memory space
- Its own GIL

This allows Python to:

- Use multiple CPU cores
- Run tasks truly at the same time

**Best for:**

- CPU-bound tasks
- Heavy computation
- Image processing, ML workloads, numerical work

**Trade-offs:**

- Higher overhead than threads
- More complex data sharing
- Slower startup time

**Related Examples**

- [`11.multiprocessing.py`](../11.multiprocessing.py)

---

## 12. Race Conditions (Multiprocessing & Multithreading)

A race condition happens when:

- Multiple threads or processes
- Access shared data
- At the same time
- And the final result depends on execution order

Example idea:

- Two workers increment the same variable
- Final value changes every run

This leads to:

- Non-deterministic behavior
- Extremely hard-to-debug bugs

**How to fix it:**

- Locks
- Semaphores
- Synchronization primitives

Race conditions are one of the most common causes of production bugs.

**Related Examples**

- [`12.multiprocessing_race_conditions.py`](../12.multiprocessing_race_conditions.py)
- [`12.multiprocessing_locks.py`](../12.multiprocessing_locks.py)

---

## 13. Shared Memory in Multiprocessing

By default, processes **do not share memory**.

But sometimes you need them to.

Python provides:

- `multiprocessing.Value`
- `multiprocessing.Array`

These allow:

- Shared state across processes
- Safe updates using locks

Important detail:

- Shared memory must be **explicit**
- Always use synchronization to avoid corruption

This shows you understand **process isolation** and performance trade-offs.

**Related Examples**

- [`13.shared_memory_in_multiprocessing.py`](../13.shared_memory_in_multiprocessing.py)

---

## 14. `collections` Module

The `collections` module provides **specialized data structures** optimized for common patterns.

Some highlights:

- `defaultdict`
- `OrderedDict`
- `Counter`
- `deque`

Why this matters:

- Cleaner code
- Faster execution
- More expressive intent

Example idea:

- `defaultdict(int)` avoids manual key checks
- Perfect for counting problems and LeetCode-style tasks

Using `collections` shows:

- Strong standard library knowledge
- Practical Python experience

**Related Examples**

- [`14.collections.py`](../14.collections.py)

---

## 15. Encapsulation

Encapsulation is about **hiding internal state** and exposing controlled access.

In Python:

- Achieved via naming conventions
- Double underscore (`__`) triggers name mangling

Example idea:

- `__balance` cannot be accessed directly
- Must use a getter method

This protects:

- Internal invariants
- Object integrity
- API stability

Python doesn’t enforce privacy strictly, but **convention matters**.

**Related Examples**

- [`15.encapsulation.py`](../15.encapsulation.py)

---

## 16. Abstraction

Abstraction hides complexity and exposes only what’s necessary.

In Python, this is often done using:

- Abstract Base Classes (ABCs)
- The `abc` module

ABCs:

- Define required methods
- Enforce contracts
- Prevent incomplete implementations

If a class subclasses an ABC:

- It **must** implement all abstract methods
- Or it cannot be instantiated

This is common in frameworks and large systems.

**Related Examples**

- [`16.abstraction.py`](../16.abstrazction.py)

---

## 17. Abstract Base Classes (`abc`)

ABCs are Python’s way of enforcing interfaces.

Key points:

- Use `ABC` and `@abstractmethod`
- Child classes must implement required methods
- Prevents silent bugs

When to use:

- You never instantiate the parent
- You want strict contracts
- You want clean architecture

This is heavily used in Django, FastAPI internals, and libraries.

**Related Examples**

- [`17.abstract_classes.py`](../17.abstract_classes.py)

---

## 18. Inheritance

Inheritance allows:

- Reuse of logic
- Shared behavior
- Hierarchical design

Important design rule:

- If the parent is never instantiated → use an ABC
- If the parent is concrete → normal inheritance is fine

You can enforce behavior using:

- `NotImplementedError`
- But ABCs are cleaner and clearer

Bad inheritance causes:

- Tight coupling
- Fragile code
- Maintenance nightmares

**Related Examples**

- [`18.inheritance.py`](../18.inheritance.py)

---

## 19. Polymorphism

Polymorphism means:

> The same interface, different behavior

In Python:

- Achieved through method overriding
- Duck typing
- Shared interfaces

Example idea:

- `Shape.area()` behaves differently for Circle vs Rectangle

Polymorphism enables:

- Extensibility
- Cleaner APIs
- Fewer conditionals

This is one of the reasons Python scales well in large codebases.

**Related Examples**

- [`19.polymorphism.py`](../19.polymorphism.py)

---

## 20. Python Data Model (Magic / Dunder Methods)

The data model defines **how objects interact with Python itself**.

These are the `__dunder__` methods.

Examples:

- `__init__`
- `__len__`
- `__repr__`
- `__enter__` / `__exit__`

Understanding the data model lets you:

- Make custom objects behave like built-ins
- Improve readability
- Build powerful abstractions

This is core senior-level knowledge.

**Related Examples**

- [`51.call_method.py`](../51.call_method.py)
- [`_slots.py`](../_slots.py)

---

## 21. Iterators

An iterator is any object that implements:

- `__iter__()`
- `__next__()`

Behavior:

- Returns next value
- Raises `StopIteration` when done

Iterators:

- Are stateful
- Are consumed once
- Are everywhere in Python

Understanding iterators helps with:

- Performance
- Lazy evaluation
- Custom data pipelines

**Related Examples**

- [`21.iterators.py`](../21.iterators.py)

---

## 22. Generators

Generators are a **special way to create iterators**.

Defined using:

- `yield`

Key properties:

- Lazy evaluation
- Minimal memory usage
- Pause and resume execution

Important detail:

- Calling a generator function does NOT execute it
- Execution starts when `next()` is called

Generators are essential for:

- Streaming data
- Large datasets
- Memory-sensitive applications

**Related Examples**

- [`22.generators.py`](../22.generators.py)

---

## 23. `@staticmethod` and `@classmethod`

These change how methods behave.

**Class methods:**

- Receive the class (`cls`)
- Can be called on class or instance
- Used for factory methods or class-level logic

**Static methods:**

- Receive nothing automatically
- Behave like namespaced functions
- Used when logic belongs to class conceptually

Choosing the right one improves:

- Readability
- Design clarity
- API correctness

**Related Examples**

- [`23.staticmethods_and_classmethods.py`](../23.staticmethods_and_classmethods.py)

---

## 24. Dependency Injection

Dependency Injection means:

- Dependencies are provided externally
- Not created inside the class

Why it matters:

- Looser coupling
- Easier testing
- More flexible design

Common form:

- Constructor injection

This allows:

- Swapping implementations
- Mocking in tests
- Cleaner architecture

Used heavily in:

- Backend systems
- Large services
- Testable codebases

**Related Examples**

- [`24.with_dependency_injection.py`](../24.with_dependency_injection.py)
- [`24.without_dependency_injection.py`](../24.without_dependency_injection.py)

---

## 25. Parameterized Testing

Parameterized testing lets you:

- Run the same test
- With multiple inputs
- In a clean, readable way

Using `pytest`:

- Pass lists of inputs
- Avoid duplicated tests
- Improve coverage

This is essential for:

- Backend development
- API testing
- Data validation

Shows:

- Testing maturity
- Professional engineering habits

**Related Examples**

- [`26.pytest_fixtures.py`](../26.pytest_fixtures.py)
