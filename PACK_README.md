# CellX2 Research Pack

This README describes the five-file project-control pack prepared for the repository. It is not a complete inventory of every document in the repository.

## Project-control files

1. `PROJECT_STATUS.md` — current project boundary, truthful status, and immediate checkpoint.
2. `RESEARCH_LEDGER.md` — evidence classifications, pinned source revisions, claims, and unresolved questions.
3. `SPU_RESEARCH.md` — SPU source map, findings, and priority semantic/runtime questions.
4. `PPU_RESEARCH.md` — PPU source map, architectural-state concerns, and incremental research plan.
5. `TEST_PLAN.md` — test status definitions, record template, first SPU/PPU test slices, and integration gates.

## Related repository documents

The repository may also contain `README.md`, `PROJECT_LEDGER.md`, `TEST_STRATEGY.md`, architecture notes, reference-project analyses, and longer audit reports. These documents are related research records, not additional members of the five-file pack above. Keep overlapping status statements synchronized when making material changes.

## Maintenance rules

- Keep pinned source revisions and the date of review explicit.
- Update findings when the reviewed commits change.
- Preserve the distinction between documented upstream behavior and CellX2 test results.
- Do not mark a test as passed unless its inputs, expected results, actual outputs, environment, and execution evidence are recorded.
- Treat the component inventory as a review of principal paths plus broader inventories, not a complete line-by-line audit of every source file.

## Scope and limitations

The pack reflects research recorded on 2026-10-21. No CellX2 test is claimed to have run. The pack prepares and organizes research documents; its existence does not imply that code has been implemented or that any runtime path works.
