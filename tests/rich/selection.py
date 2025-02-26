from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich import box

console = Console()

def display_menu(options):
    # 创建一个表格以显示选项
    table = Table(box=box.SIMPLE)
    table.add_column("选项", justify="center")

    for option in options:
        table.add_row(option)

    console.print(table)

def main():
    options = ["选项 1", "选项 2", "选项 3", "选项 4"]
    display_menu(options)

    # 允许用户选择选项
    while True:
        choice = Prompt.ask("请输入选项的编号（1-4）", choices=[str(i) for i in range(1, len(options) + 1)])
        if choice in [str(i) for i in range(1, len(options) + 1)]:
            console.print("你选择的是："+options[int(choice) - 1])
            break
        else:
            console.print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()