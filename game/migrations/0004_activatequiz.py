# Generated by Django 4.2.7 on 2023-11-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_questions_option_a_alter_questions_option_b_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivateQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activate_quiz', models.BooleanField(default=0)),
            ],
        ),
    ]
