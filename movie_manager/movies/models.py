from django.db import models

# Create your models here.
class CensorInfo(models.Model):
    rating = models.CharField(max_length = 10, null = True)
    certified_by = models.CharField(max_length = 200, null = True)


class MovieInfo(models.Model):
    title = models.CharField(max_length = 200)
    year = models.IntegerField(null = True)
    summary = models.TextField()
    censor_details = models.OneToOneField(CensorInfo, on_delete=models.SET_NULL, related_name = 'movie', null = True)

class Director(models.Model):
    name = models.CharField(max_length = 300)


