# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
#    fields = ('title','desc','content')
    list_display = ('title','desc','click_count',)
    list_display_links = ('title','desc',)
    list_editable = ('click_count',)
    fieldsets = (
        (None,{
            'fields':('title','desc','content','user','category','tag',)
        }),
        ('高级设置',{
            'classes': ('collapse',),
            'fields': ('click_count','is_recommand'),
        }),
    )
    class Media:
        js = (
            '../static/js/kindeditor/kindeditor-min.js',
            '../static/js/kindeditor/lang/zh_CN.js',
            '../static/js/kindeditor/config.js',
        )
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Catagory)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)