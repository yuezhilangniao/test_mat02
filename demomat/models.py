from django.db import models

# Create your models here.
from django.db import models

#定义部门模型类
class PartInfo(models.Model):
    #btitle = models.CharField(max_length=20)#名称
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = 'byzoro_part'
        verbose_name = '部门表'
        verbose_name_plural = verbose_name

#定义英雄模型类HeroInfo
class ManInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    month = models.IntegerField(verbose_name='月份')
    yeji = models.FloatField('业绩')
    huikuan = models.FloatField(verbose_name='回款')
    hetong = models.FloatField(verbose_name='合同')
    sex = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    #hcomment = models.CharField(max_length=200, null=True, blank=False) #hcomment对应的数据库中的字段可以为空，但通过后台管理页面添加信息时hcomment对应的输入框不能为空
    mpart = models.ForeignKey('PartInfo')#英雄与图书表的关系为一对多，所以属性定义在英雄模型类中

    class Meta:
        db_table = 'byzoro_man'
        verbose_name = '员工表'
        verbose_name_plural = verbose_name



class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name='书名')
    body = models.CharField(max_length=20, verbose_name='书体')
    b_man = models.ManyToManyField(ManInfo,blank=True,verbose_name='liaoke')