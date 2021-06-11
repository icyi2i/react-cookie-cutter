import json
import os
import sys


# if not (
#     os.path.exists("react-cookie-cutter") and
#     os.path.isdir("react-cookie-cutter")):

#     print("# Cloning the git repository : @icyi2i/react-cookie-cutter")
#     os.system("git clone https://github.com/icyi2i/react-cookie-cutter.git")

os.chdir("react-cookie-cutter")

print("# Initializing new empty git repository...")

if os.path.exists(".git") and os.path.isdir(".git"):
    os.unlink(".git")

os.system("git init")

print("# Installing required node modules...")
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

os.remove(sys.argv[0])
