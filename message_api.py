import requests

out_data = {"user": "vt51", "message": "hello! how's class?"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=out_data)
print(r.status_code)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/rdh46")
print(r)
print(type(r))
print(r.text)
list = r.json()
print(list)
