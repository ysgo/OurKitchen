# Generated by Django 2.2.7 on 2019-11-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_auto_20191126_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulting',
            name='kitchen',
            field=models.CharField(max_length=20),
        ),
    ]
