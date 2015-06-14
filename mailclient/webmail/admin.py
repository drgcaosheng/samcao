#coding:utf-8
from django.contrib import admin
from webmail.models import Publisher,Author,Book

#list_display显示列表名称,并且排序
#search_fields 为搜索框
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name','email')

#list_display显示列表
#list_filter右侧搜索日志
#date_hierarchy顶部日期过滤,接收的是字符串,而不是元组
#ordering按照所指的列进行排序
#fields 编辑表单的字段顺序
#filter_horizontal 添加1对多的多选框
#raw_id_fields 外键多对多.显示搜索文本框
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title','authors','publisher','publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
    
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
