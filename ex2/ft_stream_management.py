import sys


def read_archive(filename: str) -> str | None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
        return None

    try:
        content = file.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
    except OSError as e:
        print(
            f"[STDERR] Error reading file '{filename}': {e}", file=sys.stderr)
        return None
    finally:
        file.close()

    print(f"File '{filename}' closed.")
    return content


def write_archive(filename: str, content: str) -> None:
    try:
        fileopen = open(filename, "w")
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
        print("Data not saved.")
        return

    try:
        fileopen.write(content)
    except OSError as e:
        print(
            f"[STDERR] Error writing file '{filename}': {e}", file=sys.stderr)
        print("Data not saved.")
        return
    finally:
        fileopen.close()

    print(f"Data saved in file '{filename}'.")


def ft_stream_management() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    content: str | None = read_archive(sys.argv[1])
    if content is None:
        return

    transformed = "".join(line + "#\n" for line in content.splitlines())
    print("Transform data:")
    print("---")
    print(transformed, end="")
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    new_filename = sys.stdin.readline().rstrip("\n")
    if new_filename == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_filename}'")
    write_archive(new_filename, transformed)


if __name__ == "__main__":
    ft_stream_management()
