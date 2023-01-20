def interface():
    print("Blood Calculator")
    while True:
        print("Options:")
        print("9 - Quit")
        choice = input("Select an option: ")
        if choice == "9":
            return


def HDL_input():
    HDL_value = input("Enter the HDL result:" )
    HDL_value = int(HDL_value)
    return HDL_value

interface()