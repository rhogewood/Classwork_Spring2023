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

def HDL_analysis(HDL_int):
    if HDL_int >=60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer



interface()