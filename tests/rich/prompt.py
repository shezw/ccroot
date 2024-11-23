
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console

# name = Prompt.ask("Enter your name")

is_accept = Confirm.ask("Please accept the policy.", default="y")
assert is_accept

name = Prompt.ask("Enter your Path", default="./")

Console().print(name)

name = Prompt.ask("Select platform", choices=["DirectFB", "Wayland", "X11"], default="DirectFB")

Console().print(name)