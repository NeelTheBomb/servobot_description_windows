from pathlib import Path
import re

def flip_slashes_in_quotes(file_path):
    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace / with \ only inside double quotes
    def replace_inside_quotes(match):
        quoted_text = match.group(0)
        return quoted_text.replace("/", "\\")

    content = re.sub(r'"[^"]*"', replace_inside_quotes, content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated file in place: {path}")

# Example usage
flip_slashes_in_quotes("robot.urdf")