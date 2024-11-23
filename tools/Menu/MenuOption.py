# Menu option is used to render a menu with options and prompt the user to select an option.
# a single option has id, title, value, and comment.
class MenuOption():
    def __init__(self, id, title, value, comment):
        self.id = id
        self.title = title
        self.value = value
        self.comment = comment

    # menu option has a method to return a string representation of the option.
    def __str__(self):
        return f"[{self.id}] {self.title} ({self.value}) - {self.comment}"