import re

text = "lat = 5, lon=7, xxx = 0"
# match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text)
# match = re.findall(r"((lat|lon)\s*=\s*\d+)", text)
# match = re.findall(r"(lat|lon)\s*=\s*(?:\d+)", text)  # non-saving brackets ?:
match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
print(match)

text2 = "<p>Picture <img src='bg.jpg'> in text</p>"
# match2 = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text2)
# match2 = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text2)  # \1 take 1st saving bracket from end
match2 = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text2)  # naming ?P<...>
print(match2)

with open("map.xml", "r") as f:
    lat = []
    lon = []
    for text in f:
        match = re.search(r"<point\s+[^>]*?lon=([\"\'])(?P<lon>[0-9.,]+)\1\s+[^>]*lat=([\"\'])(?P<lat>[0-9.,]+)\1", text)
        if match:
            v = match.groupdict()
            lon.append(v["lon"])
            lat.append(v["lat"])
    print(lon, lat, sep="\n")
