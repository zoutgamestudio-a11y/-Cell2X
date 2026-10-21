# CellX2 — Research Ledger

**Snapshot date:** 2026-10-21  
**Purpose:** track claims, sources, confidence, and the next evidence needed to change each status.

## Status definitions

- **DOCUMENTED** — stated in an identified source at a pinned revision; not independently verified by CellX2.
- **INDEPENDENTLY TESTED** — run by CellX2 with recorded inputs, outputs, environment, and result.
- **SEMANTICALLY VERIFIED** — compared against an independent architectural specification or oracle, with relevant state checked.
- **INTEGRATION VERIFIED** — multiple components exercised together reproducibly by CellX2.
- **UNVERIFIED** — hypothesis, incomplete evidence, or a claim not yet demonstrated.

These statuses are not interchangeable. `DOCUMENTED` does not mean `INDEPENDENTLY TESTED`.

## Pinned sources

| Source ID | Project / source | Revision | Role |
|---|---|---|---|
| SRC-PS3R | [PS3Recomp](https://github.com/sp00nznet/ps3recomp) | `749182eebb936f086a007f63e1c7d853f3cf708a` (`v0.16.0`) | Static recompilation and title-runtime reference |
| SRC-RPCS3 | [RPCS3](https://github.com/RPCS3/rpcs3) | `4024ea31e049f3205ae406eb3f37fe7625e1bc98` | Behavioral and subsystem reference |
| SRC-SPU-ISA | SPU ISA v1.2 manual | Public architectural document; record the exact local copy/page when used in a test | Independent architectural reference for SPU semantics |

**Revision rule:** update this table whenever the reviewed commits change. Findings must cite specific paths and, where possible, line ranges or test names. Do not record only a moving branch name.

## Claims ledger

| ID | Claim | Status | Evidence presently identified | Limit / next action |
|---|---|---|---|---|
| E-001 | PS3Recomp documents a PPU disassembly/lifting path and runtime loader/dispatch path. | `DOCUMENTED` | `docs/PPU_RECOMP.md`; `tools/ppu_disasm.py`; `tools/ppu_lifter.py`; `tools/ppu_loader.py`; `runtime/ppu/` | The reported coverage is sample-specific. CellX2 has not independently reproduced it. |
| E-002 | PS3Recomp contains an SPU decoder/lifter and runtime components for local store, channels, and MFC/DMA. | `DOCUMENTED` | `tools/spu_disasm.py`; `tools/spu_lifter.py`; `runtime/spu/`; `docs/SPU_LIFTER.md` | Component existence does not prove that every instruction or runtime interaction is correct. |
| E-003 | On one documented Uncharted SPU sample, decoder-emitted mnemonics had lifter coverage, while 683 outputs remained `.word`. | `DOCUMENTED` | `docs/SPU_LIFTER.md` | Single sample only. `.word` may represent data or unclassified instructions; classify by address and control-flow context. |
| E-004 | PS3Recomp documentation describes a 63-case SPU unit suite and four selected end-to-end tests (sum, `shufb`, branch/return, DMA). | `DOCUMENTED` | `docs/SPU_LIFTER.md`; SPU test files | These are claims about the reference project's tests, not CellX2 tests or complete ISA conformance. |
| E-005 | PS3Recomp has a focused FNMS regression fixture with 449 input cases and 16,164 assertions according to the reviewed test/change description. | `DOCUMENTED` | `tools/test_spu_fnms_zero_extended.py`; `tests/test_spu_fnms_zero_extended.c` | The inspected test source was not run by CellX2. Re-check current counts if revisions change. |
| E-006 | Current PS3Recomp SPU floating-point helper code uses custom SPU-range-aware arithmetic paths. | `DOCUMENTED` | `runtime/spu/spu_helpers.h`, including `spu__sf_split`, `spu__sf_pack`, and `spu__fma_lane` | Requires semantic comparison against the ISA for each tested behavior; code inspection alone is not proof. |
| E-007 | Some SPU questions remain explicitly unresolved in PS3Recomp documentation, including `shlqby` direction and `brhz`/`brhnz` halfword selection in host representation. | `DOCUMENTED` | `docs/SPU_LIFTER.md` | Resolve using the architectural manual and asymmetric test vectors before coding. |
| E-008 | Some inspected runtime paths may report a malformed DMA transfer as rejected while completion handling may still advance. | `UNVERIFIED` | `runtime/spu/spu_dma.h`; related audit notes | Treat as a test candidate, not a confirmed defect. Record data effects and tag/error status separately. |
| E-009 | PPU lifting has incomplete floating-point status updates and some unsupported SPR cases are emitted as no-ops. | `DOCUMENTED` | `tools/ppu_lifter.py` and PPU audit notes | Inventory the precise instructions/paths. An emitted no-op must not count as semantic support. |
| E-010 | Runtime requirements extend beyond instruction translation to memory, module loading, TLS, threading, syscalls, devices and game lifecycle. | `DOCUMENTED` | PS3Recomp `runtime/`, `libs/`; RPCS3 memory/LV2/PPU/SPU/RSX source maps | Build an observed dependency map from a minimal test before implementing broad subsystems. |
| E-011 | CellX2 itself has an independently tested PPU or SPU translator. | `UNVERIFIED` | No CellX2 execution result has been established in the current review. | Do not claim it until a CellX2-owned test runs and its artifacts are recorded. |
| E-012 | CellX2 has executed a real PS3 program or complete game. | `UNVERIFIED` | No such execution was established in the current review. | A small synthetic instruction/program test must precede real-program claims. |
| E-013 | PS3Recomp's current source tree and docs are completely consistent. | `UNVERIFIED` | Audit notes identify possible stale references and scope differences. | Review each item against its current implementation and a specific revision; do not assume an inconsistency is a defect. |

## Audit questions — not confirmed bugs

| ID | Question | Why it matters | Evidence needed |
|---|---|---|---|
| Q-001 | Does a malformed DMA submission leave memory unchanged and report failure consistently? | Data effects and completion state may differ. | A deterministic case with misaligned parameters, initialized destination bytes, and captured data/tag/error state. |
| Q-002 | What ordering is guaranteed for DMA completion, stalls, events and interrupts? | Data correctness alone may hide timing/order errors. | A documented event timeline and repeatable tests across the relevant state transitions. |
| Q-003 | What are the exact semantics of `fscrrd`/`fscrwr` and unsupported SPR operations in the inspected path? | Status state can affect subsequent branches or exceptions. | ISA rules and full before/after state assertions. |
| Q-004 | Which remaining `.word` entries are data, and which are unrecognized instructions? | Blindly lifting them risks false support. | Segment metadata, address/control-flow context, and independent disassembly evidence. |
| Q-005 | Which PS3Recomp SPU execution strategy is used by each documented test/title path? | Documentation describes multiple strategies and historical states. | Trace from test/entrypoint through dispatch and generated-code execution. |
| Q-006 | Are documentation references to older tool names or algorithms stale? | A stale procedure can produce an invalid reproduction. | Verify the referenced path against the pinned tree and update the ledger with a source link. |

## How to add a new entry

Copy this template and assign a stable ID:

| ID | Claim / question | Status | Source revision and exact path | Evidence or test artifact | Limitation | Next action |
|---|---|---|---|---|---|---|
| E-XXX |  | `UNVERIFIED` |  |  |  |  |

For every test result, record:

- Test ID and version/commit.
- Exact input bytes/state and expected state.
- Source of the expected answer (ISA section/page or independent oracle).
- Toolchain, host environment and command.
- Exit code and complete relevant output.
- SHA-256 of input, tools, configuration and output where practical.
- Whether the result was a clean run from newly built artifacts.
