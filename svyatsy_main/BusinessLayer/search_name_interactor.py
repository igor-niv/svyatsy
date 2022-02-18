from svyatsy_main.DatabaseLayer.db_service import DbSvyatsyService, engLetterToRusLetterInUrl


class NameViewModel:
    def __init__(self, name, descr, month, day):
        self.name = name
        self.descr = descr
        self.month = month
        self.day = day


class NamesViewModel:
    def __init__(self):
        self.searchQueryStr = str
        self.men = list()
        self.women = list()

    def isEmpty(self):
        return len(self.men) == 0 and len(self.women) == 0


class SearchNameInteractor:
    @staticmethod
    def searchNames(searchQueryStr: str):
        namesViewModel = NamesViewModel()
        namesViewModel.searchQueryStr = searchQueryStr
        records = DbSvyatsyService.searchByName(searchQueryStr)
        if records.count() == 0:
            return namesViewModel
        for record in records.values_list():
            sex = record[1]
            name = record[2]
            descr = record[3]
            month = record[4]
            day = record[5]
            nameViewModel = NameViewModel(name, descr, month, day)
            if DbSvyatsyService.isMan(sex):
                namesViewModel.men.append(nameViewModel)
            else:
                namesViewModel.women.append(nameViewModel)

        return namesViewModel
