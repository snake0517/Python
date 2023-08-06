def calculate_rectangle_area(length, width):
    return length * width

def main():
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length <= 0 or width <= 0:
            print("Please enter positive values for length and width.")
        else:
            area = calculate_rectangle_area(length, width)
            print("The area of the rectangle is:", area)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
