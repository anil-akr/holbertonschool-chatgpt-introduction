#!/usr/bin/python3
import sys

def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <non-negative integer>", file=sys.stderr)
        return 1

    try:
        n = int(sys.argv[1])
        print(factorial(n))
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
