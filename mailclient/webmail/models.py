#coding:utf-8
from django.db import models

#class Meta 排序
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['name']

#blank=True 可选填,verbose_name设置标签显示或者设置为第一个参数.e-mail
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name='e-mail',blank=True)
    
    #组织return 默认返回的相关的信息.
    def __unicode__(self):
        return u"%s %s"%(self.first_name,self.last_name)

#blank 表示是否为空,null表示空值为什么
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True,null=True)
    
    def __unicode__(self):
        return self.title