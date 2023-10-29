# Generated by Django 4.2.6 on 2023-10-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]