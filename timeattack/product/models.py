from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings 

class DrinkModel(AbstractUser): 
    class Meta: db_table = "Drink"