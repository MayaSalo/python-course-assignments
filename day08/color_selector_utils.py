def read_colors_from_file(filename):
    """Reads color names from a file, stripping newline characters."""
    with open(filename) as fh:
        return [line.rstrip("\n") for line in fh]

def display_colors(colors):
    """Displays the list of colors with numbered indices."""
    for i, color in enumerate(colors):
        print("{}. {}".format(i, color))

def get_user_selection(colors):
    """Prompts user for a selection and returns the chosen color."""
    selected = int(input("Select color: "))
    return colors[selected]
