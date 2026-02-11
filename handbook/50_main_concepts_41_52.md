# Advanced Python Interview Reference

## Concepts 41–50 (Senior-Level)

---

## 41. `WeakKeyDictionary` & `WeakValueDictionary`

These are specialized dictionaries from the `weakref` module.

What makes them different:

- Keys or values are held as **weak references**
- Objects can still be garbage collected
- Entries disappear automatically when objects are destroyed

Use cases:

- Attaching metadata to objects
- Caches that should not keep objects alive
- Observer-style patterns

This prevents subtle memory leaks in long-running systems.

**Related Examples**

- [`41.weak_key_dictionary.py`](../41.weak_key_dictionary.py)
- [`39.weakref.py`](../39.weakref.py)

---

## 42. Optimizing Memory with `__slots__`

By default, Python stores instance attributes in a dynamic `__dict__`.

`__slots__`:

- Explicitly declares allowed attributes
- Prevents creation of `__dict__`
- Reduces memory usage per instance

Best for:

- Classes with many instances
- Performance-critical systems
- Data-heavy applications

Tradeoff:

- Less flexibility
- Slightly more rigid design

**Related Examples**

- [`_slots.py`](../_slots.py)

---

## 43. `memory_profiler`

A tool for **tracking memory usage line-by-line**.

Why it matters:

- Identifies memory leaks
- Shows which functions consume memory
- Critical for optimizing large systems

Usage pattern:

- Decorate functions
- Run program
- Analyze memory growth

This is production-level debugging, not beginner tooling.

**Related Examples**

- [`43.memory_profiler.py`](../43.memory_profiler.py)

---

## 44. `sys.getsizeof()`

Returns the **shallow size** of an object in bytes.

Important detail:

- Does NOT include referenced objects
- Only the object itself

Useful for:

- Comparing object sizes
- Estimating memory impact
- Understanding storage costs

Often used alongside memory profilers for deeper analysis.

**Related Examples**

- [`44.getsizeof.py`](../44.getsizeof.py)

---

## 45. Advanced Decorators

Decorators can do much more than logging.

Advanced uses include:

- Attaching state to functions
- Counting calls
- Caching results
- Authentication and authorization
- Stacking multiple behaviors

They can:

- Wrap functions
- Wrap classes
- Accept arguments themselves

This demonstrates strong functional programming skills.

**Related Examples**

- [`45.advanced_decorators.py`](../45.advanced_decorators.py)

---

## 46. `dataclasses`

Dataclasses remove boilerplate from data-heavy classes.

They automatically generate:

- `__init__`
- `__repr__`
- `__eq__`
- `__hash__` (optional)

Perfect for:

- DTOs
- Config objects
- Domain models

They make code:

- Cleaner
- More readable
- Easier to maintain

**Related Examples**

- [`46.dataclasses.py`](../46.dataclasses.py)

---

## 47. Metaprogramming

Metaprogramming is code that **modifies or generates code**.

In Python this includes:

- Decorators
- Metaclasses
- Dynamic attribute creation
- Runtime inspection

Used heavily in:

- Frameworks
- ORMs
- Dependency injection systems

Powerful, but must be used carefully to avoid unreadable code.

**Related Examples**

- [`36.metaclasses.py`](../36.metaclasses.py)
- [`45.advanced_decorators.py`](../45.advanced_decorators.py)

---

## 48. `functools`

The `functools` module provides function utilities.

Key tools:

- `wraps` → preserves metadata in decorators
- `lru_cache` → memoization
- `reduce` → cumulative operations

These help:

- Avoid reimplementing patterns
- Write cleaner abstractions
- Improve performance

Interviewers love seeing standard library mastery.

**Related Examples**

- [`48.functools.py`](../48.functools.py)

---

## 49. Advanced Dataclass Features

Dataclasses support advanced customization.

Examples:

- `__post_init__` for validation
- Inheritance between dataclasses
- `field()` for fine-grained control
- `frozen=True` for immutability

This allows:

- Safer models
- Controlled initialization
- Clean validation logic

Very common in modern Python codebases.

**Related Examples**

- [`49.advanced_dataclass_features.py`](../49.advanced_dataclass_features.py)

---

## 50. `asyncio`

`asyncio` enables **asynchronous, non-blocking programming**.

Core concepts:

- Coroutines (`async def`)
- `await`
- Event loop
- Tasks
- Queues

Best for:

- Network I/O
- APIs
- Databases
- Web scraping
- Real-time systems

It provides concurrency without threads or processes and is a core skill for modern Python engineers.

**Related Examples**

- [`50.asyncio.py`](../50.asyncio.py)
- [`52.multiprocess_with_queue.py`](../52.multiprocess_with_queue.py)

Understood. Below are **51 and 52 rewritten to exactly match the existing style** (structure, tone, and linking), with **no extra commentary**.

---

## 51. Callable Objects (`__call__`)

Objects can be made **callable** by defining a `__call__` method.

What this enables:

- Instances behave like functions
- Objects can retain internal state
- Configuration and behavior live together

Use cases:

- Function-like objects with state
- Strategy-style patterns
- Reusable, parameterized behavior

This is cleaner than closures when state must persist across calls.

**Related Examples**

- [`51.callable_objects.py`](../51.call_method.py)

---

## 52. Multiprocessing with `Queue`

The `multiprocessing` module enables **true parallelism** using separate processes.

Key concepts:

- Each process has its own memory space
- `Queue` allows safe inter-process communication
- Execution order is non-deterministic

Use cases:

- CPU-bound workloads
- Multi-stage processing pipelines
- Parallel data transformation

This pattern avoids the GIL and scales across CPU cores.

**Related Examples**

- [`52.multiprocess_with_queue.py`](../52.multiprocess_with_queue.py)
