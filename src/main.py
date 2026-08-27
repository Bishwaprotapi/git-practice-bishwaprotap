"""Entry point for the Git practice calculator project."""

from datetime import date


def main() -> None:
    """Print the student's name and the current date."""
    print("Name: Bishwaprotap Ray")
    print(f"Today's date: {date.today().isoformat()}")


if __name__ == "__main__":
    main()
