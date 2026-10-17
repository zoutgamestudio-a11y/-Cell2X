# PS3Recomp — Reference Project Analysis

## 1. Purpose

PS3Recomp is the primary reference project for
investigating static recompilation of PlayStation 3 software.

Official repository:
https://github.com/sp00nznet/ps3recomp

## 2. Initial Observations

The project's documentation describes components for:

- ELF and related executable-format analysis.
- PPU instruction disassembly.
- PPU-to-C/C++ code generation.
- SPU instruction disassembly and code generation.
- Runtime state and memory handling.
- System-service implementations and stubs.
- Graphics-related runtime components.

These observations describe the reference project.
They do not establish that every component is complete
or correct for every game.

## 3. PPU Research

Questions to investigate:

- Which PPU instructions are supported?
- How are guest registers represented?
- How are branches and indirect calls translated?
- How is guest memory represented?
- How are imports and system calls handled?
- Which execution dependencies remain incomplete?

## 4. SPU Research

Questions to investigate:

- Which SPU instructions are supported?
- How are vector operations represented?
- How is local store modeled?
- How are channels and mailboxes represented?
- How are DMA operations modeled?
- Which synchronization behaviors require additional work?

## 5. Runtime Research

Questions to investigate:

- How is guest memory addressed?
- How are threads and synchronization handled?
- How are system services resolved?
- How are module dependencies represented?
- Which host operating system assumptions exist?

## 6. Verification Plan

1. Record the exact upstream commit.
2. Read the relevant documentation at that commit.
3. Map documented features to source files and tests.
4. Identify explicit limitations.
5. Select small tests that can be reproduced independently.
6. Record results without assuming that upstream claims
   are automatically verified by CellX2.

## 7. Current Status

DOCUMENTED:
The upstream repository describes a static recompilation
pipeline and associated runtime components.

UNVERIFIED BY CELLX2:
- The current build status on our environment.
- Independent reproduction of upstream tests.
- Semantic correctness of selected instructions.
- Successful execution of a complete commercial game.
- Compatibility with PlayStation 4.

## 8. Next Action

Record the exact upstream commit and begin a component
inventory before deciding whether to implement new code.