from django import forms
from django.shortcuts import render

from svyatsy_main.BusinessLayer.get_all_names_interactor import GetAllNamesInteractor
from svyatsy_main.BusinessLayer.get_names_by_abc_interactor import GetNamesByAbcInteractor
from svyatsy_main.BusinessLayer.get_names_by_calendar_interactor import GetNamesByCalendarInteractor


def allNames(request):
    allNamesByMonthsViewModel = GetAllNamesInteractor.getAllNamesGroupedByMonths()
    return render(request, 'AllNames.html', {'allNamesByMonthsViewModel': allNamesByMonthsViewModel})


def namesByAbc(request):
    firstNamesLetterEng = request.path.rsplit('/', 1)[-1]
    if len(firstNamesLetterEng) == 0:
        firstNamesLetterEng = 'a'
    namesByAbcViewModel = GetNamesByAbcInteractor.getNamesByFirstLetter(firstNamesLetterEng)
    if namesByAbcViewModel is None:
        return page_not_found_view(request, None)
    return render(request, "NamesByAbc.html", {'namesByAbcViewModel': namesByAbcViewModel})


def namesByCalendar(request):
    monthIndex = request.path.rsplit('/', 1)[-1]
    if len(monthIndex) == 0:
        monthIndex = '0'
    if not monthIndex.isdigit():
        return page_not_found_view(request, None)
    namesByMonthViewModel = GetNamesByCalendarInteractor.getNamesByMonth(int(monthIndex))
    if namesByMonthViewModel is None:
        return page_not_found_view(request, None)
    return render(request, "NamesByCalendar.html", {'namesByMonthViewModel': namesByMonthViewModel})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def aboutDeveloper(request):
    return render(request, 'About.html')