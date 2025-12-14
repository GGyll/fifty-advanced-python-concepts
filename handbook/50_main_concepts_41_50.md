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

---
