in_file = open("input_file_input_lecture.txt", 'r')
fruit = in_file.readlines()
print(fruit)
in_file.close()


# a way to read line by line
# in_file = open("input_file_input_lecture.txt", 'r')
# for line in in_file:
#    print(line)

def analyze_ID(input_line):
    patient_data = first_line.strip("/n").split("=")
    patient_id = int(patient_data[1])
    return patient_id


def read_file():
    in_file2 = open("input_data.txt", "r")
    first_line = in_file2.readline()
    id = analyze_ID(first_line)
    # patient_data = first_line.strip("/n").split("=")
    # patient_id = int(patient_data[1])

# One Testing Approach
# - if put calculation in read_file; but if remove to different
# function test for input obsolete
# just need one for analyze Id instead
# def test_read_file():
#    from module import read_file
#    filename = "my_test_data.txt"
#    answer = read_file(filename)
#    expected = 50
#    assert answer == expected
