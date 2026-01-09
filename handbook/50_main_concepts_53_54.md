# Advanced Python Interview Reference

## Concepts 53–54 (Senior-Level)

---

## 53 — Typing: Protocols & Generics


Protocols and generics are tools from Python’s static typing system that allow you to write flexible APIs without losing type safety.

Common use cases: 

- Polymorphic interfaces (duck typing)
- Flexible function/type arguments 
- Safer, clearer APIs

**Related Examples**
- [`53.typing_protocols_and_generics.py`](../53.typing_protocols_and_generics.py)

---

## 54 — Descriptors (Typed + CachedProperty)

Descriptors let you control how attributes are accessed and stored on objects. They're used to add type enforcement, lazy computation, or caching to attribute access.

Common use cases:

- Type validation on assignment
- Cached/computed properties (like @property but cached)
- Logging or auditing attribute changes
- Read-only or write-only attributes
- Custom attribute behavior in libraries and frameworks


**Related Examples**
- [`54.descriptors.py`](../54.descriptors.py)
