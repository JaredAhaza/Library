# Generated by Django 2.2.2 on 2019-06-27 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
    ]
