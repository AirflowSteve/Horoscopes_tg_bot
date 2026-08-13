from prophecies.requesting_horoblocks import URLS, get_horoscope

class User:
    def __init__(self, id, sign):
        self.id = id
        self.sign = sign
        match self.sign:
            case "Овен":
                self.url = "ARIES_URL"
            case "Телец":
                self.url = "TAURUS_URL"
            case "Близнецы":
                self.url = "GEMINI_URL"
            case "Рак":
                self.url = "CANCER_URL"
            case "Лев":
                self.url = "LION_URL"
            case "Дева":
                self.url = "VIRGO_URL"
            case "Весы":
                self.url = "LIBRA_URL"
            case "Скорпион":
                self.url = "SCORPIO_URL"
            case "Стрелец":
                self.url = "SAGITTARIUS_URL"
            case "Козерог":
                self.url = "CAPRICORN_URL"
            case "Водолей":
                self.url = "AQUARIUS_URL"
            case "Рыбы":
                self.url = "PISCES_URL"

