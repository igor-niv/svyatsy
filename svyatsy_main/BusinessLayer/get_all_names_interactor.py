from svyatsy_main.DatabaseLayer.db_service import DbSvyatsyService, nameOfMonths


class NamesInMonthViewModel:
    def __init__(self, month: str, dates2Names: dict):
        self.month = month
        self.dates2Names = dates2Names

class AllNamesViewModel:
    def __init__(self):
        self.__allNamesByMonths = list()

    def addNamesInMonth(self, month: str, dates2Names: dict):
        namesInMonth = NamesInMonthViewModel(month, dates2Names)
        self.__allNamesByMonths.append(namesInMonth)

    def getNamesInMonth(self, month) -> NamesInMonthViewModel:
        for namesInMonth in self.__allNamesByMonths:
            if namesInMonth.month == month:
                return namesInMonth
        return None

    def __iter__(self):
        return self.__allNamesByMonths.__iter__()

class GetAllNamesInteractor:
    @staticmethod
    def getAllNamesGroupedByMonths() -> AllNamesViewModel:
        allNamesViewModel = AllNamesViewModel()

        for month in nameOfMonths:
            allRecordsByMonth = DbSvyatsyService.getRecordsByMonth(month)

            if allRecordsByMonth.count() == 0:
                continue

            datesToManNames = dict()
            datesToWomanNames = dict()
            recordsList = allRecordsByMonth.values('day').values_list()
            for record in recordsList:
                sex = record[1]
                name = record[2]
                day = record[5]

                dateToNamesManOrWoman = dict()
                if DbSvyatsyService.isMan(sex):
                    dateToNamesManOrWoman = datesToManNames
                else:
                    dateToNamesManOrWoman = datesToWomanNames

                if day not in dateToNamesManOrWoman:
                    dateToNamesManOrWoman[day] = name
                else:
                    dateToNamesManOrWoman[day] += ', ' + name

            allKeysForManAndWoman = set()
            allKeysForManAndWoman.update(datesToManNames.keys())
            allKeysForManAndWoman.update(datesToWomanNames.keys())

            datesToManAndWomanNames = dict()
            for key in allKeysForManAndWoman:
                manNames = ""
                womanNames = ""
                if key in datesToManNames.keys():
                    manNames = "<strong>Мужские имена: </strong><br>"
                    manNames += datesToManNames[key]
                if key in datesToWomanNames.keys():
                    womanNames = "<strong>Женcкие имена: </strong><br>"
                    womanNames += datesToWomanNames[key]
                if len(manNames) > 0 and len(womanNames) > 0:
                    manNames += "<br><br>"
                datesToManAndWomanNames[key] = manNames + womanNames

            allNamesViewModel.addNamesInMonth(month.title(), datesToManAndWomanNames)

        return allNamesViewModel





















