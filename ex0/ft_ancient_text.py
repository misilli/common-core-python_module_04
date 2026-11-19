import sys


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{filename}'")
        fileopen = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    try:
        content = fileopen.read()
        print("---")
        print(content)
        print("---")
    except (OSError, ValueError) as error:
        print(f"Error reading file '{filename}': {error}")
        return
    finally:
        fileopen.close()
        print(f"File '{filename}' closed.")


if __name__ == "__main__":
    ft_ancient_text()