# CellX2 — Initial Test Plan

**Revision:** 2026-10-21  
**Current execution state:** specification only; no tests in this document have been run by CellX2.

## 1. Purpose

Establish a compact conformance process for selected PPU/SPU instructions and build a path toward a minimal synthetic program. The first objective is test quality and traceability, not a large instruction-count claim.

## 2. Test status vocabulary

- `SPECIFIED` — inputs, expected state, and pass/fail criteria have been written.
- `IMPLEMENTED` — a test harness exists, but it has not necessarily been run.
- `RUN-PASS` — run from fresh artifacts and passed; output and environment recorded.
- `RUN-FAIL` — executed and failed; preserve output and treat it as useful evidence.
- `BLOCKED` — cannot run because an explicit dependency/environment is missing.
- `SUPERSEDED` — replaced by a newer test; preserve the earlier result for provenance.

Do not mark a test `RUN-PASS` based on source inspection, compilation claims from a reference project, or an old binary left from a failed build.

## 3. Test record template

Copy this block for every test and give it a stable ID.

```text
Test ID:
Component: PPU / SPU / runtime / pipeline
Status: SPECIFIED / IMPLEMENTED / RUN-PASS / RUN-FAIL / BLOCKED / SUPERSEDED
Test version or commit:
Instruction(s) / subsystem:
Raw input bytes or opcode:
Initial architectural state:
Expected decoded fields:
Expected final architectural state:
Source of expected behavior (ISA title/version/section/page):
Secondary comparison source and exact revision/path:
Build command:
Execution command:
Host environment / compiler:
Exit code:
Relevant output:
Input SHA-256:
Tool/config SHA-256:
Output SHA-256:
Notes / limitations:
```

## 4. Phase A — decoder tests

For each selected instruction, independently validate its raw opcode and operand fields before validating execution semantics.

**Required assertions:**

- Exact mnemonic/opcode identity.
- Destination and source register indices.
- Immediate/shift/channel fields and sign-extension rules.
- Instruction format and reserved/ignored bits as defined by the ISA.
- Correct behavior on more than one encoding where the format allows it.

**Failure condition:** any field differs from the ISA-derived expected decode, even if generated code compiles.

## 5. Phase B — first SPU semantic slice

### SPU-T-001 — `FNMS`

**Status:** `SPECIFIED` (expected results still need to be filled from the pinned ISA reference for each vector).  
**Goal:** validate the operation `RC - (RA × RB)` and SPU-specific floating-point range handling.

Vector classes:

- Ordinary finite control case.
- Zero input/product cases.
- Positive and negative operand combinations.
- Destination aliasing each source register in separate test cases.
- Selected underflow/overflow or extended-range cases defined by the ISA.
- Check every result lane and any relevant status state that the implementation claims to support.

**Pass criterion:** decoded fields and all expected result lanes match the ISA-derived vectors. Any untested FPSCR/status behavior must remain documented as outside this test's claim.

### SPU-T-002 — `SHLQBY` / `SHLQBYI`

**Status:** `SPECIFIED` (expected bytes and exact legal shift encodings need to be recorded).  
**Goal:** validate byte movement direction, lane/byte representation and zero-fill.

Use an input with distinct bytes, such as `00 11 22 33 44 55 66 77 88 99 AA BB CC DD EE FF`; record clearly whether the printed order represents low-to-high memory addresses or architectural byte order. Test shift amounts `0`, `1`, `15`, `16`, and `17` only where permitted by the exact instruction/encoding.

**Pass criterion:** all 16 output bytes match the architecture-derived expected vector.

### SPU-T-003 — `BRHZ` / `BRHNZ`

**Status:** `SPECIFIED` (ISA-derived preferred-halfword rule and exact vectors remain to be entered).  
**Goal:** test the relevant halfword selection plus branch-taken/not-taken behavior.

Use a register containing four different halfwords, then create cases where the architecturally selected halfword is zero and nonzero while other halfwords differ. Capture the relevant PC and any other state specified by the instruction.

**Pass criterion:** selected-halfword behavior and control-flow result match the ISA-derived expected state.

### SPU-T-004 — MFC/DMA basic behavior

**Status:** `SPECIFIED` (requires a deterministic runtime harness before execution).  
**Goal:** distinguish data movement from completion/error state.

Start with a valid aligned GET/PUT request and a recognizable destination/source pattern. Later cases should separately test malformed alignment/range inputs, list stall, resume and tag transitions.

Record independently:

- Bytes transferred or unchanged.
- Tag completion state.
- Error/rejection state.
- Event/notification effects, if the test harness includes them.

**Pass criterion:** data effects and status transitions each match the documented architectural/runtime contract. Do not infer success from tag completion alone.

## 6. Phase C — first PPU semantic slice

After SPU vectors and ledger rules are stable, select a small sequence with:

1. Integer arithmetic/immediate sign extension.
2. An operation affecting CR/XER.
3. A direct or conditional branch; include link behavior only where relevant.
4. A load/store with a fixed, documented byte layout.

For every instruction, compare the full affected state. Do not begin with a large executable whose runtime requirements make failures difficult to isolate.

## 7. Phase D — cross-path equivalence

When both an interpreter and a lifter exist, use the same raw instruction and initial state for each path.

Compare:

- General/vector registers that the instruction can affect.
- PC, branch/link state and stop state.
- Local store or guest memory effects.
- CR/XER/FPSCR/VSCR or channel/tag state when relevant.
- Exceptions, errors and control-transfer behavior.

An oracle comparison is supporting evidence, not a substitute for independently specified semantics. For floating-point edge cases, explicitly identify which ISA rule is used to resolve disagreement.

## 8. Phase E — minimal integration program

Build one tiny synthetic program/image with predictable behavior and minimal dependencies. The end-to-end path should be explicit:

`input bytes/image → loader/decoder → lifted code → fresh native build → execution → state/output comparison`

Record every intermediate artifact and fail the run if generation or compilation fails. Never execute a stale output after a failed build.

**Completion gate:** the program passes repeatedly from clean builds and the expected output is independently defined. This is a first integration result only, not proof of broad game compatibility.

## 9. Failure-closed pipeline and provenance

Before accepting a generated result:

- Reject unsupported instructions or unresolved instruction targets in strict mode.
- Reject overlapping/ambiguous executable input ranges unless explicitly resolved.
- Ensure test outputs correspond to the current input/source/tool versions.
- Record SHA-256 for input, tool source/configuration, generated source/binary and report where practical.
- Publish the result only after all required steps succeed.
- Report `UNSUPPORTED`, `BLOCKED`, or `FAIL`; never substitute an empty implementation and mark it successful without an explicit documented compatibility rule.

## 10. Priority order

1. Finish ISA-backed vectors for `FNMS`, `SHLQBY`/`SHLQBYI`, and `BRHZ`/`BRHNZ`.
2. Define a small PPU integer/branch/state test slice.
3. Design the smallest repeatable build-and-run harness.
4. Add a minimal integration program.
5. Expand to channels/DMA/events and PPU runtime dependencies only when the test program requires them.

## 11. Current limitations

- No CellX2 runtime execution has been recorded in this plan.
- Host compiler/toolchain and test environment are not yet recorded for any CellX2 test.
- Expected byte-level outputs for several proposed vectors still need to be filled in from the exact ISA rules before implementation.
- Reference-project tests and CI results must remain attributed to their original projects.
