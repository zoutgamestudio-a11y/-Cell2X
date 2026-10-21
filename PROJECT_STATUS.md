# CellX2 — Project Status

**Snapshot date:** 2026-10-21  
**Project identity:** CellX2 / ZoutGameStudio  
**Status:** Initial research and organization

## 1. Mission

CellX2 investigates the feasibility of recompiling PlayStation 3 software for execution on other platforms. The work must proceed from reproducible evidence rather than assumptions. Instruction decoding, code generation, runtime behavior, and whole-program execution are separate claims and must be validated separately.

## 2. Current state

### Established

- The project name and initial research direction have been recorded.
- A research dossier has been prepared for PS3Recomp and RPCS3 at pinned source revisions.
- An SPU/SPURS audit has identified implementation paths, documented tests, unresolved semantic questions, and possible runtime edge cases.
- An initial evidence classification scheme is defined in `RESEARCH_LEDGER.md`.
- An initial test specification is defined in `TEST_PLAN.md`.

### Not established by CellX2

- An independently implemented or tested PPU translator.
- An independently implemented or tested SPU translator.
- A CellX2 runtime that executes a real PS3 program.
- Successful execution of a complete PS3 game.
- Independent semantic conformance across the PPU or SPU instruction sets.

The reference projects have their own documented capabilities and tests. Those results must not be represented as CellX2 results.

## 3. Reference snapshots

| Project | Pinned revision | Intended use |
|---|---|---|
| PS3Recomp | `749182eebb936f086a007f63e1c7d853f3cf708a` (`v0.16.0`) | Primary reference for static recompilation, lifting, generated-code tests, and title-specific runtime work |
| RPCS3 | `4024ea31e049f3205ae406eb3f37fe7625e1bc98` | Supporting reference for instruction behavior, execution state, OS/device contracts, and cross-checking |

Use pinned revisions when making technical claims. A moving `master` branch is not sufficient provenance.

## 4. Working rules

1. **Do not promote a source project's claim into a CellX2 result.** Record it as `DOCUMENTED` until CellX2 independently reproduces it.
2. **Do not equate compilation with correctness.** A program can compile while decoding or runtime semantics are wrong.
3. **Keep uncertainty explicit.** Use `UNVERIFIED` when evidence is incomplete.
4. **Prefer small, falsifiable experiments.** Each test should define input state, expected output state, source of the expected result, and a pass/fail rule.
5. **Avoid silent success.** Unsupported instructions or runtime behavior should be reported as unsupported rather than replaced with a no-op and treated as correct.
6. **Preserve provenance.** Record source revision, test version, command, environment, result, and artifact hashes for every test that is actually run.
7. **Do not claim tests were run when only their source was inspected.**
8. **Review licensing before copying code.** PS3Recomp is MIT-licensed; RPCS3 is GPL-2.0. Using a project as a behavioral reference does not imply that its code may be copied without review.

## 5. Work packages

- **PPU:** decoding, integer semantics, CR/XER, branching and linking, memory, reservations, floating-point state, VMX.
- **SPU:** decoding, register and lane semantics, local store, channels, branches, floating point, MFC/DMA, events and synchronization.
- **Runtime/OS:** address space, modules and relocations, imports, TLS, threads, syscalls, filesystem, audio, input, network, graphics and lifecycle.
- **Validation infrastructure:** golden vectors, differential checks, failure-closed generation, reproducible build artifacts and provenance.

These packages should not be marked complete as one combined checkbox. Each has separate acceptance criteria.

## 6. Immediate checkpoint

The next research task is to turn the highest-priority SPU uncertainties into a small, source-backed specification before attempting implementation:

1. Confirm the instruction encoding and operand fields for `FNMS`, `SHLQBY`/`SHLQBYI`, `BRHZ` and `BRHNZ`.
2. Write expected architectural-state results from the SPU ISA reference, then cross-check RPCS3 as a second source.
3. Define distinct-lane and aliasing test vectors.
4. Keep the test status as **SPECIFIED — NOT RUN BY CELLX2** until execution and output have actually been captured.
5. Start the PPU slice only after the SPU specification and project ledger are stable enough to reproduce.

## 7. Session notes and supporting reports

The supporting research files from the 2026-10-21 review are:

- `CellX2_Research_Dossier_2026-10-21.md`
- `CellX2_SPU_Audit_2026-10-21.md`

They provide the longer audit narrative. The five files in this pack are the maintained project-control documents, not substitutes for the detailed audit reports.
