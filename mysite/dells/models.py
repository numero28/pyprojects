from django.db import models


# Create your models here.
from django.db.models.functions import math


class Circle(models.Model):

    radius = models.DecimalField

    def area(self):
        return math.pi * self.radius * self.radius
