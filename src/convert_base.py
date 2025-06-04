import argparse
from string import digits as DIGITS

ALPHABET = DIGITS + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def int_to_base(n: int, base: int) -> str:
    """Convert an integer to a string in the given base."""
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    if n == 0:
        return '0'
    sign = '-' if n < 0 else ''
    n = abs(n)
    result = []
    while n:
        n, rem = divmod(n, base)
        result.append(ALPHABET[rem])
    return sign + ''.join(reversed(result))


def convert_base(number_str: str, from_base: int, to_base: int) -> str:
    """Convert number_str from from_base to to_base."""
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        raise ValueError("Bases must be between 2 and 36")
    # int() handles sign as well
    n = int(number_str, from_base)
    return int_to_base(n, to_base)


def main() -> None:
    parser = argparse.ArgumentParser(description="Base converter")
    parser.add_argument("number", help="Number to convert")
    parser.add_argument("from_base", type=int, help="Base of the input number")
    parser.add_argument("to_base", type=int, help="Base to convert to")
    args = parser.parse_args()

    print(convert_base(args.number, args.from_base, args.to_base))


if __name__ == "__main__":
    main()
