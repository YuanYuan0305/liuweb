import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >=timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class tk_xzt(models.Model):
    th = models.IntegerField(default=0)
    tlx = models.CharField(max_length=200)
    tg = models.CharField(max_length=200)
    ta = models.CharField(max_length=200)
    tb = models.CharField(max_length=200)
    tc = models.CharField(max_length=200)
    td = models.CharField(max_length=200)
    tdan = models.CharField(max_length=10)

    def __str__(self):
        return self.tg

class tk_ctj(models.Model):
    th = models.IntegerField(default=0)
    rq = models.DateTimeField('done wrong')
    usr = models.CharField(max_length=100)
    rightcnt = models.IntegerField(default=0)
    errorcnt = models.IntegerField(default=0)

    def __str__(self):
        return self.usr



