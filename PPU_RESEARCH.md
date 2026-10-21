# CellX2 — PPU Research Notes

**Status:** initial source map and validation plan; no CellX2 PPU test is claimed to have run.  
**Primary source snapshot:** PS3Recomp `749182eebb936f086a007f63e1c7d853f3cf708a`  
**Supporting source snapshot:** RPCS3 `4024ea31e049f3205ae406eb3f37fe7625e1bc98`

## 1. Research objective

Build an accurate, incremental model of PowerPC PPU instruction behavior and architectural state before attempting broad translation. Tests must compare the full guest-visible state affected by an instruction, not only the destination register.

## 2. Source map

### PS3Recomp paths identified in the review

- `tools/ppu_disasm.py` — PPU instruction disassembly.
- `tools/ppu_lifter.py` — instruction-to-host-code lifting.
- `tools/ppu_loader.py` — program/ELF loading path.
- `runtime/ppu/ppu_loader.cpp` — runtime loader implementation.
- `runtime/ppu/ppu_context.h` — PPU execution context/state.
- `docs/PPU_RECOMP.md` — project documentation and sample-specific coverage claims.

### RPCS3 paths identified as useful references

- `rpcs3/Emu/Cell/PPUOpcodes.h` — instruction encodings/table.
- `rpcs3/Emu/Cell/PPUInterpreter.cpp` — interpreted instruction semantics.
- `rpcs3/Emu/Cell/PPUTranslator.cpp` — translation/lowering.
- `rpcs3/Emu/Cell/PPUThread.cpp` — thread state and execution integration.
- `rpcs3/Emu/Cell/PPUModule.cpp` and `PPUFunction.cpp` — module/function handling.
- `rpcs3/Emu/Memory/vm.cpp` — guest memory model.

## 3. Current findings

### 3.1 Architectural state extends beyond the result register

Depending on the instruction, PPU behavior may include updates to:

- General-purpose and floating-point registers.
- Condition Register (CR) fields.
- XER carry, overflow and summary-overflow bits.
- Link Register (LR) and Count Register (CTR).
- FPSCR status and control state.
- Reservation state for load-reserve/store-conditional operations.
- Memory and ordering effects.
- VMX/vector state, including VSCR where applicable.

A test that checks only the apparent result register can pass despite incorrect state needed by later instructions.

### 3.2 Unsupported operations must not silently count as supported

The reviewed `tools/ppu_lifter.py` contains cases where unsupported SPR behavior can be represented as a comment plus a no-op. That may allow generated host code to compile, but it does not prove that the guest program's behavior is preserved if that operation executes.

CellX2 should classify operations explicitly, for example `IMPLEMENTED`, `PARTIAL`, `UNSUPPORTED`, or `UNKNOWN`. An unsupported operation should fail a conformance test or stop generation under strict mode rather than silently passing.

### 3.3 Coverage figures are sample-specific

The reviewed `docs/PPU_RECOMP.md` reports approximately 99.8% ISA coverage on a particular sample. That is not a global PPU conformance figure. The document also describes a generic first-boot milestone at `sys_initialize_tls`, while other project materials describe title-specific progress. Those claims may cover different test scopes; reconcile the exact test and runtime path before drawing a global conclusion.

### 3.4 Floating-point status requires separate treatment

The reviewed lifter notes incomplete FPSCR status updates for some floating-point operations. Numeric output equality alone will therefore not establish full architectural equivalence where later instructions inspect status/control state.

## 4. Suggested implementation-independent test order

1. **Integer primitives:** add/subtract/logical operations and immediate sign extension.
2. **Record and condition state:** operations that update CR/XER; verify all affected fields.
3. **Control flow:** direct and conditional branches, branch-and-link, indirect branches, LR/CTR effects.
4. **Memory:** load/store widths, endianness, sign extension, alignment and boundary addresses.
5. **Reservation operations:** `lwarx`/`stwcx.` and relevant success/failure state, using an explicitly documented memory model.
6. **Floating point:** finite values first, then exceptional/boundary behavior and FPSCR.
7. **VMX/vector:** lane order, saturation/rounding and VSCR behavior as scoped by ISA requirements.

The order can change if a minimal real sample demands another instruction, but any such change should be recorded in the ledger.

## 5. Proposed test record

For every PPU test, record:

- Test ID and tested instruction/form.
- Raw 32-bit word and expected decoded fields.
- Initial GPR/FPR/CR/XER/LR/CTR/FPSCR/reservation state as relevant.
- Memory bytes and endian interpretation when relevant.
- ISA reference for the expected result and state effects.
- Resulting full relevant state, not just one output value.
- Whether the same case was checked against RPCS3 and the precise path used.
- Toolchain, command, environment, exit code and output when executed.

## 6. Evidence table

| Topic | Current status | Next action |
|---|---|---|
| PPU decoder/lifter exists in PS3Recomp | `DOCUMENTED` | Pin specific examples and test encodings/operands independently |
| CR/XER effects in CellX2 | `UNVERIFIED` | Define state model and begin with integer instructions that update these fields |
| Branch/link semantics in CellX2 | `UNVERIFIED` | Test PC/LR/CTR and conditional state transitions |
| Load/store and guest memory semantics | `UNVERIFIED` | Specify endian, alignment, sign-extension and address-boundary tests |
| Reservation/memory ordering | `UNVERIFIED` | Use a documented concurrency model and explicit success/failure cases |
| Floating-point status equivalence | `UNVERIFIED` | Test FPSCR independently from numerical register results |
| VMX/VSCR equivalence | `UNVERIFIED` | Defer broad coverage until the foundational state tests pass |

## 7. Completion gate for a first PPU slice

A slice is ready to be considered tested only when each chosen instruction has:

- A known encoding with expected operand fields.
- An ISA-based expected result and state delta.
- Assertions for every relevant architectural state component.
- Tests for the principal boundary or alias conditions applicable to that instruction.
- A captured run against fresh artifacts, including test revision, environment and exit code.

**Current CellX2 result:** not run; this document records a research plan only.
