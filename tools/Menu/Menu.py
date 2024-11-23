from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from MenuOption import MenuOption
from typing import List

console = Console()

# use a dict to collect all string bellow in this file
# the left is the key with file name and short keyid of each string
dict = {}

dict["en-us"] = {
        "Menu.title": "Please Selected",
        "Menu.head_id": "ID",
        "Menu.head_title": "Title",
        "Menu.head_value": "Value",
        "Menu.head_comment": "Comment",
        "Menu.input_tip": "Your choice is：",
        "Menu.invalid_tip": "Invalid choice, please input again.",
    }

dict["zh-cn"] = {
        "Menu.title": "请选择",
        "Menu.head_id": "编号",
        "Menu.head_title": "标题",
        "Menu.head_value": "值",
        "Menu.head_comment": "说明",
        "Menu.input_tip": "您的选择是：",
        "Menu.invalid_tip": "无效的选择，请重新输入。",
    }

# display menu should input a list of options of MenuOption
def display_menu( name = dict["en-us"]["Menu.title"], options: List[MenuOption] = []):

    # 创建一个表格以显示选项
    table = Table(box=box.SIMPLE)
    table.add_column(name, justify="left")
    table.add_row("ID", "Title", "Value", "Comment")

    for option in options:
        table.add_row(str(option.id), option.title, option.value, option.comment)

    console.print(table)

    # 允许用户选择选项
    while True:
        choice = Prompt.ask("Please input the id or value", choices=[str(i) for i in range(1, len(options) + 1)])
        print(choice)
        if choice in [str(i) for i in range(1, len(options) + 1)]:
            console.print(f"Your choice is：{options[int(choice) - 1]}")
            return options[int(choice) - 1]
        else:
            console.print("Invalid choice, please input again.")
