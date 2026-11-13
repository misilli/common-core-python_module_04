import sys
import typing


def print_error(message: str) -> None:
    print(f"[STDERR] {message}", file=sys.stderr)


def read_archive(filename: str) -> str | None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print_error(f"Error opening file '{filename}': {error}")
        return None

    try:
        content: str = file.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
    except OSError as error:
        print_error(f"Error reading file '{filename}': {error}")
        return None
    finally:
        file.close()

    print(f"File '{filename}' closed.")
    return content


def add_archive_character(content: str) -> str:
    return "".join(line + "#\n" for line in content.splitlines())


def save_archive(filename: str, content: str) -> bool:
    print(f"Saving data to '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "w")
    except OSError as error:
        print_error(f"Error opening file '{filename}': {error}")
        return False

    try:
        file.write(content)
    except OSError as error:
        print_error(f"Error writing file '{filename}': {error}")
        return False
    finally:
        file.close()

    print(f"Data saved in file '{filename}'.")
    return True


def ask_filename() -> str:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    return sys.stdin.readline().rstrip("\n")


def ft_stream_management() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    content: str | None = read_archive(sys.argv[1])
    if content is None:
        return

    transformed: str = add_archive_character(content)
    print("Transform data:")
    print("---")
    print(transformed, end="")
    print("---")

    new_filename: str = ask_filename()
    if new_filename == "":
        print("Not saving data.")
        return

    if not save_archive(new_filename, transformed):
        print("Data not saved.")


if __name__ == "__main__":
    ft_stream_management()
