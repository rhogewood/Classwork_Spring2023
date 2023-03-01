import requests

out_data = {
    "name": "Rebecca Hogewood",
    "net_id": "rdh46",
    "e-mail": "rebecca.hogewood@duke.edu"
}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
                  json=out_data)
print(r.status_code)
print(r.text)
