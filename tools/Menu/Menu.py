from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from tools.i18n import i18n

console = Console()


# use a dict to collect all string bellow in this file
# the left is the key with file name and short keyid of each string

# display menu should input a list of options of MenuOption
def display_menu(name=i18n("Menu.title"), options=None):
    # 创建一个表格以显示选项
    if options is None:
        return None

    table = Table(box=box.SIMPLE)
    table.add_column(name, justify="left")
    table.add_row(i18n("Menu.head_id"), i18n("Menu.head_title"), i18n("Menu.head_value"), i18n("Menu.head_comment"))

    for option in options:
        table.add_row(str(option.id), option.title, option.value, option.comment)

    console.print(table)

    # 允许用户选择选项
    while True:
        choice = Prompt.ask(i18n("Menu.input_prompt"), choices=[str(i) for i in range(1, len(options) + 1)])
        if choice in [str(i) for i in range(1, len(options) + 1)]:
            console.print(f"{i18n("Menu.input_tip")}{options[int(choice) - 1]}")
            return options[int(choice) - 1]
        else:
            console.print(i18n("Menu.invalid_tip"))
