from rich.console import Console
from rich.tree import Tree
from pathlib import Path
from sys import argv

path = Path(argv[1])
console = Console()
for itemroot in path.glob("*"):
    console.print(f"[green]{itemroot.relative_to(path)}")

def make_tree(path: Path) -> Tree:
    tree = Tree(f"[bold red]{path.name}")
    for itemroot in path.glob("*"):
        if itemroot.is_dir():
            tree.add(make_tree(itemroot))
        else:
            tree.add(f"[green]{itemroot.relative_to(path)}")

    return tree

console.print(make_tree(path))