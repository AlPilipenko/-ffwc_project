from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class User_Data(models.Model):
    user = models.ForeignKey(
                    User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    weight = models.FloatField()
    goal_weight = models.FloatField()
    height = models.FloatField()
    # description = models.TextField(null=True, blank=True)
    # complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    weight_update = models.FloatField(default=0)



    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']