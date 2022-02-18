from django import forms
from django.shortcuts import render

from svyatsy_main.BusinessLayer.search_name_interactor import SearchNameInteractor
from svyatsy_main.DatabaseLayer.db_service import DbSvyatsyService


class SearchForm(forms.Form):
    s = forms.CharField()

def formSearch(request):
    searchForm = SearchForm(request.GET)
    if not searchForm.is_valid():
        return render(request, 'NamesBySearch.html', {'isFound': False, 'isEmptySearch': True, 'namesViewModel': None})

    name = searchForm.cleaned_data['s']
    namesViewModel = SearchNameInteractor.searchNames(name)

    if namesViewModel.isEmpty():
        return render(request, 'NamesBySearch.html', {'isFound': False, 'isEmptySearch': False, 'namesViewModel': namesViewModel})

    return render(request, 'NamesBySearch.html', {'isFound': True, 'isEmptySearch': False, 'namesViewModel': namesViewModel})



