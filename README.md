# CellX2

### From Cell to Cross-Platform

CellX2 is an independent research project investigating PlayStation 3 software recompilation, Cell architecture translation, and the conditions required for correct execution.

The current phase focuses on understanding the PlayStation 3 PPU and SPU architectures, auditing existing open-source references, and establishing reproducible methods for validating instruction semantics.

## Project Goals

- Study the Cell Broadband Engine architecture.
- Investigate PowerPC PPU and SPU instruction semantics and translation.
- Research operating-system services and runtime requirements.
- Examine graphics, audio, input, synchronization, and lifecycle dependencies.
- Define small, reproducible tests for instruction correctness.
- Establish a minimal, verifiable execution path before making broader feasibility claims.

## Research Principles

- Correctness must be demonstrated through reproducible tests, not assumptions.
- Existing implementations are references, not unquestionable truth.
- Reference-project results must never be presented as CellX2 results.
- Source revisions, test inputs, expected outputs, and actual results must be recorded.
- Unsupported or unresolved behavior must remain explicit.
- Third-party code and documentation must be used in accordance with their licenses and applicable law.

## Current Status

**Phase:** Initial research and project organization.

The project has research notes and test specifications, but no independently executed CellX2 instruction test or end-to-end execution result is recorded yet. No successful execution of a complete commercial PlayStation 3 game has been established by CellX2.

## Reference Projects

- [PS3Recomp](https://github.com/sp00nznet/ps3recomp)
- [RPCS3](https://github.com/RPCS3/rpcs3)

These are independent reference projects. CellX2 does not claim affiliation with or endorsement by their maintainers.

## Legal and Licensing Notes

CellX2 aims to develop original research, tools, and tests. Third-party software and documentation remain subject to their respective licenses and applicable law. This repository does not intend to distribute commercial game files or proprietary game assets without authorization.

## Roadmap

- [x] Establish an initial research baseline.
- [x] Record pinned reference project versions and commits.
- [x] Document the initial PPU and SPU research status.
- [x] Draft initial instruction-level test specifications.
- [ ] Complete ISA-backed expected vectors for the first SPU tests.
- [ ] Execute and record the first reproducible instruction-level test.
- [ ] Map runtime and system-service dependencies from a minimal test.
- [ ] Build and verify a small synthetic program before considering larger execution goals.

## Project Identity

**Project:** CellX2  
**Studio identity:** ZoutGameStudio  
**Status:** Research and development — no CellX2 instruction test has yet been recorded as executed.
