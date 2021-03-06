# Generated by Django 2.2.7 on 2019-12-27 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analysis', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.CharField(choices=[('M', '오전(6시~12시)'), ('A', '오후(12시~18시)'), ('N', '밤/심야(18시~24시)')], max_length=1)),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.Kitchen_info')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
