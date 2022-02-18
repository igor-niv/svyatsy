# Svyatsy (Святцы)

Исходный код сайта www.svyatsy.site
Сайт разработан на языке Python с использованием веб-фреймворка Django.
Сайт хостится на платформе DigitalOcean (виртуальная машина с Ubuntu 20.04 / Django 3.2 / Gunicorn 'Green Unicorn' / Nginx).

Сайст состоит из одного "приложения" (по терминологии Django), которое расположено в папке svyatsy_main.
В данной папке важны следующие подпапки:
* BusinessLayer - бизнес логика сайта;
* DatabaseLayer - уровень доступа к данным (в качестве хранилища используется БД SQLite);
* PresentationLayer - содержит "котроллеры", которые непосредственно взаимодейтствуют с графическим интерфейсом сайта.

В папке templates содержаться шаблоны html страниц.