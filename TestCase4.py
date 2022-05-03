from bs4 import BeautifulSoup
import requests

base_url = 'https://www.musala.com/careers/join-us'
scraped_locations = {'Sofia', 'Skopje'}

# 1. open musala/join us
source = requests.get(base_url).content

# 2. get an array of locations
soup = BeautifulSoup(source, 'lxml')
location_options = soup.find("select", { "id" : "get_location" }).findAll("option", recursive=False)

# 3. filter array by Skopje and Sofia
filtered_locations = [a for a in location_options if a.text in scraped_locations]
for i in filtered_locations:

    # 4. request filtered array
    url = f"{base_url}/?location={i.text}"
    location_page = requests.get(url).content
    soup_location = BeautifulSoup(location_page, 'lxml')

    # 5. get array of positions
    positions_in_one_location = soup_location.findAll("article", {"class": "card-jobsHot"})

    # 6. aggregate and print
    for k in positions_in_one_location:
        location = k.find("p", {"class": "card-jobsHot__location"})
        title = k.find("h2", {"class": "card-jobsHot__title"})
        link = k.find("a", {"class": "card-jobsHot__link"})

        print(f"{i.text}{location.text == 'Anywhere' and ' (Anywhere)' or ''}\n"
              f"Position: {title.text}\n"
              f"More info: {link['href']}\n"
              f"_________________")