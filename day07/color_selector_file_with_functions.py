def load_colors(filename):
    """Reads color names from a text file and returns a list."""
    colors = []
    with open(filename, 'r') as fh:
        for line in fh:
            colors.append(line.strip())
    return colors

def display_colors(colors):
    """Displays a numbered list of colors."""
    for i, color in enumerate(colors):
        print(f"{i}. {color}")

def select_color(colors):
    """Prompts the user to select a color by number and returns the selection."""
    while True:
        try:
            selected = int(input("Select color: "))
            if 0 <= selected < len(colors):
                return colors[selected]
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    filename = 'colors.txt'
    colors = load_colors(filename)
    display_colors(colors)
    selected_color = select_color(colors)
    print("The selected color is:", selected_color)

if __name__ == "__main__":
    main()
