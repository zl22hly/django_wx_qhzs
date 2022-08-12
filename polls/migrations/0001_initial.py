# Generated by Django 3.2.13 on 2022-08-08 14:13

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeURL', models.CharField(max_length=60, verbose_name='首页外链')),
                ('homeIMG', models.CharField(max_length=60, verbose_name='图片')),
                ('homeTitle', models.CharField(max_length=60, verbose_name='图片标题')),
                ('animation', models.CharField(max_length=60, verbose_name='首页动画图片')),
            ],
            options={
                'verbose_name': '首页',
                'verbose_name_plural': '首页',
                'db_table': 'sd_homeData',
            },
        ),
        migrations.CreateModel(
            name='NewsPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name3', models.CharField(max_length=60, verbose_name='分类')),
            ],
            options={
                'verbose_name': '资讯分类',
                'verbose_name_plural': '资讯分类',
                'db_table': 'sd_newsPosts',
            },
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naturalLevel', models.CharField(choices=[(1, '国际重要湿地'), (2, '国家重要湿地'), (3, '省级重要湿地'), (4, '重要湿地')], max_length=20, verbose_name='自然级别')),
                ('ParkLevel', models.CharField(choices=[(1, '国家级自然保护区'), (2, '省级自然保护区'), (3, '国家湿地公园'), (4, '省级湿地公园'), (5, '湿地保护区(小区)'), (6, '省级小微湿地')], max_length=20, verbose_name='级别划分')),
                ('numbering', models.CharField(max_length=20, verbose_name='编号')),
                ('name1', models.CharField(max_length=60, verbose_name='名称')),
                ('fullname', models.CharField(max_length=60, verbose_name='全名')),
                ('abbreviation', models.CharField(max_length=10, verbose_name='简称')),
                ('icon', models.CharField(max_length=60, verbose_name='图标')),
                ('initiate', models.CharField(choices=[(1, '2000以前'), (2, '2000 - 2005'), (3, '2006 - 2010'), (4, '2011 - 2015'), (5, '2016 - 2020'), (6, '2021至今')], max_length=60, verbose_name='加入时间')),
                ('slide', models.CharField(max_length=60, verbose_name='轮播图片')),
                ('introduceEN', models.CharField(max_length=600, verbose_name='介绍英')),
                ('introduceZH', models.CharField(max_length=600, verbose_name='介绍中')),
                ('introduceMP3EN', models.CharField(max_length=60, verbose_name='英文语音')),
                ('introduceMP3ZH', models.CharField(max_length=60, verbose_name='中文语音')),
                ('introduceMP4', models.CharField(max_length=60, verbose_name='介绍影片')),
                ('introduceVR', models.CharField(max_length=60, verbose_name='介绍vr')),
                ('lon', models.FloatField(verbose_name='中心经度')),
                ('lat', models.FloatField(verbose_name='中心伟度')),
                ('mapLevel', models.IntegerField(choices=[(1, 15), (2, 16), (3, 17), (4, 18)], verbose_name='最佳级别')),
                ('province', models.CharField(choices=[(1, '湖北省')], max_length=10, verbose_name='省')),
                ('area', models.CharField(choices=[(1, '鄂东北'), (2, '鄂东南'), (3, '鄂西南'), (4, '鄂西北'), (5, '江汉平原')], max_length=20, verbose_name='片区')),
                ('city', models.CharField(choices=[(1, '武汉'), (2, '鄂州'), (3, '黄冈'), (4, '黄石'), (5, '咸宁'), (6, '孝感'), (7, '随州'), (8, '荆门'), (9, '荆州'), (10, '襄阳'), (11, '宜昌'), (12, '十堰'), (13, '恩施'), (14, '神农架'), (15, '天门'), (16, '潜江'), (17, '仙桃')], max_length=10, verbose_name='市')),
                ('county', models.CharField(max_length=10, verbose_name='县')),
                ('scenery', models.CharField(max_length=20, verbose_name='景点')),
            ],
            options={
                'verbose_name': 'park',
                'verbose_name_plural': 'park',
                'db_table': 'sd_park',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='名称')),
                ('introduce', models.CharField(max_length=1000, verbose_name='介绍')),
                ('count', models.CharField(max_length=60, verbose_name='数量')),
            ],
            options={
                'verbose_name': '等级',
                'verbose_name_plural': '等级',
                'db_table': 'sd_posts',
            },
        ),
        migrations.CreateModel(
            name='Protect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=60, verbose_name='名称')),
                ('protectURL', models.CharField(max_length=60, verbose_name='外链')),
                ('protectIMG', models.CharField(max_length=60, verbose_name='图片')),
                ('lon', models.FloatField(verbose_name='中心经度')),
                ('lat', models.FloatField(verbose_name='中心伟度')),
                ('fatherPark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.park', verbose_name='所属公园')),
            ],
            options={
                'verbose_name': '公园景点',
                'verbose_name_plural': '公园景点',
                'db_table': 'sd_protect',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMG', models.CharField(max_length=60, verbose_name='图片')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('subTitle', models.CharField(max_length=30, verbose_name='副标题')),
                ('point', models.CharField(max_length=60, verbose_name='要点')),
                ('text', models.CharField(max_length=2000, verbose_name='正文')),
                ('quote', models.CharField(max_length=60, verbose_name='引用位置')),
                ('add_Date', models.DateTimeField(verbose_name='添加时间')),
                ('category', models.CharField(max_length=60, verbose_name='分类')),
                ('fatherPark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.newsposts', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '资讯原文',
                'verbose_name_plural': '资讯原文',
                'db_table': 'sd_news',
            },
        ),
        migrations.CreateModel(
            name='HomeIMGData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeURL', models.CharField(max_length=60, verbose_name='首页外链')),
                ('homeIMG', models.CharField(max_length=60, verbose_name='图片')),
                ('homeTitle', models.CharField(max_length=60, verbose_name='图片标题')),
                ('fatherPark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.homedata', verbose_name='轮播')),
            ],
            options={
                'verbose_name': '轮播',
                'verbose_name_plural': '轮播',
                'db_table': 'sd_homeIMGData',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(max_length=11, unique=True, verbose_name='手机')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'sd_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]