"""svyatsy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from svyatsy_main.PresentationLayer.views import allNames, namesByAbc, namesByCalendar, aboutDeveloper
from svyatsy_main.PresentationLayer.forms import formSearch

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', namesByCalendar),
    path('AllNames/', allNames),
    path('About/', aboutDeveloper),
    path('NamesByAbc/', namesByAbc),
    re_path(r'^NamesByAbc/[а-я]*', namesByAbc),
    path('NamesByCalendar/', namesByCalendar),
    re_path(r'^NamesByCalendar/[0-9]', namesByCalendar),
    re_path(r'^[0-9]', namesByCalendar),
    re_path(r'^search/', formSearch),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("sitemap.xml", TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
]

handler404 = "svyatsy_main.PresentationLayer.views.page_not_found_view"
