# PS3Recomp — Reference Project Analysis

## 1. Purpose

PS3Recomp is the primary reference project for investigating static recompilation of PlayStation 3 software.

Official repository: https://github.com/sp00nznet/ps3recomp

## 2. Pinned revision

Primary reviewed snapshot: `749182eebb936f086a007f63e1c7d853f3cf708a`.

The older commit `39a36296511c445707adabcd312f0b740cfbd694` is an ancestor of that snapshot. Findings must identify the precise commit inspected; do not combine claims from different revisions without saying so.

## 3. Initial observations

The project's documentation describes components for:
- ELF and related executable-format analysis.
- PPU instruction disassembly.
- PPU-to-C/C++ code generation.
- SPU instruction disassembly and code generation.
- Runtime state and memory handling.
- System-service implementations and stubs.
- Graphics-related runtime components.

These observations describe the reference project. They do not establish that every component is complete or correct for every program.

## 4. PPU research

Questions to investigate:
- Which PPU instructions are supported?
- How are guest registers represented?
- How are branches and indirect calls translated?
- How is guest memory represented?
- How are imports and system calls handled?
- Which execution dependencies remain incomplete?

## 5. SPU research

Questions to investigate:
- Which SPU instructions are supported?
- How are vector operations represented?
- How is local store modeled?
- How are channels and mailboxes represented?
- How are DMA operations modeled?
- Which synchronization behaviors require additional work?

## 6. Runtime research

Questions to investigate:
- How is guest memory addressed?
- How are threads and synchronization handled?
- How are system services resolved?
- How are module dependencies represented?
- Which host operating-system assumptions exist?

## 7. Verification plan

1. Record the exact upstream commit.
2. Read relevant documentation at that commit.
3. Map documented features to source files and tests.
4. Identify explicit limitations.
5. Select small tests that can be reproduced independently.
6. Record results without assuming that upstream claims are automatically verified by CellX2.

## 8. Current status

**DOCUMENTED:** The upstream repository describes a static recompilation pipeline and associated runtime components.

**UNVERIFIED BY CELLX2:**
- Independent reproduction of upstream tests.
- Semantic correctness of selected instructions.
- Successful execution of a complete commercial game.
- Broad compatibility beyond the currently studied test scope.

## 9. Next action

Continue the component inventory at the pinned revision, complete ISA-backed expected vectors for selected SPU instructions, and choose a small reproducible test before considering implementation scope.
