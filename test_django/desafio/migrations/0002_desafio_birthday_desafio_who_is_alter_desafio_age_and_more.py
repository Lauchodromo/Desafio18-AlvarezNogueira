# Generated by Django 4.0.6 on 2022-07-29 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desafio',
            name='birthday',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='desafio',
            name='who_is',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='desafio',
            name='age',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='desafio',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
