# Generated by Django 5.0.4 on 2024-04-18 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizSelectWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(blank=True, max_length=50, null=True)),
                ('choice4', models.CharField(blank=True, max_length=50, null=True)),
                ('correctWord1', models.CharField(max_length=50)),
                ('correctWord2', models.CharField(blank=True, max_length=50, null=True)),
                ('correctWord3', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]