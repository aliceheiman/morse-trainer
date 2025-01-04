from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import random


def clean(data, allowed_symbols):
    # Replace % symbol with the word "percent"
    data = data.replace("%", " percent")

    data = data.upper()
    uniques = set(data)

    # remove symbols
    for u in uniques:
        if u not in allowed_symbols:
            data = data.replace(u, "")

    return data


def get_nature_briefings():

    url = "https://www.nature.com/nature/articles?type=nature-briefing"

    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    # Get short summaries
    results = soup.find_all("div", {"data-test": "article-description"})
    results = [r.text.strip() for r in results]

    # Get their dates
    dates = soup.find_all("time", {"itemprop": "datePublished"})
    dates = [d.text.strip() for d in dates]

    return results, dates


def get_shakespeare(sonnet_nr):

    with open("data/shakespeare.json", "r") as f:
        contents = f.read()

    sonnets = json.loads(contents)
    return sonnets[sonnet_nr - 1]
