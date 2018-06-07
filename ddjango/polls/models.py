# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=100, verbose_name='问题')
    pub_date = models.DateTimeField(default=datetime.now(), verbose_name='问题时间')

    class Meta:
        verbose_name = "投票"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=50, verbose_name='选择')
    vote = models.IntegerField(default=0, verbose_name='票数')

    class Meta:
        verbose_name = '选择'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.choice_text
