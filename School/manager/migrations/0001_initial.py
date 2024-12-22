# Generated by Django 5.1.3 on 2024-12-20 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nomi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sanasi")),
            ],
            options={
                'verbose_name': 'Kurs ',
                'verbose_name_plural': 'Kurslar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nomi')),
                ('homework', models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name='Uyga vazifa')),
                ('deadline', models.DateTimeField(auto_now_add=True, verbose_name='Uyga vazifa muddati')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sanasi")),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sanasi')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.course', verbose_name='Kursi')),
            ],
            options={
                'verbose_name': 'Dars ',
                'verbose_name_plural': 'Darslar',
                'ordering': ['-id'],
            },
        ),
    ]
