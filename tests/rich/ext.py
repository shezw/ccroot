from rich import print
from rich.panel import Panel

from rich.progress import track
from rich.progress import Progress

import time
from time import sleep

from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn

print(Panel("Hello, [red]World!"))

print(Panel.fit("Hello, [red]World!"))

print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))

import rich.progress

with rich.progress.open("data.json", "rb") as file:
    data = json.load(file)
print(data)

from time import sleep
from urllib.request import urlopen

from rich.progress import wrap_file

response = urlopen("https://www.shezw.com")
size = int(response.headers["Content-Length"])

with wrap_file(response, size) as file:
    for line in file:
        print(line.decode("utf-8"), end="")
        sleep(0.1)

for i in track(range(5), description="Processing..."):
    time.sleep(1)  # Simulate work being done


with Progress() as progress:

    task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)


text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
progress = Progress(text_column, bar_column, expand=True)

with progress:
    for n in progress.track(range(100)):
        progress.print(n)
        sleep(0.1)