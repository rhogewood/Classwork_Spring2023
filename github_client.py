import requests

r = requests.get("https://api.github.com/repos/rhogewood"
                 "/Classwork_Spring2023/branches")
print(r)
print(type(r))
print(r.text)
branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])
