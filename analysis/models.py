from django.db import models
from django.conf import settings

class Kitchen_info(models.Model):
    kitchen_name = models.CharField(max_length=20)
    lat = models.FloatField(blank=False)
    lng = models.FloatField(blank=False)
    image = models.CharField(max_length=20)
    capacity = models.IntegerField()

class Reservation_time(models.Model):
    kitchen_name = models.ForeignKey(Kitchen_info, on_delete=models.CASCADE)
    start_date = models.DateField()
    last_date = models.DateField()
    time = models.IntegerField()

class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Start_up(models.Model):
    signgucd = models.IntegerField()
    signgunm = models.CharField(max_length=20)
    danger =  models.CharField(max_length=20)
    close = models.FloatField(blank=False)
    remain_term = models.FloatField(blank=False)
    plma = models.FloatField(blank=False)

class move_pop(models.Model):
    rdnm = models.CharField(max_length=20)
    all_total = models.IntegerField()
    men_total = models.IntegerField()
    women_total = models.IntegerField()
    total_20s = models.IntegerField()
    total_30s = models.IntegerField()
    total_40s = models.IntegerField()
    total_50s = models.IntegerField()
    total_60s = models.IntegerField()
    men_20s = models.IntegerField()
    men_30s = models.IntegerField()
    men_40s = models.IntegerField()
    men_50s = models.IntegerField()
    men_60s = models.IntegerField()
    women_20s = models.IntegerField()
    women_30s = models.IntegerField()
    women_40s = models.IntegerField()
    women_50s = models.IntegerField()
    women_60s = models.IntegerField()

class stay_pop(models.Model):
    rdnm = models.CharField(max_length=20)
    all_total = models.IntegerField()
    men_total = models.IntegerField()
    women_total = models.IntegerField()
    total_20s = models.IntegerField()
    total_30s = models.IntegerField()
    total_40s = models.IntegerField()
    total_50s = models.IntegerField()
    total_60s = models.IntegerField()
    men_20s = models.IntegerField()
    men_30s = models.IntegerField()
    men_40s = models.IntegerField()
    men_50s = models.IntegerField()
    men_60s = models.IntegerField()
    women_20s = models.IntegerField()
    women_30s = models.IntegerField()
    women_40s = models.IntegerField()
    women_50s = models.IntegerField()
    women_60s = models.IntegerField()

class Movepop(models.Model):
    rdnm = models.CharField(max_length=20)
    all_total = models.IntegerField()
    men_total = models.IntegerField()
    women_total = models.IntegerField()
    total_20s = models.IntegerField()
    total_30s = models.IntegerField()
    total_40s = models.IntegerField()
    total_50s = models.IntegerField()
    total_60s = models.IntegerField()
    men_20s = models.IntegerField()
    men_30s = models.IntegerField()
    men_40s = models.IntegerField()
    men_50s = models.IntegerField()
    men_60s = models.IntegerField()
    women_20s = models.IntegerField()
    women_30s = models.IntegerField()
    women_40s = models.IntegerField()
    women_50s = models.IntegerField()
    women_60s = models.IntegerField()

class Sales(models.Model):
    rdnm = models.CharField(max_length=20)
    store_code = models.CharField(max_length=20)
    mon_sales = models.IntegerField()
    mon_sales_count = models.IntegerField()
    weekdays_sales_rate = models.IntegerField()
    weekend_sales_rate = models.IntegerField()
    weekdays_sales_coount = models.IntegerField()
    weekend_sales_count = models.IntegerField()
    breakfast_sales = models.IntegerField()
    lunch_sales = models.IntegerField()
    dinner_sales = models.IntegerField()
    men_sales_rate = models.IntegerField()
    women_sales_rate = models.IntegerField()
    



     