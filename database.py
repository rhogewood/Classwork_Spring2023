def create_patient_entry(first_name, last_name, patient_mrn, patient_age):
    new_patient = {"First Name": first_name,
                   "Last Name": last_name,
                   "Patient MRN": patient_mrn,
                   "Patient Age": patient_age,
                   "Test": []}
    return new_patient


def get_full_name(patient):
    return "{} {}".format(patient["First Name"], patient["Last Name"])


def print_database(db):
    for patient in db.values():
        print("MRN: {}, Full Name: {}, Age: {}"
              .format(patient["Patient MRN"],
                      get_full_name(patient),
                      patient["Patient Age"]))


def main_driver():
    db = {}
    db[1] = create_patient_entry("Ann", "Ables", 1, 34)
    db[2] = create_patient_entry("Bob", "Boyles", 2, 45)
    db[3] = create_patient_entry("Chris", "Chou", 3, 52)
    print(db)
    print_database(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 100)
    add_test_to_patient(db, 2, "HDL", 99)
    print_database(db)
    # room_numbers = ["103", "232", "333"]
    # print(db)
    # print_directory(db, room_numbers)
    print(get_test_result(db, 2, "LDL"))


# two different ways to get the same thing for room numbers(above)


def get_patient_entry(db, mrn_to_find):
    patient = db.get(mrn_to_find)
    if patient is None:
        return False
    return patient


def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient is False:
        print("Bad entry")
    else:
        patient["Test"].append([test_name, test_value])
    return


def get_test_val_from_list(test_list, test_name):
    for test in test_list:
        if test[0] == test_name:
            return test[1]
    return False


def get_test_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_value = get_test_val_from_list(patient["Test"], test_name)
    return (test_value)


if __name__ == "__main__":
    main_driver()
