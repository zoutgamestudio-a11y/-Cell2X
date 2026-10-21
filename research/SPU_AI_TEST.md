# CellX2 — SPU AI Test Specification and Current Findings

**Date:** 2026-10-21  
**Test ID:** SPU-AI-SPEC-001  
**Specification self-check:** PASS (9/9 assertions)  
**CellX2 implementation execution:** NOT RUN / BLOCKED

## 1. What was checked

A small Python checker was run against the proposed first SPU test. It verifies the internal consistency of the raw opcode words, destination/source register fields, signed 10-bit immediate extraction, encode/decode round trips, and four-lane arithmetic expectations.

This is a **specification self-check**, not execution of CellX2's decoder, lifter, or runtime.

## 2. Reference source snapshots reviewed

- PS3Recomp: `749182eebb936f086a007f63e1c7d853f3cf708a`
  - `tools/spu_disasm.py`
  - `tools/spu_lifter.py`
  - `runtime/spu/spu_helpers.h`
  - `runtime/spu/spu_interp.c`
  - `runtime/spu/tests/test_spu_helpers.c`
- RPCS3: `4024ea31e049f3205ae406eb3f37fe7625e1bc98`
  - `rpcs3/Emu/Cell/SPUOpcodes.h`
  - relevant SPU interpreter/disassembler paths

The two projects are comparison references. Their tests and implementations are not CellX2 results, and agreement between them alone is not independent proof of architectural correctness.

## 3. Proposed instruction vectors

Instruction: SPU `AI` (Add Word Immediate), adding a sign-extended 10-bit immediate to each 32-bit word lane. Results are represented modulo 2^32.

Initial source register `r5`:

`[0x00000010, 0x7FFFFFFF, 0xFFFFFFFC, 0x00000000]`

| Assembly | Raw instruction word | Expected destination `r3` |
|---|---:|---|
| `ai $r3, $r5, 7` | `0x1C01C283` | `[0x00000017, 0x80000006, 0x00000003, 0x00000007]` |
| `ai $r3, $r5, -3` | `0x1CFF4283` | `[0x0000000D, 0x7FFFFFFC, 0xFFFFFFF9, 0xFFFFFFFD]` |

## 4. Self-check output

Nine assertions passed:

1. Decode the +7 raw word.
2. Decode the -3 raw word and sign extension.
3. Encode/decode round trip for +7.
4. Encode/decode round trip for -3.
5. Four-lane +7 expected vector.
6. Four-lane -3 expected vector.
7. Input source state is treated as input-only by the arithmetic model.
8. Positive overflow representation modulo 2^32.
9. Negative result representation modulo 2^32.

## 5. Evidence classification

- The raw-word and expected-result consistency is **analytically checked by this standalone specification checker**.
- Under the project's existing ledger, do not silently reclassify this as `INDEPENDENTLY TESTED`: the checker is not the CellX2 implementation and the architectural expectation still needs traceable ISA-manual citations.
- The CellX2 implementation-level test remains **NOT RUN / BLOCKED** because the inspected project files currently document plans and research rather than providing a runnable CellX2 SPU decoder/executor.
- This work does not establish a functioning SPU translator, runtime, or execution of any PS3 program.

## 6. Required next steps

1. Locate or implement a CellX2-owned executable decoder/harness.
2. Run both raw words through that implementation and record decoded fields.
3. Execute the instruction against a four-word architectural register state.
4. Capture actual before/after state, environment, source revision, command, and exit code.
5. Compare results with the SPU ISA manual and use RPCS3 as a secondary cross-check.
6. Only then record a CellX2 implementation test result.

## 7. Broader SPU audit conclusions still open

The earlier source review identified questions worth targeted tests, not confirmed defects:
- Whether invalid DMA submissions leave memory and completion/error state consistent.
- Whether effective-address high bits are rejected or intentionally unsupported.
- Whether synchronous DMA completion accurately models the behaviors required by relevant software.
- Whether status/special-register operations are fully modeled on the inspected paths.
- Whether documentation coverage counts distinguish decoder dispatch from semantic correctness.
- Whether title-specific diagnostic code is separated clearly from general runtime behavior.

Each needs an exact path/revision, architecture-backed expected behavior, and a reproducible test before being promoted from an audit question to a confirmed defect.

## 8. Links to pinned references

- PS3Recomp SPU disassembler: https://github.com/sp00nznet/ps3recomp/blob/749182eebb936f086a007f63e1c7d853f3cf708a/tools/spu_disasm.py
- PS3Recomp SPU lifter: https://github.com/sp00nznet/ps3recomp/blob/749182eebb936f086a007f63e1c7d853f3cf708a/tools/spu_lifter.py
- PS3Recomp SPU helpers: https://github.com/sp00nznet/ps3recomp/blob/749182eebb936f086a007f63e1c7d853f3cf708a/runtime/spu/spu_helpers.h
- PS3Recomp SPU helper tests: https://github.com/sp00nznet/ps3recomp/blob/749182eebb936f086a007f63e1c7d853f3cf708a/runtime/spu/tests/test_spu_helpers.c
- RPCS3 SPU opcode table: https://github.com/RPCS3/rpcs3/blob/4024ea31e049f3205ae406eb3f37fe7625e1bc98/rpcs3/Emu/Cell/SPUOpcodes.h
