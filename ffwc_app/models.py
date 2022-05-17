from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class User_Data(models.Model):
    user = models.ForeignKey(
                    User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    weight = models.FloatField(validators=[MinValueValidator(0.0)], )
    goal_weight = models.FloatField(validators=[MinValueValidator(0.0)], )
    height = models.FloatField(validators=[MinValueValidator(0.0)], )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Weight_Update(models.Model):
    user = models.ForeignKey(User_Data, on_delete=models.CASCADE,
                                                        null=True, blank=True)
    weight_update = models.FloatField(
                                validators=[MinValueValidator(0.0)], default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

    class Meta:
        ordering = ['created']
