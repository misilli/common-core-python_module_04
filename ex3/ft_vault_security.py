def secure_archive(name: str, action: str, content: str) -> tuple[bool, str]:
    try:
        if action == "write":
            with open(name, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"
        elif action == "read":
            with open(name, "r") as file:
                return True, file.read()
    except OSError as error:
        return False, str(error)
    return False, ""


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read", ""))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read", ""))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "read", "")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", str(result[1])))


if __name__ == "__main__":
    main()
