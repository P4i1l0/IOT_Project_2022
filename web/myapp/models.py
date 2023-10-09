from django.db import models

# Create your models here.
class Tables(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    len_person = models.IntegerField()
    max_person = models.IntegerField()
    level = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return self.title