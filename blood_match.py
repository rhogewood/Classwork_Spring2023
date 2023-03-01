import requests

# r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/rdh46")
# print(r)
# print(type(r))
# print(r.text)
# patients = r.json()
# print(patients)
# {"Donor":"F4","Recipient":"M6"}

# r_donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F4")
# print(r_donor.text)
# # B-
#
# r_rec = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M6")
# print(r_rec.text)
# # B-
# # They have the same blood type - OK match


out_data = {"Name": "rdh46", "Match": "Yes"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json=out_data)
print(r.status_code)
print(r.text)
