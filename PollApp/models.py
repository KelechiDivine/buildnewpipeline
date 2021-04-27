from django.db import models


# Create your models here.

class Exam(models.Model):
    # objects = None
    Question = models.CharField(max_length=100)
    optionOne = models.CharField(max_length=100)
    optionTwo = models.CharField(max_length=100)
    optionThree = models.CharField(max_length=100)
    optionFour = models.CharField(max_length=100)
    optionFive = models.CharField(max_length=100)
    corrans = models.CharField(max_length=100)
