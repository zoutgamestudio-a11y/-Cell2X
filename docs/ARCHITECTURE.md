# CellX2 — Architecture Research

## 1. Scope

CellX2 investigates the components required to translate PlayStation 3 software into native host code.

The initial objective is to establish a correct and testable execution path for a small program. Full-program support is a later objective and must be supported by evidence.

## 2. Conceptual Pipeline

Input executable
    |
    v
Executable-format analysis
    |
    v
Instruction decoding
    |
    v
Control-flow and function analysis
    |
    v
Instruction translation
    |
    v
Generated native source
    |
    v
Native compilation
    |
    v
Runtime and system-service integration
    |
    v
Execution and verification

This is a conceptual model, not an implemented pipeline.

## 3. PPU

The PPU work package covers:
- Instruction semantics.
- Register state.
- Control flow.
- Memory operations.
- Floating-point and vector behavior.
- Function calls and ABI behavior.

## 4. SPU

The SPU work package covers:
- Instruction decoding and semantics.
- Vector registers.
- Local store.
- Channels and mailboxes.
- DMA behavior.
- Synchronization and task execution.

## 5. Runtime

The runtime work package covers:
- Guest memory.
- System services.
- Threads and synchronization.
- Module dependencies.
- Host and guest ABI boundaries.

## 6. Graphics and Other Subsystems

Graphics, audio, and input may require separate implementations or compatibility layers.

Their requirements must be established from the selected test program rather than assumed in advance.

## 7. Execution Environment

The first practical target should be a host environment where tests can be built, executed, and debugged reproducibly. Broader platform feasibility is deferred until instruction-level and minimal-program experiments provide evidence.

## 8. Design Rules

- Prefer small, independently testable components.
- Keep architectural semantics separate from host-specific code.
- Record assumptions and known limitations.
- Avoid duplicating existing components without evidence that replacement is necessary.
- Do not claim compatibility based solely on successful compilation.

## 9. Current Implementation Status

All architecture descriptions in this document are research plans unless explicitly marked otherwise.

No complete CellX2 execution pipeline has been verified.
