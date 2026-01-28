from pathlib import Path

def flip_slashes_in_place(file_path):
    path = Path(file_path)

    # Read file
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace / with \
    content = content.replace("/", "\\")

    # Write back to the same file
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated file in place: {path}")

# Example usage
flip_slashes_in_place("robot.urdf")
