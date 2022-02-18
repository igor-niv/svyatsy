from svyatsy_main.DatabaseLayer.models import Svyatsy

nameOfMonths = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
          'декабрь']

daysInMonth = {'январь': 31,
               'февраль': 29,
               'март': 31,
               'апрель': 30,
               'май': 31,
               'июнь': 30,
               'июль': 31,
               'август': 31,
               'сентябрь': 30,
               'октябрь': 31,
               'ноябрь': 30,
               'декабрь': 31}

engLetterToRusLetterInUrl = {
    'a': 'А',
    'b': 'Б',
    'v': 'В',
    'g': 'Г',
    'd': 'Д',
    'e': 'Е',
    'z': 'З',
    'i': 'И',
    'k': 'К',
    'l': 'Л',
    'm': 'М',
    'n': 'Н',
    'o': 'О',
    'p': 'П',
    'r': 'Р',
    's': 'С',
    't': 'Т',
    'u': 'У',
    'f': 'Ф',
    'x': 'Х',
    'yu': 'Ю',
    'ya': 'Я'
}

class DbSvyatsyService:
    @staticmethod
    def getRecordsByMonth(month: str):
        svyatsyByMonth = Svyatsy.objects.filter(month=month).order_by('day')
        return svyatsyByMonth

    @staticmethod
    def getAllRecords():
        svyatsy = Svyatsy.objects.all().order_by('name')
        return svyatsy

    @staticmethod
    def searchByName(name: str):
        svyatsyByName = Svyatsy.objects.filter(name=name).order_by('name')
        return svyatsyByName

    @staticmethod
    def isMan(sex: str):
        return sex == "man"
