# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')
    parent = models.ForeignKey('self', default=None, blank=True, null=True,
                               verbose_name=u'上级分类')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    # status = models.IntegerField(default=0, choices=STATUS.items(),
    #                              verbose_name=u'状态')

    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'分类'
        ordering = ['rank', '-create_time']

    def __unicode__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'标签'
        ordering = ['rank', '-create_time']

    def __unicode__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, verbose_name=u'作者')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    title = models.CharField(max_length=100, verbose_name=u'标题')
    en_title = models.CharField(max_length=100, verbose_name=u'英文标题')
    img = models.CharField(max_length=200,
                           default='/static/img/article/default.jpg')
    tags = models.ManyToManyField(Tags,max_length=200, null=True, blank=True,
                            verbose_name=u'标签', help_text=u'用逗号分隔')
    summary = models.TextField(verbose_name=u'摘要')
    content = models.TextField(verbose_name=u'正文')
    view_times = models.IntegerField(default=0)
    zan_times = models.IntegerField(default=0)
    is_top = models.BooleanField(default=False, verbose_name=u'置顶')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    # status = models.IntegerField(default=0, choices=STATUS.items(),
    #                              verbose_name='状态')
    pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    # def get_tags(self):
    #     tags_list = self.tags.split(',')
    #     while '' in tags_list:
    #         tags_list.remove('')
    #
    #     return tags_list

    class Meta:
        verbose_name_plural = verbose_name = u'文章'
        ordering = ['rank', '-is_top', '-pub_time', '-create_time']

    def __unicode__(self):
            return self.title

    __str__ = __unicode__

class register(models.Model):
    username = models.CharField(max_length=100, verbose_name=u'用户名')
    password = models.CharField(max_length=100, verbose_name=u'密码')
    email = models.CharField(max_length=200, verbose_name=u'邮箱')
    img = models.CharField(max_length=200, verbose_name=u'用户头像',
                           default='/static/img/head/default.jpeg')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = u'注册用户'
        ordering = ['-create_time']



class Carousel(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    summary = models.TextField(blank=True, null=True, verbose_name=u'摘要')
    img = models.CharField(max_length=200, verbose_name=u'轮播图片',
                           default='/static/img/carousel/default.jpg')
    url = models.CharField(max_length=200, verbose_name=u'图片链接', null=True)
    # article = models.ForeignKey(Article, verbose_name=u'文章')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'轮播'
        ordering = ['-create_time']

        # app_label = string_with_title('blog', u"博客管理")