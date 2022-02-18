from django import forms
from django.shortcuts import render

from svyatsy_main.BusinessLayer.search_name_interactor import SearchNameInteractor
from svyatsy_main.DatabaseLayer.db_service import DbSvyatsyService

# Форма поиска имени

# Объявим форму с одним текстовым полем,
# куда пользователь будет вводить имя для поиска.
# Нужно только для упрощения парсинга запроса.
# "Реальная" форма (form) определена в html коде.
class SearchForm(forms.Form):
    s = forms.CharField()

# Обработчик запроса на поиск имени
def formSearch(request):
    searchForm = SearchForm(request.GET)

    # Если запрос не валидный, отобразим соответственный статус на странице
    if not searchForm.is_valid():
        return render(request, 'NamesBySearch.html', {'isFound': False, 'isEmptySearch': True, 'namesViewModel': None})

    name = searchForm.cleaned_data['s'] # получение имени из запроса
    namesViewModel = SearchNameInteractor.searchNames(name) # используем слой бизнес-логики для поиска имени в БД

    # ни одного имени по запросу не найдено, отобразим соответственный статус на странице
    if namesViewModel.isEmpty():
        return render(request, 'NamesBySearch.html', {'isFound': False, 'isEmptySearch': False, 'namesViewModel': namesViewModel})

    # имя (или имена) найдены, покажем их на странице
    return render(request, 'NamesBySearch.html', {'isFound': True, 'isEmptySearch': False, 'namesViewModel': namesViewModel})



