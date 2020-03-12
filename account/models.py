from django.db import models


class Account(models.Model):
    uuid = models.CharField("uuid", primary_key=True, max_length=34)
    name = models.CharField("ФИО", max_length=100)
    balance = models.IntegerField("Баланс")
    hold = models.IntegerField("Холд")
    status = models.BooleanField("Статус", default=False)
