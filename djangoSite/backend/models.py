from django.db import models


# Create your models here.
class Backend(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    class Meta:
        db_table = 't_backend'