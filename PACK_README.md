# CellX2 Research Pack

This pack contains five project-control documents intended to be copied into the root of the CellX2 repository:

1. `PROJECT_STATUS.md` — current project boundary, truthful status and immediate checkpoint.
2. `RESEARCH_LEDGER.md` — evidence classifications, pinned source revisions, claims and unresolved questions.
3. `SPU_RESEARCH.md` — SPU source map, findings and highest-priority semantic/runtime questions.
4. `PPU_RESEARCH.md` — PPU source map, architectural-state concerns and incremental research plan.
5. `TEST_PLAN.md` — test status definitions, record template, first SPU/PPU slices and integration gates.

## How to use it

- Copy the five `.md` files into the repository root.
- Keep the filenames stable so internal Markdown links and future notes remain easy to maintain.
- When the source revisions change, update the pinned commits and revisit findings affected by the changes.
- Update status only when new evidence exists. A test specification is not a test result.

## Scope and limitations

The pack reflects research performed on 2026-10-21 using pinned PS3Recomp and RPCS3 snapshots. It records a deep review of principal source paths plus broader inventories; it does not claim that every line of either repository has been manually audited. No CellX2 test is reported as run. The pack does not modify or commit anything to GitHub; it prepares files for upload.
