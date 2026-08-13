from bs4 import BeautifulSoup as BS
import requests

URLS = {"ARIES_URL" : "https://orakul.com/horoscope/astrologic/general/aries/today.html",
        "TAURUS_URL" : "https://orakul.com/horoscope/astrologic/general/taurus/today.html",
        "GEMINI_URL" : "https://orakul.com/horoscope/astrologic/general/gemini/today.html",
        "CANCER_URL" : "https://orakul.com/horoscope/astrologic/general/cancer/today.html",
        "LION_URL" : "https://orakul.com/horoscope/astrologic/general/lion/today.html",
        "VIRGO_URL" : "https://orakul.com/horoscope/astrologic/general/virgo/today.html",
        "LIBRA_URL" : "https://orakul.com/horoscope/astrologic/general/libra/today.html",
        "SCORPIO_URL" : "https://orakul.com/horoscope/astrologic/general/scorpio/today.html",
        "SAGITTARIUS_URL" : "https://orakul.com/horoscope/astrologic/general/sagittarius/today.html",
        "CAPRICORN_URL" : "https://orakul.com/horoscope/astrologic/general/capricorn/today.html",
        "AQUARIUS_URL" : "https://orakul.com/horoscope/astrologic/general/aquarius/today.html",
        "PISCES_URL" : "https://orakul.com/horoscope/astrologic/general/pisces/today.html",
}

def get_horoscope(url_):
    request = requests.get(url_)
    html = BS(request.text, "html.parser")
    text = html.find(class_="horoBlock").text
    text = " ".join(text.split()[:-1])
    return text

    # with open(f"prophecies/{sign}.txt", "w", encoding="UTF-8") as f:
    #     f.write(text)

