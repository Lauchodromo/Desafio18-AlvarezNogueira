# Generated by Django 4.0.6 on 2022-08-10 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golem_gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='plans',
            options={'verbose_name': 'Plan', 'verbose_name_plural': 'Plans'},
        ),
    ]