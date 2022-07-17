# from pickletools import long1
# from pyexpat import model
# level = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name="级别")
# 国际重要,国家重要,省级重要,其他重要
# 国家级自然保护区,省级自然保护区,国家湿地公园,省级湿地公园,湿地保护小区,小微湿地
from django.db import models


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
    naturalLevel = models.CharField(max_length=20, verbose_name="自然级别")
    ParkLevel = models.CharField(max_length=20, verbose_name="行政级别")
    numbering = models.CharField(max_length=20, verbose_name="编号")
    name1 = models.CharField(max_length=60, verbose_name="名称")
    fullname = models.CharField(max_length=60, verbose_name="全名")
    abbreviation = models.CharField(max_length=10, verbose_name="简称")
    icon = models.CharField(max_length=60, verbose_name="图标")
    initiate = models.DateTimeField(verbose_name="加入时间")
    slide = models.CharField(max_length=60, verbose_name="轮播图片")
    introduceEN = models.CharField(max_length=600, verbose_name="介绍英")
    introduceZH = models.CharField(max_length=600, verbose_name="介绍中")
    introduceMP3EN = models.CharField(max_length=60, verbose_name="英文语音")
    introduceMP3ZH = models.CharField(max_length=60, verbose_name="中文语音")
    introduceMP4 = models.CharField(max_length=60, verbose_name="介绍影片")
    introduceVR = models.CharField(max_length=60, verbose_name="介绍vr")
    lon = models.FloatField(verbose_name="中心经度")
    lat = models.FloatField(verbose_name="中心伟度")
    mapLevel = models.IntegerField(verbose_name="最佳级别")
    province = models.CharField(max_length=10, verbose_name="省")
    area = models.CharField(max_length=20, verbose_name="片区")
    city = models.CharField(max_length=10, verbose_name="市")
    county = models.CharField(max_length=10, verbose_name="县")
    scenery = models.CharField(max_length=20, verbose_name="景点")

    class Meta:
        db_table = "sd_park"
        verbose_name = "park"
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
    name3 = models.CharField(max_length=60, verbose_name="分类")

    class Meta:
        db_table = "sd_newsPosts"
        verbose_name = "资讯分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name3


class News(models.Model):
    fatherPark = models.ForeignKey(NewsPosts, on_delete=models.CASCADE, verbose_name="所属分类")
    IMG = models.CharField(max_length=60, verbose_name="图片")
    title = models.CharField(max_length=20, verbose_name="标题")
    subTitle = models.CharField(max_length=30, verbose_name="副标题")
    point = models.CharField(max_length=60, verbose_name="要点")
    text = models.CharField(max_length=2000, verbose_name="正文")
    quote = models.CharField(max_length=60, verbose_name="引用位置")
    add_Date = models.DateTimeField(verbose_name="添加时间")
    category = models.CharField(max_length=60, verbose_name="分类")

    class Meta:
        db_table = "sd_news"
        verbose_name = "资讯原文"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class HomeData(models.Model):
    homeURL = models.CharField(max_length=60, verbose_name="首页外链")
    homeIMG = models.CharField(max_length=60, verbose_name="图片")
    homeTitle = models.CharField(max_length=60, verbose_name="图片标题")
    animation = models.CharField(max_length=60, verbose_name="首页动画图片")

    class Meta:
        db_table = "sd_homeData"
        verbose_name = "首页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.animation
