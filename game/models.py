from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Questions(models.Model):
    CAT_CHOICES = (
        ('Basic','Basic'),
        ('Intermediate','Intermediate'),
        ('Complex','Complex'),
        
    )
    question = models.CharField(max_length=250)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices=CAT_CHOICES)


    class Meta:
        ordering = ('-category',)

    def __str__(self):
        return self.question
    

class Result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question_id = models.IntegerField()
    question_ans = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    score = models.IntegerField(default=0)