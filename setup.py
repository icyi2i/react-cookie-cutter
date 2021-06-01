import json
import os

# os.system("git clone https://github.com/icyi2i/react-cookie-cutter.git")
os.chdir("react-cookie-cutter")
# os.unlink(".git")
os.system("git init")
os.system("npm install")

with open("package.json") as f:
    package = json.load(f)

print("Enter the following details. Leave empty for default values:")
name = input(
    f"- name ({package['name']}) :")
description = input(
    f"- description ({package['description']}) :")

keywords = list(map(
    lambda x : x.strip(),
    input(f"- keywords ({package['keywords']}) :").split(",")))

if len(name):
    package["name"] = name
if len(description):
    package["description"] = description
if len(keywords[0]):
    package["keywords"] = keywords

# print(package)
with open("package.json", mode="w") as f:
    json.dump(package, f, indent=2)

if len(name):
    os.chdir("../")
    os.renames(
        os.path.join(os.getcwd(), "react-cookie-cutter"),
        os.path.join(os.getcwd(), name))
