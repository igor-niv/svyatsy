# Generated by Django 3.2.9 on 2022-02-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Svyatsy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.TextField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('month', models.TextField()),
                ('day', models.IntegerField()),
            ],
        ),
    ]