def inputs():
    print("Enter coordinates in form 'x y'")
    c1 = input("Enter first coordinate: ")
    c2 = input("Enter second coordinate: ")
    x = float(input("Enter new x-coordinate of third point: "))
    return c1, c2, x


def sep_values(c1, c2):
    first = c1.split(" ")
    second = c2.split(" ")
    x1 = float(first[0])
    y1 = float(first[1])
    x2 = float(second[0])
    y2 = float(second[1])
    return x1, y1, x2, y2


def find_line(x1, y1, x2, y2, x):
    m = (y1 - y2) / (x1 - x2)
    b = y1 - m * x1
    y_coord = m * x + b
    (print("The y-coordinate required for the given x-coordinate to "
           "lie of this line is: {} ".format(y_coord)))
    return y_coord


if __name__ == "__main__":
    c1, c2, x = inputs()
    x1, y1, x2, y2 = sep_values(c1, c2)
    find_line(x1, y1, x2, y2, x)
