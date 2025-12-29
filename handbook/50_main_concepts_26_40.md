# Advanced Python Interview Reference

## Concepts 26–40 (Senior-Level)

---

## 26. Fixtures (Testing Setup & Teardown)

Fixtures are how you **prepare and clean up test environments** in pytest.

Key idea:

- A fixture runs before a test
- Yields a resource
- Cleanup happens after the test finishes

This is extremely useful for:

- Database connections
- Temporary files
- External services

Instead of setting up and tearing down for every test, you:

- Do it once
- Reuse it safely
- Keep tests clean and readable

This is backend-engineer-level testing knowledge.

**Related Examples**

- [`26.pytest_fixtures.py`](../26.pytest_fixtures.py)

---

## 27. Serialization & Deserialization

Serialization is converting objects into a format that can be:

- Stored on disk
- Sent over the network
- Cached
- Reconstructed later

In Python, this is often done with:

- `pickle`
- JSON (for interoperability)

Common use cases:

- Saving ML models
- Storing configs
- Caching expensive results

Deserialization restores the object back to its original state.

Important note:

- Pickle is powerful but **not secure** for untrusted data

**Related Examples**

- [`27.serialization_deserialization.py`](../27.serialization_deserialization.py)
- [`example.bin`](../example.bin)
- [`handler.pkl`](../handler.pkl)
- [`person.pkl`](../person.pkl)

---

## 28. `__getstate__` and `__setstate__`

These methods customize how objects are pickled.

Why they exist:

- Some objects cannot be serialized
- File handles, sockets, threads, etc.

`__getstate__`:

- Called during serialization
- Remove or transform unserializable fields

`__setstate__`:

- Called during deserialization
- Restore missing state

This shows deep understanding of:

- Object lifecycle
- Serialization internals

**Related Examples**

- [`28.__getstate___and__setstate__.py`](../28.__getstate___and__setstate__.py)

---

## 29. `heapq`

`heapq` implements a **priority queue** using a binary heap.

Key properties:

- Min-heap by default
- Fast insert: `O(log n)`
- Fast pop: `O(log n)`
- Fast access to smallest element: `O(1)`

Why not use a list?

- Lists require `O(n)` inserts/removals
- Heaps scale much better

Common use cases:

- Task schedulers
- Shortest-path algorithms
- Anytime “highest priority first” matters

**Related Examples**

- [`29.heapq.py`](../29.heapq.py)

---

## 30. Higher-Order Functions

A higher-order function:

- Takes a function as input
- Or returns a function

This enables:

- Reusable logic
- Clean abstractions
- Functional-style programming

You see this a lot in:

- Validators
- Callbacks
- Middleware
- Decorators

Frameworks like Django rely heavily on this pattern.

**Related Examples**

- [`30.higher_order_functions.py`](../30.higher_order_functions.py)

---

## 31. `filter`

`filter` is a built-in higher-order function.

It:

- Takes a predicate function
- Returns only items where predicate is `True`

This replaces:

- Verbose loops
- Manual condition checks

Example idea:

- Filtering even numbers
- Validating datasets

Using `filter` shows:

- Standard library fluency
- Clean Python style

**Related Examples**

- [`31.filter.py`](../31.filter.py)

---

## 32. Advanced List Comprehensions

List comprehensions can do much more than simple loops.

You can:

- Nest loops
- Add conditionals
- Call functions
- Transform data inline

This allows:

- Very expressive one-liners
- Cleaner and faster code
- Reduced boilerplate

Senior engineers know when to use this—and when not to overdo it.

**Related Examples**

- [`32.advanced_list_comprehension.py`](../32.advanced_list_comprehension.py)

---

## 33. `bytes`

`bytes` represents **binary data**.

Key properties:

- Immutable
- Values from 0–255
- Common in low-level work

Used for:

- Files
- Network packets
- Images
- Audio
- Protocols

Understanding `bytes` is critical when dealing with:

- File I/O
- APIs
- Performance-sensitive systems

**Related Examples**

- [`33.bytes.py`](../33.bytes.py)
- [`example.txt`](../example.txt)
- [`file1.txt`](../file1.txt)
- [`file2.txt`](../file2.txt)

---

## 34. Bytecode & `dis` Module

Python source code is compiled into **bytecode** before execution.

The `dis` module lets you:

- Inspect bytecode
- See how Python executes code
- Identify inefficiencies

This helps with:

- Performance optimization
- Understanding interpreter behavior
- Learning Python internals

Senior engineers don’t use this daily—but knowing it exists matters.

**Related Examples**

- [`34.python_bytecode.py`](../34.python_bytecode.py)

---

## 35. `memoryview`

`memoryview` lets you:

- Work with slices of data
- Without copying it

This is critical for:

- Large binary files
- Network buffers
- Memory efficiency

Normal slicing creates copies.
`memoryview` creates **views**.

Using this can massively reduce memory usage in data-heavy systems.

**Related Examples**

- [`35.memoryview.py`](../35.memoryview.py)

---

## 36. Metaclasses

Metaclasses define **how classes themselves are created**.

By default:

- Every class uses `type` as its metaclass

With custom metaclasses you can:

- Modify class creation
- Inject attributes
- Enforce rules
- Generate behavior dynamically

This is advanced but very powerful.

**Related Examples**

- [`36.metaclasses.py`](../36.metaclasses.py)

---

## 37. Metaclasses in Frameworks (Django Example)

Django models use a custom metaclass.

What happens:

- You define a class
- Metaclass intercepts creation
- Fields are collected
- Database mappings are generated
- Managers are attached

This explains:

- Why Django models feel “magic”
- How frameworks automate behavior

Understanding this separates advanced users from power users.

**Related Examples**

- [`36.metaclasses.py`](../36.metaclasses.py)

---

## 38. Nesting & Combining Context Managers

You can nest context managers using:

```python
with open(a), open(b):
    ...
```

When context managers are dynamic:

- Use `contextlib.ExitStack`

This allows:

- Programmatic management
- Dynamic resource handling
- Clean teardown logic

Very useful for:

- Files
- DB connections
- Resource pools

**Related Examples**

- [`37.nesting_and_combining_context_managers.py`](../37.nesting_and_combining_context_managers.py)

---

## 39. Custom Context Managers

You can create context managers using:

- Classes with `__enter__` / `__exit__`
- Or generators with `@contextmanager`

Generator-based context managers:

- Are simpler
- Are more readable
- Are very common in production code

Especially useful for:

- Database transactions
- Temporary states
- Resource handling

**Related Examples**

- [`38.custom_context_managers.py`](../38.custom_context_managers.py)

---

## 40. `weakref`

Weak references do **not increase reference count**.

This allows:

- Garbage collection of objects
- Even if they are referenced weakly

Useful for:

- Caching
- Metadata storage
- Avoiding memory leaks

Downside:

- Object may disappear unexpectedly
- Must ensure strong references exist when needed

This shows deep GC and memory knowledge.

**Related Examples**

- [`39.weakref.py`](../39.weakref.py)
- [`41.weak_key_dictionary.py`](../41.weak_key_dictionary.py)
