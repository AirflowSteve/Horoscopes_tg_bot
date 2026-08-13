from prophecies.requesting_horoblocks import URLS, get_horoscope

class User:
    def __init__(self, id, sign):
        self.id = id
        self.sign = sign
        match self.sign:
            case "Овен":
                self.url = URLS["ARIES_URL"]
            case "Телец":
                self.url = URLS["TAURUS_URL"]
            case "Близнецы":
                self.url = URLS["GEMINI_URL"]
            case "Рак":
                self.url = URLS["CANCER_URL"]
            case "Лев":
                self.url = URLS["LION_URL"]
            case "Дева":
                self.url = URLS["VIRGO_URL"]
            case "Весы":
                self.url = URLS["LIBRA_URL"]
            case "Скорпион":
                self.url = URLS["SCORPIO_URL"]
            case "Стрелец":
                self.url = URLS["SAGITTARIUS_URL"]
            case "Козерог":
                self.url = URLS["CAPRICORN_URL"]
            case "Водолей":
                self.url = URLS["AQUARIUS_URL"]
            case "Рыбы":
                self.url = URLS["PISCES_URL"]

        self.prophecy = get_horoscope(self.url)
