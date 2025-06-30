from color_utils import read_colors_from_file, display_colors, get_user_selection

def main():
    colors = read_colors_from_file("colors.txt")
    display_colors(colors)
    selected_color = get_user_selection(colors)
    print("The selected color is:", selected_color)

if __name__ == "__main__":
    main()
