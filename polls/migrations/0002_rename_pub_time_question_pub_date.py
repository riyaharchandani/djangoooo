# Generated by Django 5.1.2 on 2024-10-14 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_time',
            new_name='pub_date',
        ),
    ]
