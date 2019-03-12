from django.db import models

class doctor(models.Model):
            emp = models.IntegerField(default=0)
            name = models.CharField(max_length=200)
            address = models.CharField(max_length=200)
            phone = models.IntegerField(default=0)
            specialize = models.CharField(max_length=200)

class patient(models.Model):
            enroll = models.IntegerField(default=0)
            name = models.CharField(max_length=200)
            address = models.CharField(max_length=200)
            phone = models.IntegerField(default=0)
            blood_group = models.CharField(max_length=200)

class visit(models.Model):
            emp = models.IntegerField(default=0)
            enroll = models.IntegerField(default=0)
            category = models.CharField(max_length=200)
            time = models.TimeField(max_length=200)
            date = models.DateField(max_length=200)