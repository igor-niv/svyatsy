from svyatsy_main.DatabaseLayer.db_service import DbSvyatsyService, engLetterToRusLetterInUrl

#  Получение имен, начинающихся на заданную букву

# Модель содержит одно имя и информацию о нем
class NameByAbcViewModel:
    def __init__(self, name, descr, month, day):
        self.name = name
        self.descr = descr
        self.month = month
        self.day = day

# Модель содержит мужские и женские имена
class NamesByAbcViewModel:
    def __init__(self):
        self.firstLetterRu = str()
        self.men = list()
        self.women = list()

class GetNamesByAbcInteractor:
    #  Получение имен, начинающихся на заданную букву
    @staticmethod
    def getNamesByFirstLetter(firstLetterEng: str):
        namesByAbcViewModel = NamesByAbcViewModel()
        # мы получаем в URL английскую букву (или две, например для Ю: yu), нужно преобразовать в одну русскую
        if firstLetterEng in engLetterToRusLetterInUrl.keys():
            firstLetterRu = engLetterToRusLetterInUrl[firstLetterEng]
        else:
            return None
        allRecords = DbSvyatsyService.getAllRecords()
        for record in allRecords.values_list():
            sex = record[1]
            name = record[2]
            if not name.startswith(firstLetterRu):
                continue
            descr = record[3]
            month = record[4]
            day = record[5]
            nameByAbc = NameByAbcViewModel(name, descr, month, day)
            if DbSvyatsyService.isMan(sex):
                namesByAbcViewModel.men.append(nameByAbc)
            else:
                namesByAbcViewModel.women.append(nameByAbc)

        namesByAbcViewModel.firstLetterRu = firstLetterRu
        return namesByAbcViewModel