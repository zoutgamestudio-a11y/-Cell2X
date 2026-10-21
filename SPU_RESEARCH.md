# CellX2 — SPU Research Notes

**Status:** research and test specification only; no CellX2 SPU test is claimed to have run.  
**Primary source snapshot:** PS3Recomp `749182eebb936f086a007f63e1c7d853f3cf708a`  
**Supporting source snapshot:** RPCS3 `4024ea31e049f3205ae406eb3f37fe7625e1bc98`

## 1. Research objective

Establish a small, testable SPU semantic slice that separates instruction decoding, code generation, architectural effects, and runtime integration. The first goal is not broad coverage; it is a trustworthy test method that can detect a known wrong decode or semantic implementation.

## 2. Source map

### PS3Recomp paths examined in the research review

- `tools/spu_disasm.py` — instruction decoding/disassembly.
- `tools/spu_lifter.py` — lifting SPU instructions to host code.
- `runtime/spu/spu_helpers.h` — shared semantic helpers, including floating-point helpers.
- `runtime/spu/spu_context.h` — SPU execution context/state.
- `runtime/spu/spu_dma.h` — MFC/DMA behavior.
- `runtime/spu/spu_channels.c` — channel behavior.
- `runtime/spu/spu_interp.c` and `runtime/spu/spu_interp_tables.inc` — interpreter paths.
- `runtime/spu/spu_coherency.c`, `runtime/spu/spu_drain.c` — related runtime handling.
- `tools/spu_program_pipeline.py` and `tools/test_spu_program_pipeline.py` — generation, provenance, and failure handling.
- `docs/SPU_LIFTER.md`, `docs/SPU_FALLBACK.md`, `docs/SPU_CONTEXT_REGISTRIES.md`, `docs/SPU_INTERPRETER_LIFTED_HANDOFF.md`, `docs/SPURS_SCHEDULING.md` — explanatory material.
- `runtime/spu/tests/` and `tests/test_spu_fnms_zero_extended.py` — focused and integration test source.

### RPCS3 paths examined or identified as relevant

- `rpcs3/Emu/Cell/SPUOpcodes.h` — opcode encoding/table.
- `rpcs3/Emu/Cell/SPUInterpreter.cpp` — interpreted behavior.
- `rpcs3/Emu/Cell/SPUThread.cpp` and `.h` — execution state and lifecycle.
- `rpcs3/Emu/Cell/SPUCommonRecompiler.cpp`.
- `rpcs3/Emu/Cell/SPUASMJITRecompiler.cpp`.
- `rpcs3/Emu/Cell/SPULLVMRecompiler.cpp`.
- `rpcs3/Emu/Cell/MFC.cpp` — MFC-related behavior.

**Scope limitation:** this was a deep review of principal paths plus a broad source inventory, not a complete line-by-line validation of every file or generated case.

## 3. Core findings

### 3.1 Decode, lift, and semantics are separate gates

A valid host-language output only proves that code generation produced something the host compiler accepted. It does not prove that the opcode, operands, register fields, immediates, lane order or state effects were correct.

CellX2 must validate separately:

1. Raw 32-bit instruction → expected mnemonic and decoded operands.
2. Decoded instruction → generated host expression or instruction representation.
3. Initial architectural state + instruction → expected final architectural state.
4. When applicable, interpreter and lifted paths → equivalent guest-visible state.

A cross-check with RPCS3 is useful, but the architectural ISA reference should be the independent authority for selected semantic tests to avoid circular validation.

### 3.2 Decoder coverage is not instruction-set conformance

The reviewed PS3Recomp documentation reports that the mnemonics emitted by its decoder for one Uncharted SPU sample had lifter coverage, while 683 words remained unclassified as `.word`. This is evidence about one sample and one decoder/lifter relationship only. It does not show that all words are instructions or that all generated semantics are correct.

Do not force all `.word` entries through the lifter just to make a coverage number look better. Retain an explicit `UNKNOWN` or `UNSUPPORTED` state until each item has evidence.

### 3.3 Lane order and host endianness require asymmetric data

SPU values can be represented in host-native scalar/vector types while helper functions apply SPU byte-order conversions. Symmetric vectors may conceal a lane reversal or byte-selection defect.

Use test values with different bytes and different word/halfword lanes. State the exact byte layout in the test record, and define whether each expectation is expressed as a byte array or integer lane values.

### 3.4 FNMS is a high-value early test

The architectural operation is `RC - (RA × RB)` with SPU-specific extended-range and saturation/underflow behavior. Do not use the host's default fused floating-point operation as the sole semantic definition.

