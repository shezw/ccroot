from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from tools.MenuSelection import MenuSelection
from tools.Option import CCOption, CCOptionType
from tools.i18n import i18n

console = Console()


# use a dict to collect all string bellow in this file
# the left is the key with file name and short keyid of each string

# display menu should input a list of options of MenuOption
def display_menu(name=i18n("Menu.title"), options:[MenuSelection]=None):
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
            console.print(options[int(choice) - 1].to_json(), style="bold green")
            console.print(i18n("Menu.input_tip")+options[int(choice) - 1].title)
            return options[int(choice) - 1]
        else:
            console.print(i18n("Menu.invalid_tip"))


def ask_menu_choices(choices: []):
    if choices is None or len(choices) == 0:
        console.print(i18n("Menu.unsupported_option_type"+CCOptionType.CHOICE.__str__()), style="bold red")
        return None


def ask_single(option:CCOption):
    """
    Ask a single option from the user.
    :param option: The CCOption to ask.
    :return: The value of the option.
    """
    # depends manager outside

    if option.type.__str__() == CCOptionType.STRING.__str__():
        while True:
            value = Prompt.ask(option.description, default=option.default)
            if not option.required or value:
                break
    elif option.type.__str__() == CCOptionType.BOOLEAN.__str__():
        _default_value = None
        if option.default is not None:
            _default_value = "yes" if option.default else "no"
        value = Prompt.ask(option.description, choices=["yes", "no", "y","n"], default=_default_value)
        value = value in ["yes", "y"]
    elif option.type.__str__() == CCOptionType.NUMBER.__str__():
        value = Prompt.ask(option.description, default=option.default)
    elif option.type.__str__() == CCOptionType.CHOICE.__str__():
        # value = Prompt.ask(option.description, choices=option.choices, default=option.default)
        if option.choices is None or len(option.choices) == 0:
            console.print(i18n("Menu.unsupported_option_type"+option.type.__str__()), style="bold red")
            return None

        menu_options = []

        for choice in option.choices:
            if isinstance(choice, dict):
                _cmt = choice.get("description", "")
                _value = choice.get("value", "")
                _name = choice.get("name", "")
                menu_options.append(MenuSelection(str(len(menu_options) + 1), _name, _value, _cmt))
            elif isinstance(choice, str):
                menu_options.append(MenuSelection(str(len(menu_options) + 1), choice, choice, ""))

        value = display_menu(option.description, menu_options)

    elif option.type.__str__() == CCOptionType.LIBRARY.__str__():
        value = Prompt.ask(option.description, choices=option.choices, default=option.default)
    else:
        console.print(i18n("Menu.unsupported_option_type"+option.type.__str__()), style="bold red")
        return None

    return value