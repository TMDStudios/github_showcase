# Generated by Django 3.1.7 on 2021-04-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]