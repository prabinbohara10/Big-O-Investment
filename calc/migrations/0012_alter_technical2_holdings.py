# Generated by Django 4.0.2 on 2022-02-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0011_alter_signup_detail_portfolio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technical2',
            name='holdings',
            field=models.IntegerField(default=10),
        ),
    ]
