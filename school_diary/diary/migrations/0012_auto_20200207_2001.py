# Generated by Django 3.0.2 on 2020-02-07 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0011_auto_20200207_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['surname', 'first_name', 'second_name'], 'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученик'},
        ),
        migrations.RemoveField(
            model_name='students',
            name='id',
        ),
        migrations.AlterField(
            model_name='students',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('second_name', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('subjects', models.ManyToManyField(to='diary.Subjects', verbose_name='Предметы')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
                'ordering': ['surname', 'first_name', 'second_name'],
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], verbose_name='Класс')),
                ('letter', models.CharField(max_length=2, verbose_name='Буква')),
                ('teachers', models.ManyToManyField(to='diary.Teachers', verbose_name='Учителя')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'ordering': ['number', 'letter'],
            },
        ),
    ]