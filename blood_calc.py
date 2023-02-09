def interface():
    print("Blood Calc")
    while True:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Total Cholesterol")
        print("9 - Quit")
        choice = input("Select an option: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            TC_driver()


def HDL_driver():
    HDL_in = HDL_input()
    HDL_ana = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_ana)


def HDL_input():
    HDL_value = input("Enter the HDL result:")
    HDL_value = int(HDL_value)
    return HDL_value


def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def HDL_output(HDL_value, HDL_ana):
    print("The HDL result of {} is considered {}".format(HDL_value, HDL_ana))


def LDL_driver():
    LDL_in = LDL_input()
    LDL_ana = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_ana)


def LDL_input():
    LDL_value = input("Enter the LDL result:")
    LDL_value = int(LDL_value)
    return LDL_value


def LDL_analysis(LDL_int):
    if LDL_int >= 190:
        answer = "Very High"
    elif 160 <= LDL_int < 189:
        answer = "High"
    elif 130 <= LDL_int < 159:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer


def LDL_output(LDL_value, LDL_ana):
    print("The LDL result of {} is considered {}".format(LDL_value, LDL_ana))


def TC_driver():
    TC_in = TC_input()
    TC_ana = TC_analysis(TC_in)
    TC_output(TC_in, TC_ana)


def TC_input():
    TC_value = input("Enter the Total Cholesterol result:")
    TC_value = int(TC_value)
    return TC_value


def TC_analysis(TC_int):
    if TC_int >= 240:
        answer = "High"
    elif 200 <= TC_int < 240:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer


def TC_output(TC_value, TC_ana):
    (print("The Total Cholesterol result of {} is considered {}"
           .format(TC_value, TC_ana)))

    if __name__ == "__main__":
        interface()
