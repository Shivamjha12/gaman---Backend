# Generated by Django 4.2 on 2023-07-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_destinationplanner_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationplanner',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
