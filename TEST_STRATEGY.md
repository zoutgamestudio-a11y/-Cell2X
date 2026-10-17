# CellX2 — Test Strategy

## 1. Objective

Establish a reproducible method for validating
instruction translation and runtime behavior.

Tests must detect semantic errors rather than merely
confirm that generated code compiles.

## 2. Testing Layers

### Layer 1 — Instruction-Level Tests

Test individual instructions with controlled inputs.

Examples:
- Integer addition.
- Integer subtraction.
- Logical operations.
- Comparisons.
- Conditional branches.
- Loads and stores.
- Register updates.

Each test must define its expected output.

### Layer 2 — State-Transition Tests

Verify changes to:
- General-purpose registers.
- Condition registers.
- Link register.
- Count register.
- Memory.

Tests must cover relevant edge cases.

### Layer 3 — Translation Tests

For each test program:
1. Define the original instruction sequence.
2. Record the expected architectural result.
3. Translate the program.
4. Compile the generated code.
5. Execute it in a controlled test environment.
6. Compare the resulting state.

Compilation success alone is insufficient.

### Layer 4 — Runtime Tests

Test:
- Memory allocation and access.
- Function calls and returns.
- Guest-to-host transitions.
- Error handling.
- Required runtime services.

### Layer 5 — Integration Tests

Combine previously tested components.

Integration failures must be distinguished from
instruction-level failures.

## 3. Reference Selection

Use architectural specifications and independent
implementations where available.

RPCS3 may serve as a behavioral reference, but agreement
with one implementation does not independently prove
correctness.

Disagreements must be documented and investigated.

## 4. Test Record Format

Every test record must include:

- Test ID
- Test name
- Architecture or subsystem
- Source revision
- Input state
- Expected output state
- Actual output state
- Environment
- Result
- Logs
- Known limitations

## 5. Result Categories

PASS:
Observed behavior matches the defined expected behavior.

FAIL:
Observed behavior differs from the expected behavior.

BLOCKED:
The test could not run because a required component
or environment was unavailable.

INCONCLUSIVE:
Available evidence is insufficient to determine correctness.

NOT RUN:
The test has been designed but not executed.

## 6. Initial Test Plan

### PPU-001
Purpose: Validate a basic integer operation.

Status: NOT RUN.

### PPU-002
Purpose: Validate a conditional branch.

Status: NOT RUN.

### PPU-003
Purpose: Validate a load/store sequence.

Status: NOT RUN.

### PPU-004
Purpose: Validate a function call and return.

Status: NOT RUN.

### SPU-001
Purpose: Establish a basic SPU instruction test.

Status: NOT RUN.

### RT-001
Purpose: Validate a minimal runtime memory operation.

Status: NOT RUN.

## 7. Regression Testing

Every corrected defect should produce a test that
fails before the fix and passes after the fix.

Previously passing tests must be rerun after changes
that may affect their behavior.

## 8. Completion Criteria

A test is not complete until its inputs, expected
results, actual results, and execution environment
have been recorded.

A subsystem is not considered verified merely because
its source code exists.