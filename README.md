# CellX2

### From Cell to Cross-Platform

CellX2 is an independent research project exploring PlayStation 3
game recompilation, Cell architecture translation, and the feasibility
of cross-platform execution.

The initial focus is understanding the PlayStation 3 PPU and SPU
architectures, studying existing open-source projects, and establishing
reproducible methods for validating recompilation correctness.

## Project Goals

- Study the Cell Broadband Engine architecture.
- Investigate PowerPC PPU and SPU instruction translation.
- Research operating system services and runtime requirements.
- Examine graphics, audio, and input dependencies.
- Develop small, reproducible tests for instruction correctness.
- Evaluate the feasibility of running recompiled software on different
  platforms, including PC and potentially PlayStation 4.

## Research Principles

- Correctness must be demonstrated through tests, not assumptions.
- Existing implementations are references, not unquestionable truth.
- Source code, test results, and conclusions must be documented.
- Research findings must distinguish verified results from hypotheses.
- Third-party code must be used in accordance with its license.

## Current Status

**Phase:** Initial research and project organization.

No successful end-to-end execution of a commercial PlayStation 3 game
has been established by this project.

## Reference Projects

- [PS3Recomp](https://github.com/sp00nznet/ps3recomp)
- [RPCS3](https://github.com/RPCS3/rpcs3)
- [OpenOrbis PS4 Toolchain](https://github.com/OpenOrbis/OpenOrbis-PS4-Toolchain)

These projects are independent references. CellX2 does not claim
affiliation with or endorsement by their maintainers.

## Legal and Licensing Notes

CellX2 aims to develop original research, tools, and tests.
Third-party software and documentation remain subject to their
respective licenses and applicable law.

This repository does not intend to distribute commercial game files
or proprietary game assets without authorization.

## Roadmap

- [ ] Establish the research baseline.
- [ ] Record reference project versions and commits.
- [ ] Document PPU and SPU implementation status.
- [ ] Define reproducible instruction-level tests.
- [ ] Evaluate runtime and system-service dependencies.
- [ ] Test a small program before attempting a full game.
- [ ] Assess cross-platform execution feasibility.

## Project Identity

**Project:** CellX2  
**Studio identity:** ZoutGameStudio  
**Status:** Research and development