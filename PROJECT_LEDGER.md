# CellX2 — Project Ledger

## 1. Project Objective

CellX2 investigates the feasibility of recompiling
PlayStation 3 software for execution on other platforms.

The research focuses on:
- PowerPC PPU instruction translation.
- SPU instruction translation.
- Runtime and operating system dependencies.
- Memory and execution semantics.
- Graphics, audio, and input dependencies.
- Cross-platform execution feasibility.

## 2. Evidence Classification

Every significant claim must use one of these categories.

### DOCUMENTED
Information found in an identified source.
This does not mean CellX2 independently verified it.

### INDEPENDENTLY TESTED
A test executed by the CellX2 team with recorded inputs
and outputs.

### SEMANTICALLY VERIFIED
An implementation was compared against an independent
reference or architectural specification.

### INTEGRATION VERIFIED
Multiple components were tested together in a reproducible
execution environment.

### UNVERIFIED
A hypothesis or claim that still requires evidence.

## 3. Current Project Status

Status: Initial research and organization.

Confirmed project work:
- Repository created.
- Initial README drafted.
- Research plan being established.

Not yet established:
- An independently tested PPU instruction translator.
- An independently tested SPU instruction translator.
- A working CellX2 runtime.
- Successful execution of a complete PS3 game.
- Compatibility with PlayStation 4.

## 4. Reference Projects

### PS3Recomp
Purpose: Primary reference for static recompilation
of PlayStation 3 software.

Status: DOCUMENTED.

Required work:
- Record the exact commit examined.
- Map existing components.
- Review available tests.
- Identify documented limitations.
- Reproduce selected tests where feasible.

### RPCS3
Purpose: Supporting reference for PS3 execution behavior.

Status: DOCUMENTED.

Required work:
- Identify relevant implementation files.
- Compare selected behaviors against independent
  architectural documentation.
- Record disagreements and unresolved questions.

### OpenOrbis PS4 Toolchain
Purpose: Reference for PS4 homebrew development
and target-platform constraints.

Status: DOCUMENTED.

Important limitation:
A PS4 homebrew toolchain is not itself a PS3
static recompiler.

## 5. Research Work Packages

### A — PPU
- Instruction semantics.
- Registers and condition state.
- Branches and function calls.
- Memory access and endianness.
- Floating-point and vector instructions.

### B — SPU
- Instruction decoding.
- Vector semantics.
- Local store.
- Channels and mailboxes.
- DMA and synchronization.

### C — Runtime
- Memory model.
- System calls.
- Threading and synchronization.
- Module loading.
- Host and guest ABI boundaries.

### D — Hardware-Dependent Subsystems
- RSX graphics.
- Audio.
- Input.
- Timing and synchronization.

### E — Target Platform
- Host operating system.
- Compiler and ABI.
- Runtime dependencies.
- PS4 feasibility assessment.

## 6. Current Milestones

- [x] Create repository.
- [x] Draft initial project description.
- [ ] Record reference repository commits.
- [ ] Build a component inventory.
- [ ] Define the first independent PPU tests.
- [ ] Execute and record the first reproducible test.
- [ ] Define initial SPU tests.
- [ ] Assess runtime dependencies.
- [ ] Evaluate target-platform feasibility.

## 7. Evidence Rules

Every test record should include:
- Test identifier.
- Date.
- Source revision.
- Input.
- Expected result.
- Actual result.
- Test environment.
- Pass or fail.
- Relevant logs.
- Known limitations.

A generated source file is not proof of semantic correctness.

A successful build is not proof of correct execution.

A successful startup is not proof that a complete game works.

## 8. Decision Log

No architectural decision is final until its rationale,
alternatives, and evidence have been recorded.

## 9. Current Conclusion

CellX2 is in the initial research phase.

No end-to-end game execution has been independently
verified by CellX2.

## Reference Baseline

- Project: ps3recomp
- Repository: https://github.com/sp00nznet/ps3recomp
- Reference commit: 39a36296511c445707adabcd312f0b740cfbd694
- Status: Reference identified; commit contents not yet independently audited.
- Purpose: Track upstream PPU/SPU recompilation tools, runtime requirements,
  supported platforms, and existing tests.
- CellX2 verification: No independent validation recorded yet.
- Next action: Inspect the reference commit and identify a small,
  reproducible test for CellX2.