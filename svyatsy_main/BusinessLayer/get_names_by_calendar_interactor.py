from svyatsy_main.DatabaseLayer.db_service import DbSvyatsyService, nameOfMonths

# Получение имен святых, рожденных в определенный месяц

# Модель содержит одно имя и информацию о нем
class NameByMonthViewModel:
    def __init__(self, name, descr, day):
        self.name = name
        self.descr = descr
        self.day = day

# Модель содержит мужские и женские имена
class NamesByMonthViewModel:
    def __init__(self):
        self.month = str()
        self.men = list()
        self.women = list()


class GetNamesByCalendarInteractor:
    # Получение имен святых, рожденных в определенный месяц
    @staticmethod
    def getNamesByMonth(monthIndex: int):
        namesByMonthViewModel = NamesByMonthViewModel()
        month = str()
        if monthIndex < len(nameOfMonths):
            month = nameOfMonths[monthIndex]
        else:
            return None                                         # если индекс месяца превышает 11 (отчет от нуля), то вернем признак ошибки
        allRecords = DbSvyatsyService.getRecordsByMonth(month)
        for record in allRecords.values_list():
            sex = record[1]
            name = record[2]
            descr = record[3]
            day = record[5]
            nameByMonth = NameByMonthViewModel(name, descr, day)
            if DbSvyatsyService.isMan(sex):
                namesByMonthViewModel.men.append(nameByMonth)
            else:
                namesByMonthViewModel.women.append(nameByMonth)

        namesByMonthViewModel.month = month
        return namesByMonthViewModel
