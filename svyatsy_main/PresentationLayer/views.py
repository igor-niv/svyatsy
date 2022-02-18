from django import forms
from django.shortcuts import render

from svyatsy_main.BusinessLayer.get_all_names_interactor import GetAllNamesInteractor
from svyatsy_main.BusinessLayer.get_names_by_abc_interactor import GetNamesByAbcInteractor
from svyatsy_main.BusinessLayer.get_names_by_calendar_interactor import GetNamesByCalendarInteractor


# обработчик запроса на отображение всех имен на странице
def allNames(request):
    # обращение к слою бизнес-логики для получения данных
    allNamesByMonthsViewModel = GetAllNamesInteractor.getAllNamesGroupedByMonths()
    return render(request, 'AllNames.html', {'allNamesByMonthsViewModel': allNamesByMonthsViewModel})


# обработчик запроса на отображение имен согласно выбранной букве алфавита
def namesByAbc(request):
    # последний компонент в пути (URL) - это буква алфавита (английская, ее позже преобразуем в русскую)
    firstNamesLetterEng = request.path.rsplit('/', 1)[-1]
    if len(firstNamesLetterEng) == 0:
        firstNamesLetterEng = 'a'
    # обращение к слою бизнес-логики для получения данных
    namesByAbcViewModel = GetNamesByAbcInteractor.getNamesByFirstLetter(firstNamesLetterEng)
    if namesByAbcViewModel is None:
        return page_not_found_view(request, None)
    return render(request, "NamesByAbc.html", {'namesByAbcViewModel': namesByAbcViewModel})


# обработчик запроса на отображение имен согласно выбранному месяцу календаря
def namesByCalendar(request):
    monthIndex = request.path.rsplit('/', 1)[-1]
    if len(monthIndex) == 0:
        monthIndex = '0'
    if not monthIndex.isdigit():
        return page_not_found_view(request, None)
    # обращение к слою бизнес-логики для получения данных
    namesByMonthViewModel = GetNamesByCalendarInteractor.getNamesByMonth(int(monthIndex))
    if namesByMonthViewModel is None:
        return page_not_found_view(request, None)
    return render(request, "NamesByCalendar.html", {'namesByMonthViewModel': namesByMonthViewModel})


# обработчик, показывающий страницу с информацией о сайте
def aboutDeveloper(request):
    return render(request, 'About.html')


# обработчик, показывающий 404-ю страницу
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

