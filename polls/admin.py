from django.contrib import admin
from polls.models import HomeData, Park, Protect, User, News, NewsPosts, HomeIMGData
# Register your models here.
admin.site.site_header = '湿地小程序'  
admin.site.site_title = '湖北湿地' 


admin.site.register(User)

admin.site.register(News)

admin.site.register(Park)

admin.site.register(HomeData)

admin.site.register(HomeIMGData)

admin.site.register(Protect)

admin.site.register(NewsPosts)