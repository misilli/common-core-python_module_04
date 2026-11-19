def secure_archive(
    name: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(name, "r") as file:
                return True, file.read()
        elif action == "write":
            with open(name, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"
        else:
            return False, f"Unknown action '{action}'"
    except (OSError, ValueError) as error:
        return False, f"{error}"


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read", ""))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/sudoers", "read", ""))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "read", "")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", str(result[1])))


if __name__ == "__main__":
    main()