The reviewed PS3Recomp code has a dedicated FNMS branch in the lifter rather than handling it through the `rr_bin` dictionary. The shared helper currently contains a custom representation-aware SPU floating-point path (`spu__sf_split`, `spu__sf_pack`, `spu__fma_lane`, and related fast paths). A design note about a narrower historical workaround may not fully describe the current implementation; read the pinned helper source.

The reference test source constructs synthetic opcodes, routes them through decoder/lifter code and checks compiled results. Its documented 449 input cases and 16,164 assertions are reference-project results; CellX2 has not independently run them.

### 3.5 Explicit open questions

The reviewed lifter documentation records unresolved or qualified behavior around:

- `SHLQBY` direction under its host representation.
- Which halfword is selected by `BRHZ` and `BRHNZ` in the relevant representation.
- Partial treatment of `FSCRRD` / `FSCRWR` and floating-point status.
- Default handling for some unsupported or unrecognized channel operations.
- The separation between manual SPU fallback and automated lifter/interpreter test paths.

Treat these as questions to resolve, not proof that the implementation is wrong. Use the SPU ISA manual first and RPCS3 as an additional comparison.

## 4. Runtime areas: not just arithmetic

The SPU execution contract includes more than a register array:

- 128-bit registers and the local store.
- PC, branch/link behavior and stop state.
- Channels, mailboxes and blocking/wakeup rules.
- MFC commands, DMA lists, tags, stalls, notification, and completion ordering.
- Reservation/atomic effects where implemented by the runtime model.
- Events, interrupts and SPU lifecycle.
- SPURS policy/workload/job orchestration and image loading.

A small arithmetic instruction passing does not validate the runtime. A translated SPU program can still fail because local-store setup, a mailbox, DMA ordering, a tag state transition, event delivery or job lifecycle differs.

## 5. High-priority questions to formalize

### SPU-Q-01 — `SHLQBY` / `SHLQBYI`

Create distinct-byte input such as a sequence where every byte differs. Test shift amounts `0`, `1`, `15`, `16`, and `17` (where the encoding and instruction variant allow the value). Record the ISA-defined result bytes and verify zero-fill and movement direction.

### SPU-Q-02 — `BRHZ` / `BRHNZ`

Use a register with four different halfwords so each candidate halfword produces a distinguishable zero/nonzero result. Test both branch-taken and branch-not-taken cases and record the final PC/link state required by the instruction.

### SPU-Q-03 — `FNMS`

Cover ordinary finite controls, zero operands, sign combinations, aliasing of destination with each source, and SPU range-boundary cases from the ISA. Compare all relevant result lanes, not merely one scalar lane.

### SPU-Q-04 — MFC/DMA malformed transfers

Prepare a destination initialized to a recognizable byte pattern. For a malformed or misaligned request, observe data modification, tag status, error state and notification separately. An audit note indicates some rejection paths may still interact with completion handling; this is a question requiring a test, not a confirmed defect.

### SPU-Q-05 — `FSCRRD` / `FSCRWR` and special registers

Make an explicit table for each selected operation: input state, read value, side effects, exception/status behavior and support classification. Distinguish fully implemented behavior from documented stubs.

## 6. Evidence table

| Topic | Current status | Required next evidence |
|---|---|---|
| Decoder opcode/operand fields | `DOCUMENTED` in reference code | Golden raw-word vectors checked against ISA encoding |
| Selected lifter branches | `DOCUMENTED` in reference code | Generated-output inspection and output-state assertions |
| FNMS helper/test path | `DOCUMENTED` in reference code | Independent ISA-derived vectors and captured CellX2 run |
| `SHLQBY` semantics | `UNVERIFIED` for CellX2 | Asymmetric byte vectors and an ISA-backed expected result |
| `BRHZ` / `BRHNZ` semantics | `UNVERIFIED` for CellX2 | Distinct-halfword vectors, expected branch state and captured run |
| DMA malformed-input behavior | Audit question; `UNVERIFIED` | Capture memory/tag/error effects with reproducible parameters |
| SPURS lifecycle | `DOCUMENTED` as a complex reference subsystem | Small lifecycle integration test after instruction-level gates |

## 7. Proposed completion gate for the first SPU slice

Do not call this slice complete until:

- Every test records the raw opcode and decoded operands.
- Expected behavior cites the applicable ISA rule/page or a clearly identified independent source.
- Result assertions cover all architecturally relevant state for the selected instruction.
- Inputs expose lane order, sign, immediate, aliasing and boundary errors where relevant.
- A deliberately wrong decode or semantic helper makes at least one test fail.
- The test starts from a fresh build and its output and tool/input revisions are saved.

**Current CellX2 result:** not run; specification/research only.
