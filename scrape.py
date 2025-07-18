import json
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_sharks"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

species_list = []

# On the page, species are in unordered lists under specific sections
for ul in soup.find_all("ul"):
    for li in ul.find_all("li"):
        a_tag = li.find("a")
        if a_tag and a_tag.get("href") and "wiki" in a_tag.get("href"):
            species_name = a_tag.text.strip()
            species_link = "https://en.wikipedia.org" + a_tag.get("href")
            species_list.append((species_name, species_link))

# Remove duplicates and filter only sharks (avoid unrelated links)
species_list = list(set(species_list))
species_list = [(name, link) for name, link in species_list if "shark" in name.lower()]

species_list.pop(8)

#finish cleaning list

print(f"Found {len(species_list)} shark species")
for name, link in species_list[:10]:
    print(name, link)



with open("sharks.json", "w") as f:
    json.dump(species_list, f)
