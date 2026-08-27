"""Entry point for the Git practice calculator project."""

from datetime import date

from utils import absolute_value, add, divide, multiply, remainder, subtract


def main() -> None:
    """Print the student's name and the current date."""
    print("Name: Bishwaprotap Ray")
    print(f"Today's date: {date.today().isoformat()}")
    print(f"7 + 3 = {add(7, 3)}")
    print(f"7 - 3 = {subtract(7, 3)}")
    print(f"7 × 3 = {multiply(7, 3)}")
    print(f"7 ÷ 3 = {divide(7, 3):.2f}")
    print(f"|-7| = {absolute_value(-7)}")
    print(f"7 remainder 3 = {remainder(7, 3)}")


if __name__ == "__main__":
    main()
