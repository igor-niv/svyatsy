from svyatsy_main.DatabaseLayer.db_service import DbSvyatsyService, nameOfMonths

# Получить все имена и их описания

# Модель содержит все имена святых, рожденных в определенном месяце.
# Группировка по датам.
class NamesInMonthViewModel:
    def __init__(self, month: str, dates2Names: dict):
        self.month = month
        self.dates2Names = dates2Names  # словарь, содержащий даты и список имен святых, рожденных в них

# Модель содержит все имена всех святых и описания, что есть в базе данных сайта.
# Группировка по месяцам.
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

    # Встроенный итератор.
    # Нужен для простоты итерации в коде html страницы.
    def __iter__(self):
        return self.__allNamesByMonths.__iter__()

class GetAllNamesInteractor:
    # Получить все имена и их описания.
    # Основная сложность состоит в том, что имена (и описания) должны быть сгруппированы
    # по месяцам, внутри месяца нужна группировка по датам, внутри конкретной даты нужна
    # группировка по признаку мужчина / женщина. Это нужно, чтоб данные красиво отобразить
    # в общей таблице в html коде.
    @staticmethod
    def getAllNamesGroupedByMonths() -> AllNamesViewModel:
        allNamesViewModel = AllNamesViewModel()

        for month in nameOfMonths:
            allRecordsByMonth = DbSvyatsyService.getRecordsByMonth(month) # получаем все имена в конкретном месяце...

            if allRecordsByMonth.count() == 0:
                continue

            datesToManNames = dict()
            datesToWomanNames = dict()
            recordsList = allRecordsByMonth.values('day').values_list() #... и сортируем их по дате
            for record in recordsList:
                sex = record[1]
                name = record[2]
                day = record[5]

                # разделение на мужские и женские имена,
                # храним их в разных словарях

                dateToNamesManOrWoman = dict()
                if DbSvyatsyService.isMan(sex):
                    dateToNamesManOrWoman = datesToManNames
                else:
                    dateToNamesManOrWoman = datesToWomanNames

                if day not in dateToNamesManOrWoman:
                    dateToNamesManOrWoman[day] = name
                else:
                    dateToNamesManOrWoman[day] += ', ' + name

            # Теперь нужно объединить словари с мужскими и женскими именами в один словарь.
            # В этом общем словаре одно значение будет выглядеть так:
            #  ключ              значение
            #  Дата -> "Мужские имена: здесь список имен; Женские имена: здесь список имен"
            #
            # Т.к. ключи в обоих словарях - это даты. То нам нужно получить все даты которые есть
            # в обоих словарях без повторения (т.к. на определенную дату могут быть мужские и женские имена,
            # либо только мужские (либо только женские), либо вообще не быть имен. Для этого используем set
            # множество. Затем получив объединение ключей мы можем выбирать данные из обоих массивов в общий.

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





















