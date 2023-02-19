import json
from urllib.request import urlopen

md_template = ""
with open("README-template.md", "r", encoding="utf8") as f:
    md_template = f.read()

jasima_url = "https://linku.la/jasima/data.json"
data = json.loads(urlopen(jasima_url).read().decode("utf8"))

list_body = ""

for font in data["fonts"]:
    name = str(font)
    font_object = data["fonts"][font]

    if "webpage" in font_object["links"]:
        url = font_object["links"]["webpage"]
    elif "repo" in font_object["links"]:
        url = font_object["links"]["repo"]
    elif "fontfile" in font_object["links"]:
        url = font_object["links"]["fontfile"]

    print(font_object.keys())

    creator = "Unknown Author"
    if "creator" in font_object.keys():
        creator = font_object["creator"]

    license = "?"
    if "license" in font_object.keys():
        license = font_object["license"]

    list_body += f"|[{name}]({url}) | {creator} | {license}\n"

print(md_template.format(list_body=list_body[:-1]))

with open("../README.md", "w", encoding="utf8") as f:
    f.write(md_template.format(list_body=list_body[:-1]))