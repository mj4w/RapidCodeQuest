# Generated by Django 4.2.7 on 2023-11-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_activatequiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activatequiz',
            name='activate_quiz',
            field=models.IntegerField(default=0),
        ),
    ]
