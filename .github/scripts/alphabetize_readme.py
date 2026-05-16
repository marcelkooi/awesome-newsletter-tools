import re
import sys


def get_sort_key(item):
    match = re.match(r"- \[([^\]]+)\]", item)
    if match:
        return match.group(1).lower()
    return item.lower()


def sort_readme_lists(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    lines = content.split("\n")
    result = []
    i = 0
    changed = False

    while i < len(lines):
        line = lines[i]

        if not line.startswith("- "):
            result.append(line)
            i += 1
        else:
            list_items = []
            while i < len(lines) and lines[i].startswith("- "):
                list_items.append(lines[i])
                i += 1

            sorted_items = sorted(list_items, key=get_sort_key)
            if sorted_items != list_items:
                changed = True
            result.extend(sorted_items)

    new_content = "\n".join(result)

    with open(filepath, "w") as f:
        f.write(new_content)

    if changed:
        print(f"Sorted lists in {filepath}")
    else:
        print(f"No changes needed in {filepath}")

    return changed


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    sort_readme_lists(filepath)
