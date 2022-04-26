# Svyatsy  (Святцы)

Исходный код сайта www.svyatsy.site

Сайт разработан на языке Python с использованием веб-фреймворка Django.
Сайт хостится на платформе DigitalOcean (виртуальная машина с Ubuntu 20.04 / Django 3.2 / Gunicorn 'Green Unicorn' / Nginx).

# Изучение кода можно начинать с 
* файла https://github.com/igor-niv/svyatsy/blob/main/svyatsy/urls.py он содержит роутинг запросов;
* файла https://github.com/igor-niv/svyatsy/blob/main/svyatsy_main/PresentationLayer/views.py он содержит обработчики запросов (presentation layer);
* файла https://github.com/igor-niv/svyatsy/blob/main/svyatsy_main/PresentationLayer/forms.py он содержит обработчик формы на поиск имени (presentation layer);
* четырех файлов interactors в папке https://github.com/igor-niv/svyatsy/tree/main/svyatsy_main/BusinessLayer они содержат код бизнес логики по обработке данных (business logic layer);
* файла https://github.com/igor-niv/svyatsy/blob/main/svyatsy_main/DatabaseLayer/models.py он содержит объектную модеь БД  (data access layer);
* файла https://github.com/igor-niv/svyatsy/blob/main/svyatsy_main/DatabaseLayer/db_service.py он содержит простой DAO класс (data access layer);
* папки https://github.com/igor-niv/svyatsy/tree/main/templates она содержит html шаблоны сайта.

В данных файлах присутствуют комментарии на русском.

# Примечание
* Реализован человека-читаемый URL через роутинг запросов;
* Включение подвала и чердака в HTML коде реализовано через директивы сервера (код в отдаче будет представлять единую HTML страницу);
* Реализован счетчик посещений от liveinternet;
* Реализована интеграция с VK через виджет шаринга информации о сайте;
* Созданы файлы robots.txt и sitemap.xml (www.svyatsy.site/robots.txt и www.svyatsy.site/sitemap.xml);
* Сайт проиндексирован в Google и Yandex (запрос на индексацию отправлен 18 февраля, она еще может быть в процессе);
* и т.д.

Сайт проверен в Safari (macOS, iPadOS, iOS), Chrome (Windows), Microsoft Edge (Windows).

Сайт проиндексирован Яндекс (доступен через строку поиска site:svyatsy.site).
