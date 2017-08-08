from django.db import models


# Create your models here.
class Thread(models.Model):
    op_id = models.CharField
    title = models.CharField
    timestamp = models.DateField
    comments = models.CharField
