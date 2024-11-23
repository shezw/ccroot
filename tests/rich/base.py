from rich.console import Console
from rich.json import JSON
from rich.__main__ import make_test_card
from datetime import datetime
from time import sleep

from rich import print
from rich.columns import Columns

import os
import sys

console = Console()

console.print("Console Print text")
console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")


console.log("Hello, World!")

console.print_json('[false, true, null, "foo"]')

console.out("Locals", locals())

console.rule("[bold red]Chapter 2")


def do_work():
    console.print("do work")
    sleep(2)

with console.status("Working..."):
    do_work()

with console.status("Monkeying around...", spinner="monkey"):
    do_work()


path = console.input("Please input or drop you home path: ")


with open("report.txt", "wt") as report_file:
    console = Console(file=report_file)
    console.rule(f"Report Generated {datetime.now().ctime()}" + path)

# with console.pager():
#     console.print(make_test_card())

if len(sys.argv) < 2:
    print("Usage: python columns.py DIRECTORY")
else:
    directory = os.listdir(sys.argv[1])
    columns = Columns(directory, equal=True, expand=True)
    print(columns)

# with console.screen():
#     console.print(locals())
#     sleep(5)


