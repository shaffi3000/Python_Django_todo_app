# Generated by Django 3.1.4 on 2021-01-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='type',
            field=models.CharField(default='day', max_length=10),
        ),
    ]