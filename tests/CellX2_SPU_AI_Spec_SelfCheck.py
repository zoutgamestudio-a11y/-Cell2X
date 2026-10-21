#!/usr/bin/env python3
"""CellX2 SPU AI specification self-check.
Checks raw-word fields and expected arithmetic, not the CellX2 implementation.
"""
from dataclasses import dataclass

MASK32 = 0xFFFFFFFF
OPCODE_AI = 0x1C

@dataclass(frozen=True)
class DecodedAI:
    rt: int
    ra: int
    immediate: int

def decode_ai(word: int) -> DecodedAI:
    if not 0 <= word <= MASK32:
        raise ValueError("instruction word must be a 32-bit unsigned value")
    opcode = (word >> 24) & 0xFF
    if opcode != OPCODE_AI:
        raise ValueError(f"unexpected opcode byte: {opcode:#04x}")
    raw_imm = (word >> 14) & 0x3FF
    signed_imm = raw_imm - 0x400 if raw_imm & 0x200 else raw_imm
    return DecodedAI(rt=word & 0x7F, ra=(word >> 7) & 0x7F, immediate=signed_imm)

def encode_ai(rt: int, ra: int, immediate: int) -> int:
    if not (0 <= rt < 128 and 0 <= ra < 128):
        raise ValueError("register indices must be in range 0..127")
    if not (-512 <= immediate <= 511):
        raise ValueError("AI immediate must fit signed 10-bit range")
    return (OPCODE_AI << 24) | ((immediate & 0x3FF) << 14) | (ra << 7) | rt

def ai_lane_model(lanes, immediate):
    return tuple((lane + immediate) & MASK32 for lane in lanes)

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    print(f"PASS: {name}")

def main():
    source = (0x00000010, 0x7FFFFFFF, 0xFFFFFFFC, 0x00000000)
    plus7, minus3 = 0x1C01C283, 0x1CFF4283
    d7, dm3 = decode_ai(plus7), decode_ai(minus3)
    check("decode +7 raw word", d7 == DecodedAI(3, 5, 7))
    check("decode -3 raw word and sign extension", dm3 == DecodedAI(3, 5, -3))
    check("encode +7 round-trip", encode_ai(3, 5, 7) == plus7)
    check("encode -3 round-trip", encode_ai(3, 5, -3) == minus3)
    expected7 = (0x00000017, 0x80000006, 0x00000003, 0x00000007)
    expectedm3 = (0x0000000D, 0x7FFFFFFC, 0xFFFFFFF9, 0xFFFFFFFD)
    actual7 = ai_lane_model(source, d7.immediate)
    actualm3 = ai_lane_model(source, dm3.immediate)
    check("AI +7 four-lane vector", actual7 == expected7)
    check("AI -3 four-lane vector", actualm3 == expectedm3)
    check("source state remains unchanged in pure model", source == (0x10, 0x7FFFFFFF, 0xFFFFFFFC, 0))
    check("positive overflow wraps modulo 2^32", actual7[1] == 0x80000006)
    check("negative result represented modulo 2^32", actualm3[2] == 0xFFFFFFF9)
    print("\nRESULT: SPECIFICATION SELF-CHECK PASS (9 checks)")
    print("LIMIT: Not a CellX2 implementation test.")

if __name__ == "__main__":
    main()
