# bikes/models.py

import pandas as pd
from turtle import distance
from django.db import models
from django.urls import reverse


""" class DatatableView(models.Model):
    time_depart = models.DateTimeField()
    time_return = models.DateTimeField()
    depart_stn_id = models.IntegerField()
    depart_stn_name = models.TextField()
    return_stn_id = models.IntegerField()
    return_stn_name = models.TextField()
    distance = models.FloatField()
    duration = models.FloatField()

    def __str__(self):
        return self.time_depart
 """

# time taken to read data
