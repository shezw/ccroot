from Menu import MenuOption, display_menu

def main():

    options_json = [
        {"id": 1, "title": "Windows", "value": "win", "comment": "Windows system"},
        {"id": 2, "title": "Linux", "value": "linux", "comment": "Linux system"},
        {"id": 3, "title": "MacOS", "value": "mac", "comment": "MacOS system"},
        {"id": 4, "title": "Android", "value": "android", "comment": "Android system"},
        {"id": 5, "title": "iOS", "value": "ios", "comment": "iOS system"}
    ]

    # a test options that include 5 real systems
    options = [
        MenuOption(1, "Windows", "win", "Windows system"),
        MenuOption(2, "Linux", "linux", "Linux system"),
        MenuOption(3, "MacOS", "mac", "MacOS system"),
        MenuOption(4, "Android", "android", "Android system"),
        MenuOption(5, "iOS", "ios", "iOS system")
    ]

    options_form_json = [MenuOption(option["id"], option["title"], option["value"], option["comment"]) for option in options_json]

    selection = display_menu("Please select target system",options_form_json)

if __name__ == "__main__":
    main()
