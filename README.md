## Architecture

Library consists of several loosely coupled submodules:

- `pycyphal.dsdl` — DSDL language support: transcompilation (code generation) and object serialization. This module is a thin wrapper over Nunavut.
- `pycyphal.transport` — the abstract Cyphal transport layer model and several concrete transport implementations (Cyphal, Cyphal/UDP, Cyphal/serial, etc.). This submodule exposes a relatively low-level API where data is represented as serialized blocks of bytes. 
- `pycyphal.presentation` — this layer binds the transport layer together with DSDL serialization logic, providing a higher-level object-oriented API. At this layer, data is represented as instances of auto-generated Python classes (code generation is managed by `pycyphal.dsdl`). 
- `pycyphal.application` — the top-level API for the application. The factory `pycyphal.application.make_node()` is the main entry point of the library.
- `pycyphal.util` — a loosely organized collection of various utility functions and classes that are used across the library.

