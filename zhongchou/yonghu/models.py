#coding=utf-8
from django.db import models
import datetime
class Users(models.Model):#账户表
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=15)
    Password = models.CharField(max_length=15)
    TouXiang = models.CharField(max_length=50)
    #一个人拥有一个产品库表ChanPinTable_ID，记录他发布的产品
    #test = models.CharField(max_length=15,null=True)
    def __unicode__(self):
        return self.Username

class Chanpin(models.Model):
    ChanPinID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=15)
    picture = models.CharField(max_length=50)
    jieshao = models.TextField()
    TaocanName_1 = models.CharField(max_length=15)
    TaocanPrice_1 = models.FloatField()
    Taocanjianjie_1 = models.TextField(null=True)
    TaocanName_2 = models.CharField(max_length=15)
    TaocanPrice_2 = models.FloatField()
    Taocanjianjie_2 = models.TextField(null=True)
    TaocanName_3 = models.CharField(max_length=15)
    TaocanPrice_3 = models.FloatField()
    Taocanjianjie_3 = models.TextField(null=True)
    Price = models.FloatField()
    hasSale = models.FloatField()
    CreateTime = models.DateTimeField(default=datetime.datetime.now)
    DueTime = models.DateTimeField()
    #一个产品具有一张评论表
    def __unicode__(self):
        return self.Name