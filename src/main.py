"""Entry point for the Git practice calculator project."""

from datetime import date

from utils import add, divide, multiply, subtract


def main() -> None:
    """Print the student's name and the current date."""
    print("Name: Bishwaprotap Ray")
    print(f"Today's date: {date.today().isoformat()}")
    print(f"7 + 3 = {add(7, 3)}")
    print(f"7 - 3 = {subtract(7, 3)}")
    print(f"7 × 3 = {multiply(7, 3)}")
    print(f"7 ÷ 3 = {divide(7, 3):.2f}")


if __name__ == "__main__":
    main()
