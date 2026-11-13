import sys
import typing


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    try:
        content: str = file.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
    except OSError as error:
        print(f"Error reading file '{filename}': {error}")
        return
    finally:
        file.close()

    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
