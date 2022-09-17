# from pickletools import long1
# from pyexpat import model
# level = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name="级别")
# 国际重要,国家重要,省级重要,其他重要
# 国家级自然保护区,省级自然保护区,国家湿地公园,省级湿地公园,湿地保护小区,小微湿地
from django.db import models
from django.contrib.auth.models import AbstractUser
#用户模型
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机")

    # identifier = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = 'identifier'

    class Meta:
        db_table = "sd_users"
        verbose_name = "用 户 "
    def __str__(self):
        return self.username


# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=60, verbose_name="名称")
    introduce = models.CharField(max_length=1000, verbose_name="介绍")
    count = models.CharField(max_length=60, verbose_name="数量")

    class Meta:
        db_table = "sd_posts"
        verbose_name = "等级"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Park(models.Model):
    province_CHOICE = (
        (1, "湖北省"),
    )
    area_CHOICE = (
        (1, "鄂东北"),
        (2, "鄂东南"),
        (3, "鄂西南"),
        (4, "鄂西北"),
        (5, "江汉平原"),
    )
    city_CHOICE = (
        (1, "武汉"),
        (2, "鄂州"),
        (3, "黄冈"),
        (4, "黄石"),
        (5, "咸宁"),
        (6, "孝感"),
        (7, "随州"),
        (8, "荆门"),
        (9, "荆州"),
        (10, "襄阳"),
        (11, "宜昌"),
        (12, "十堰"),
        (13, "恩施"),
        (14, "省直"),

    )
    # county_CHOICE = (
    #     (1, "神农架"),
    #     (2, "天门"),
    #     (3, "潜江"),
    #     (4, "仙桃"),
    # )
    mapLevel_CHOICE = (
        (1, 15),
        (2, 16),
        (3, 17),
        (4, 18),
    )
    initiate_CHOICE = (
        (1, "2000以前"),
        (2, "2000 - 2005"),
        (3, "2006 - 2010"),
        (4, "2011 - 2015"),
        (5, "2016 - 2020"),
        (6, "2021至今"),
    )
    naturalLevel_CHOICE = (
        (1, "国际重要湿地"),
        (2, "国家重要湿地"),
        (3, "省级重要湿地"),
        (4, "重要湿地"),

    )
    ParkLevel_CHOICE = (
        (1, "国家级自然保护区"),
        (2, "省级自然保护区"),
        (3, "国家湿地公园"),
        (4, "省级湿地公园"),
        (5, "湿地保护区(小区)"),
        (6, "省级小微湿地"),
    )

    naturalLevel = models.CharField(max_length=60, verbose_name="自然级别", choices=naturalLevel_CHOICE)
    ParkLevel = models.CharField(max_length=60, verbose_name="级别划分", choices=ParkLevel_CHOICE)
    numbering = models.CharField(max_length=60, verbose_name="编号")
    name1 = models.CharField(max_length=60, verbose_name="名称")
    fullname = models.CharField(max_length=60, verbose_name="全名")
    abbreviation = models.CharField(max_length=60, verbose_name="简称")
    icon = models.JSONField(default=list, blank=True, null=True, verbose_name="图标")
    initiate = models.CharField(max_length=60, verbose_name="加入时间", choices=initiate_CHOICE)
    slide = models.JSONField(default=list, blank=True, null=True, verbose_name="轮播图片")
    introduceEN = models.TextField(max_length=12000, verbose_name="介绍英")
    introduceZH = models.TextField(max_length=8000, verbose_name="介绍中")
    introduceMP3EN = models.CharField(max_length=60, verbose_name="英文语音")
    introduceMP3ZH = models.CharField(max_length=60, verbose_name="中文语音")
    introduceMP4 = models.CharField(max_length=1000, verbose_name="介绍影片")
    introduceVR = models.CharField(max_length=60, verbose_name="介绍vr")
    lon = models.CharField(max_length=60, verbose_name="中心经度")
    lat = models.CharField(max_length=60, verbose_name="中心伟度")
    mapLevel = models.IntegerField(verbose_name="最佳级别", choices=mapLevel_CHOICE)
    province = models.CharField(max_length=20, verbose_name="省", choices=province_CHOICE)
    area = models.CharField(max_length=60, verbose_name="片区", choices=area_CHOICE)
    city = models.CharField(max_length=50, verbose_name="市", choices=city_CHOICE)
    county = models.CharField(max_length=50, verbose_name="县")
    scenery = models.JSONField(default=list, blank=True, null=True,verbose_name="景点")

    class Meta:
        db_table = "sd_park"
        verbose_name = "公园"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name1


class Protect(models.Model):
    fatherPark = models.ForeignKey(Park, on_delete=models.CASCADE, verbose_name="所属公园")
    name2 = models.CharField(max_length=60, verbose_name="名称")
    protectURL = models.CharField(max_length=60, verbose_name="外链")
    protectIMG = models.CharField(max_length=60, verbose_name="图片")
    lon = models.FloatField(verbose_name="中心经度")
    lat = models.FloatField(verbose_name="中心伟度")

    class Meta:
        db_table = "sd_protect"
        verbose_name = "公园景点"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name2


class NewsPosts(models.Model):
    label = models.CharField(max_length=60, verbose_name="分类")
    checked= models.CharField(max_length=60, verbose_name="主要")
    value= models.CharField(max_length=60, verbose_name="数值")
    class Meta:
        db_table = "sd_newsPosts"
        verbose_name = "资讯分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.label


class News(models.Model):
    fatherPark = models.ForeignKey(NewsPosts, on_delete=models.CASCADE, verbose_name="所属分类")
    IMG = models.CharField(max_length=60, verbose_name="图片",default="news.jpg")
    title = models.CharField(max_length=60, verbose_name="标题")
    subTitle = models.CharField(max_length=60, verbose_name="副标题")
    point = models.CharField(max_length=60, verbose_name="要点")
    text = models.TextField(max_length=2000, verbose_name="正文")
    quote = models.CharField(max_length=60, verbose_name="引用位置")
    add_Date = models.CharField(max_length=60, verbose_name="添加时间")
    category = models.CharField(max_length=60, verbose_name="分类")
    state=models.CharField(max_length=60, verbose_name="状态",default="true")
    class Meta:  
        db_table = "sd_news"
        verbose_name = "资讯原文"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class HomeData(models.Model):
    homeURL = models.JSONField(default=list, blank=True, null=True, verbose_name="首页外链")
    homeIMG = models.JSONField(default=list, blank=True, null=True, verbose_name="图片")
    homeTitle = models.JSONField(default=list, blank=True, null=True, verbose_name="图片标题")
    animation = models.CharField(max_length=600, verbose_name="首页动画图片")

    class Meta:
        db_table = "sd_homeData"
        verbose_name = "首页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.animation


class HomeIMGData(models.Model):
    title = models.CharField(max_length=60, verbose_name="成果")
    homeURL = models.JSONField(default=list, blank=True, null=True,verbose_name="首页外链")
    homeIMG = models.JSONField(default=list, blank=True, null=True,verbose_name="图片")
    homeTitle = models.JSONField(default=list, blank=True, null=True,verbose_name="图片标题")
    

    class Meta:
        db_table = "sd_homeIMGData"
        verbose_name = "成果"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.animation