import sys


def read_archive(filename: str) -> str | None:
    try:
        fileopen = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return None

    try:
        content = fileopen.read()
        print("---")
        print(content)
        print("---")
    except OSError as error:
        print(f"Error reading file '{filename}': {error}")
        return None
    finally:
        fileopen.close()
        print(f"File '{filename}' closed.")

    return content


def write_archive(filename: str, content: str) -> None:
    try:
        fileopen = open(filename, "w")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        print("Data not saved.")
        return

    try:
        fileopen.write(content)
    except OSError as error:
        print(f"Error writing file '{filename}': {error}")
        print("Data not saved.")
        return
    finally:
        fileopen.close()

    print(f"Data saved in file '{filename}'.")


def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")

    content = read_archive(sys.argv[1])
    if content is None:
        return

    transformed = "".join(line + "#\n" for line in content.splitlines())
    print("Transform data:")
    print("---")
    print(transformed)
    print("---")

    new_filename = input("Enter new file name (or empty): ")
    if new_filename == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_filename}'")
    write_archive(new_filename, transformed)


if __name__ == "__main__":
    ft_archive_creation()
