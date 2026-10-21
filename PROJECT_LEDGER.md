# CellX2 — Project Ledger

**Snapshot date:** 2026-10-21  
**Status:** Initial research and organization

## 1. Project objective

CellX2 investigates the feasibility of recompiling PlayStation 3 software. The current phase is limited to architecture research, source auditing, and defining reproducible tests. No end-to-end execution capability is claimed.

Research areas:
- PowerPC PPU instruction semantics and translation.
- SPU instruction semantics and translation.
- Runtime and operating-system dependencies.
- Memory, control-flow, and execution semantics.
- Graphics, audio, input, and lifecycle dependencies.

## 2. Evidence classification

- **DOCUMENTED** — found in an identified source and pinned revision; not independently verified by CellX2.
- **INDEPENDENTLY TESTED** — executed by CellX2 with recorded inputs, outputs, environment, and result.
- **SEMANTICALLY VERIFIED** — compared with an independent architectural specification or oracle, with relevant state checked.
- **INTEGRATION VERIFIED** — multiple components exercised together reproducibly by CellX2.
- **UNVERIFIED** — hypothesis or claim that still requires evidence.

These categories are not interchangeable. Source inspection and upstream test reports do not count as CellX2 execution results.

## 3. Current project status

### Established
- Repository and initial project description exist.
- A research baseline has been recorded for PS3Recomp and RPCS3 at pinned revisions.
- Principal PPU/SPU source paths and relevant test/documentation areas have been inventoried.
- Initial PPU/SPU research notes and test specifications exist.
- An evidence ledger distinguishes reference-project claims from CellX2 results.

### Not established by CellX2
- An independently implemented or tested PPU translator.
- An independently implemented or tested SPU translator.
- A working CellX2 runtime.
- Semantic conformance across either instruction set.
- Successful execution of a real PS3 program or complete game.

## 4. Pinned reference snapshots

| Project | Revision | Role |
|---|---|---|
| PS3Recomp | `749182eebb936f086a007f63e1c7d853f3cf708a` | Primary static-recompilation, lifter, runtime, and test reference |
| RPCS3 | `4024ea31e049f3205ae406eb3f37fe7625e1bc98` | Supporting behavioral and subsystem reference |

The older PS3Recomp commit `39a36296511c445707adabcd312f0b740cfbd694` is a parent of the pinned revision, not the current primary baseline. Findings must identify the exact revision they describe. Do not use a moving branch as provenance for a technical claim.

## 5. Research work packages

### A — PPU
- Instruction encoding and semantics.
- Registers and condition state, including CR/XER.
- Branches, calls, and link/count behavior.
- Memory access, endianness, and reservations.
- Floating-point and vector behavior.

### B — SPU
- Instruction decoding and operand fields.
- Vector and lane semantics.
- Local store and control flow.
- Channels and mailboxes.
- MFC/DMA, tags, events, and synchronization.

### C — Runtime and OS
- Address space and memory model.
- System calls and imports.
- Threads and synchronization.
- Module loading, relocations, and TLS.
- Host/guest ABI boundaries and lifecycle.

### D — Hardware-dependent subsystems
- Graphics, audio, input, timing, and synchronization.
- Requirements must be derived from a minimal test rather than assumed in advance.

## 6. Milestones

- [x] Create repository and draft initial project description.
- [x] Record pinned reference commits.
- [x] Begin a component inventory of principal PPU/SPU paths.
- [x] Draft initial PPU/SPU research notes and test specifications.
- [ ] Finish ISA-backed expected vectors for the first SPU tests.
- [ ] Execute and record the first reproducible CellX2 test.
- [ ] Establish a minimal test harness and synthetic program.
- [ ] Map runtime dependencies based on observed test requirements.

A drafted test specification is not a completed test run. The component inventory is broad but does not represent a line-by-line audit of every reference file.

## 7. Evidence rules

Every executed test must record:
- Stable test identifier and test/tool revision.
- Raw input bytes or opcode and initial architectural state.
- Expected decode and expected final state.
- Exact architectural source for the expected result.
- Secondary comparison source and pinned revision, if used.
- Build and execution commands, environment, and exit code.
- Actual output, relevant logs, and known limitations.
- Artifact hashes where practical.

A generated source file is not proof of semantic correctness. A successful build is not proof of correct execution. A successful startup is not proof that a complete program works.

## 8. Decision log

No architectural decision is final until its rationale, alternatives, and supporting evidence are recorded. Unresolved questions must remain explicit and must not be relabeled as confirmed defects.

## 9. Current conclusion

CellX2 remains in the initial research and organization phase. The next priority is to complete small, ISA-backed SPU test vectors, then execute the first reproducible test when a suitable environment is available. No CellX2 end-to-end execution has been independently verified.
