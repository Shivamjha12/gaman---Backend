# Generated by Django 4.2 on 2023-07-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_alter_destinationplanner_moneyspent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationplanner',
            name='MoneySpent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='destinationplanner',
            name='tips',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]